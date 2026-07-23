#!/usr/bin/env python3
"""Upload sample profile images to MinIO and link them to g2p_register_individuals.

Images are stored under openg2p-data/demography/images/IND-XXXX.jpg.
Each image is uploaded under the same filename to a MinIO bucket and the
corresponding row in g2p_register_individuals is updated with
record_image_document_id = filename.
"""

import os
import sys
from pathlib import Path

import psycopg2
from minio import Minio


def env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if value is None or value == "":
        print(f"[upload-images] Missing required env var: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def main() -> None:
    images_dir = Path(
        os.environ.get("IMAGES_DIR", "/openg2p-data/demography/images")
    )
    bucket_name = env("IMAGE_BUCKET_NAME", "registrant-photos")
    endpoint = env("MINIO_ENDPOINT")
    access_key = env("MINIO_ACCESS_KEY")
    secret_key = env("MINIO_SECRET_KEY")
    secure = os.environ.get("MINIO_SECURE", "false").lower() in ("1", "true", "yes")

    if not images_dir.is_dir():
        print(f"[upload-images] Images directory not found: {images_dir}", file=sys.stderr)
        sys.exit(1)

    image_files = sorted(images_dir.glob("*.jpg"))
    if not image_files:
        print(f"[upload-images] No .jpg files found in {images_dir}", file=sys.stderr)
        sys.exit(1)

    client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"[upload-images] Created MinIO bucket: {bucket_name}")

    print(
        f"[upload-images] Uploading {len(image_files)} image(s) to s3://{bucket_name}/ …"
    )
    uploaded: list[tuple[str, str]] = []
    for path in image_files:
        client.fput_object(bucket_name, path.name, str(path), content_type="image/jpeg")
        uploaded.append((path.stem, path.name))
    print(f"[upload-images] Uploaded {len(uploaded)} images.")

    # Update DB references. functional_record_id matches stem (e.g. IND-0001).
    conn = psycopg2.connect(
        host=env("PGHOST"),
        port=os.environ.get("PGPORT", "5432"),
        dbname=env("PGDATABASE"),
        user=env("PGUSER"),
        password=env("PGPASSWORD"),
    )
    conn.autocommit = False
    cur = conn.cursor()
    try:
        cur.executemany(
            'UPDATE "public"."g2p_register_individuals" '
            "SET record_image_document_id = %s "
            "WHERE functional_record_id = %s",
            [(obj_key, fr_id) for fr_id, obj_key in uploaded],
        )
        conn.commit()
        print(
            f"[upload-images] Updated {cur.rowcount} rows in g2p_register_individuals."
        )
    except Exception as exc:
        conn.rollback()
        print(f"[upload-images] DB update FAILED: {exc}", file=sys.stderr)
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
