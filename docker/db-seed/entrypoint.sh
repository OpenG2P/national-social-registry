#!/bin/sh
set -e

# ──────────────────────────────────────────────────────────────
# OpenG2P Registry DB Seed Entrypoint
#
# Meta-data SQL ships with the nsr-extension (register definitions, schemas,
# tabs, sections, lookups, configs). Sample registrant data, sub-table data
# and profile images come from openg2p-data (cloned into /openg2p-data at
# image build time).
#
# Expected environment variables:
#   PGHOST, PGPORT (default 5432), PGDATABASE, PGUSER, PGPASSWORD
#   LOAD_SAMPLE_DATA - "true" to load demography + NSR sub-tables (default false)
#   LOAD_IMAGES      - "true" to upload profile images to MinIO (default false)
#   LOAD_TEMPLATES   - "true" to upload Jinja templates to MinIO (default false)
#   MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_SECURE
#   TEMPLATE_BUCKET_NAME (default "template"), TEMPLATES_DIR
#   IMAGE_BUCKET_NAME (default "registrant-photos"), IMAGES_DIR
#   OPENG2P_DATA_DIR (default "/openg2p-data")
# ──────────────────────────────────────────────────────────────

PGPORT="${PGPORT:-5432}"
LOAD_SAMPLE_DATA="${LOAD_SAMPLE_DATA:-false}"
LOAD_IMAGES="${LOAD_IMAGES:-false}"
LOAD_TEMPLATES="${LOAD_TEMPLATES:-false}"

SEED_DIR="/seed"
META_DATA_DIR="${SEED_DIR}/meta_data"

run_sql_files() {
  dir="$1"
  label="$2"

  if [ ! -d "$dir" ]; then
    echo "[db-seed] No ${label} directory found at ${dir}, skipping."
    return
  fi

  sql_files=$(find "$dir" -name '*.sql' -type f | sort)
  if [ -z "$sql_files" ]; then
    echo "[db-seed] No SQL files found in ${dir}, skipping."
    return
  fi

  echo "[db-seed] Running ${label} scripts from ${dir} ..."
  for f in $sql_files; do
    echo "[db-seed]   -> $(basename "$f")"
    psql -v ON_ERROR_STOP=0 -f "$f"
  done
  echo "[db-seed] ${label} scripts completed."
}

echo "============================================="
echo " OpenG2P Registry DB Seed"
echo " Extension     : ${EXTENSION_FOLDER:-unknown}"
echo " Database      : ${PGDATABASE}@${PGHOST}:${PGPORT}"
echo " Sample data   : ${LOAD_SAMPLE_DATA}"
echo " Images        : ${LOAD_IMAGES}"
echo " Templates     : ${LOAD_TEMPLATES}"
echo "============================================="

# 1. Meta-data SQL (always)
run_sql_files "$META_DATA_DIR" "meta-data"

# 2. Sample data from openg2p-data JSON
if [ "$LOAD_SAMPLE_DATA" = "true" ]; then
  echo "[db-seed] Loading sample data from openg2p-data ..."
  python3 /seed/load_sample_data.py
else
  echo "[db-seed] Skipping sample data (LOAD_SAMPLE_DATA=${LOAD_SAMPLE_DATA})."
fi

# 3. Profile images to MinIO
if [ "$LOAD_IMAGES" = "true" ]; then
  echo "[db-seed] Uploading profile images to MinIO ..."
  python3 /seed/upload_images.py
else
  echo "[db-seed] Skipping image upload (LOAD_IMAGES=${LOAD_IMAGES})."
fi

# 4. Jinja templates to MinIO
if [ "$LOAD_TEMPLATES" = "true" ]; then
  echo "[db-seed] Uploading templates to MinIO ..."
  python3 /seed/upload_templates.py
else
  echo "[db-seed] Skipping template upload (LOAD_TEMPLATES=${LOAD_TEMPLATES})."
fi

echo "[db-seed] Done."
