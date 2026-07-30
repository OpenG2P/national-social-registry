#!/usr/bin/env python3
"""Load sample data into NSR Postgres.

Reads:
- /openg2p-data/demography/{individuals,households}.csv (core+geo, shared)
- /seed/seed-data/*.json (NSR sub-tables, shipped in the db-seed image)
"""

import csv
import json
import os
import sys
import uuid
from pathlib import Path

import psycopg2
import psycopg2.extras
from psycopg2.extras import Json


def to_json(value):
    return None if value is None else Json(value)


SEEDER = "seeder"
CREATED_AT = "2026-04-01 00:00:00"

OPENG2P_DATA_DIR = Path(os.environ.get("OPENG2P_DATA_DIR", "/openg2p-data"))
DEMO_DIR = OPENG2P_DATA_DIR / "demography"
NSR_DATA_DIR = Path(os.environ.get("NSR_SEED_DATA_DIR", "/seed/seed-data"))


def env(name: str) -> str:
    value = os.environ.get(name, "")
    if not value:
        print(f"[load-sample-data] Missing env var: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def load_json(path: Path):
    if not path.is_file():
        print(f"[load-sample-data] Missing file: {path}", file=sys.stderr)
        sys.exit(1)
    return json.loads(path.read_text())


JSON_COLUMNS_INDIVIDUAL = {"phone_numbers"}
JSON_COLUMNS_HOUSEHOLD = set()

# Geo is carried in the seed files as plain names (country..village). The
# internal id + hierarchy JSON the registry stores are derived here as a
# slug-path, matching the LEGACY master-data loader (load_geo_data.py + geo.csv).
#
# WARNING: that join no longer holds when Master Data is seeded from a country
# pack, which is now the default. A pack uses the unit's P-code as
# level_value_id, so MDS holds "XK01010101" while the rows written here carry
# "kamuntu/jasiri/baraka/umani/bimaka". Nothing errors — the names in
# geo_code_hierarchy_json still read correctly, so reports that unpack geo
# positionally look fine — but these records cannot be joined to a boundary and
# so never appear on a map.
#
# Only the small demography fixture (~500 people) is affected. The bulk analytics
# sample reads its geography from MDS directly and is pack-coherent.
#
# Fixing it properly is two changes: regenerate openg2p-data/demography from a
# pack so the name paths are real pack paths, and resolve those names against
# MDS here to emit the actual level_value_id.
GEO_LEVELS = ["country", "region", "district", "ward", "village"]


def _slug(name: str) -> str:
    return name.strip().lower().replace(" ", "_")


def geo_lowest_id(rec: dict) -> str:
    """Slug-path of the full country..village chain (= master-data PK)."""
    return "/".join(_slug(rec[level]) for level in GEO_LEVELS)


def geo_hierarchy(rec: dict):
    """Build geo_code_hierarchy_json from the name columns, matching the shape
    registry-core's G2PGeoHierarchyService produces at runtime."""
    hierarchy = []
    for depth, level in enumerate(GEO_LEVELS):
        node_id = "/".join(_slug(rec[GEO_LEVELS[i]]) for i in range(depth + 1))
        hierarchy.append(
            {
                "level_mnemonic": level,
                "level_value_mnemonic": rec[level],
                "level_value_id": node_id,
            }
        )
    return to_json({"hierarchy": hierarchy})


def _read_csv_rows(path: Path, json_columns: set[str]) -> list[dict]:
    if not path.is_file():
        print(f"[load-sample-data] Missing file: {path}", file=sys.stderr)
        sys.exit(1)
    with path.open(newline="", encoding="utf-8") as f:
        out = []
        for row in csv.DictReader(f):
            parsed = {}
            for k, v in row.items():
                if v == "":
                    parsed[k] = None
                elif k in json_columns:
                    parsed[k] = json.loads(v)
                else:
                    parsed[k] = v
            out.append(parsed)
        return out


def _as_int(v):
    return int(v) if v not in (None, "") else None


def search_text_individual(ind: dict) -> str:
    parts = [
        ind["functional_record_id"],
        ind["full_name"],
        ind.get("foundational_id") or "",
        ind.get("foundational_id_masked") or "",
        ind.get("gender") or "",
        ind.get("birth_date") or "",
        str(ind.get("estimated_age") or ""),
        ind.get("marital_status") or "",
    ]
    return " ".join(p for p in parts if p)


def search_text_household(hh: dict) -> str:
    parts = [
        hh["functional_record_id"],
        hh["head_name"],
        hh["headship_type"],
        str(hh["size_total"]),
    ]
    return " ".join(p for p in parts if p)


def insert_individuals(cur, individuals: list[dict]) -> None:
    columns = [
        "internal_record_id", "functional_record_id",
        "link_internal_record_id", "link_foundational_id",
        "record_name", "record_image_document_id",
        "created_by", "created_at", "last_approved_at", "last_approved_by",
        "search_text", "record_status", "record_status_reason",
        "foundational_id", "first_name", "middle_name", "last_name",
        "given_name", "prefix", "suffix",
        "gender", "birth_date", "phone_numbers", "emails",
        "marital_status", "occupation", "income_level",
        "language_code", "education_level", "registration_date",
        "latitude", "longitude", "altitude", "plus_code",
        "address_line_1", "address_line_2", "postal_code", "country_code",
        "geo_lowest_level_value_id", "geo_code_hierarchy_json",
        "foundational_id_masked", "foundational_id_verification_status",
        "full_name", "estimated_age", "age_method",
    ]
    rows = []
    for ind in individuals:
        rows.append(
            (
                ind["internal_record_id"],
                ind["functional_record_id"],
                ind.get("household_id"),  # link to master Household register
                None,
                ind["full_name"],
                None,
                SEEDER,
                CREATED_AT,
                CREATED_AT,
                SEEDER,
                search_text_individual(ind),
                "ACTIVE",
                None,
                ind.get("foundational_id"),
                ind["first_name"],
                ind.get("middle_name"),
                ind["last_name"],
                ind["given_name"],
                None,
                None,
                ind["gender"],
                ind["birth_date"],
                to_json(ind.get("phone_numbers")),
                to_json([ind["emails"]] if ind.get("emails") else None),
                ind["marital_status"],
                None,
                None,
                ind.get("language_code"),
                ind.get("education_level"),
                "2026-04-01",
                ind["latitude"],
                ind["longitude"],
                ind["altitude"],
                ind["plus_code"],
                ind["address_line_1"],
                ind["address_line_2"],
                ind["postal_code"],
                ind["country_code"],
                geo_lowest_id(ind),
                geo_hierarchy(ind),
                ind["foundational_id_masked"],
                "VERIFIED",
                ind["full_name"],
                _as_int(ind.get("estimated_age")),
                "DOCUMENTED",
            )
        )
    sql = (
        f'INSERT INTO "public"."g2p_register_individuals" ('
        + ", ".join(f'"{c}"' for c in columns)
        + ") VALUES %s ON CONFLICT (\"internal_record_id\") DO NOTHING"
    )
    psycopg2.extras.execute_values(cur, sql, rows, template=None, page_size=200)
    print(f"[load-sample-data]   -> g2p_register_individuals: {len(rows)}")


def insert_households(cur, households: list[dict]) -> None:
    columns = [
        "internal_record_id", "functional_record_id",
        "link_internal_record_id", "link_foundational_id",
        "record_name", "record_image_document_id",
        "created_by", "created_at", "last_approved_at", "last_approved_by",
        "search_text", "record_status", "record_status_reason",
        "latitude", "longitude", "altitude", "plus_code",
        "address_line_1", "address_line_2", "postal_code", "country_code",
        "geo_lowest_level_value_id", "geo_code_hierarchy_json",
        "household_head_internal_record_id", "household_head_name",
        "headship_type", "size_total", "size_adults", "size_children_u5",
        "size_school_age", "size_elderly",
        "number_of_female_members", "number_of_male_members",
        "elderly_member_present",
    ]
    rows = []
    for hh in households:
        size_elderly = _as_int(hh.get("size_elderly")) or 0
        rows.append(
            (
                hh["internal_record_id"],
                hh["functional_record_id"],
                None,
                None,
                f"{hh['head_name']} {hh['functional_record_id']}",
                None,
                SEEDER,
                CREATED_AT,
                CREATED_AT,
                SEEDER,
                search_text_household(hh),
                "ACTIVE",
                None,
                hh["latitude"],
                hh["longitude"],
                hh["altitude"],
                hh["plus_code"],
                hh["address_line_1"],
                hh["address_line_2"],
                hh["postal_code"],
                hh["country_code"],
                geo_lowest_id(hh),
                geo_hierarchy(hh),
                hh["head_individual_id"],
                hh["head_name"],
                hh["headship_type"],
                _as_int(hh.get("size_total")),
                _as_int(hh.get("size_adults")),
                _as_int(hh.get("size_children_u5")),
                _as_int(hh.get("size_school_age")),
                size_elderly,
                _as_int(hh.get("number_of_female_members")),
                _as_int(hh.get("number_of_male_members")),
                "TRUE" if size_elderly > 0 else "FALSE",
            )
        )
    sql = (
        f'INSERT INTO "public"."g2p_register_households" ('
        + ", ".join(f'"{c}"' for c in columns)
        + ") VALUES %s ON CONFLICT (\"internal_record_id\") DO NOTHING"
    )
    psycopg2.extras.execute_values(cur, sql, rows, template=None, page_size=200)
    print(f"[load-sample-data]   -> g2p_register_households: {len(rows)}")


SUB_TABLES = [
    (
        "g2p_register_individual_livelihoods",
        "individual_livelihoods.json",
        ["primary_livelihood", "secondary_livelihood", "employment_status", "coping_strategies_index", "mobile_phone_type"],
    ),
    (
        "g2p_register_individual_livestock",
        "individual_livestock.json",
        ["livestock_species", "livestock_counts"],
    ),
    (
        "g2p_register_individual_land",
        "individual_land.json",
        ["land_access", "land_size", "productive_assets"],
    ),
    (
        "g2p_register_individual_shocks",
        "individual_shocks.json",
        ["shock_type", "shock_date", "shock_period", "coping_strategy"],
    ),
    (
        "g2p_register_individual_disabilities",
        "individual_disabilities.json",
        ["disability_domain", "disability_severity"],
    ),
    (
        "g2p_register_individual_vulnerability",
        "individual_vulnerability.json",
        [
            "disability_status", "orphanhood_flag", "chronic_illness_flag",
            "displacement_status", "pastoralist_classification",
            "high_mobility_indicator", "plw_status", "plw_status_date",
        ],
    ),
    (
        "g2p_register_individual_programs",
        "individual_programs.json",
        ["program_name", "program_start_date", "program_exit_date"],
    ),
    (
        "g2p_register_household_assets",
        "household_assets.json",
        ["asset_type", "asset_category", "quantity", "size_value", "size_unit", "size_band", "details"],
    ),
    (
        "g2p_register_household_housing_and_services",
        "household_housing_and_services.json",
        [
            "dwelling_type", "roof_material", "wall_material", "floor_material",
            "tenure_status", "water_source_type", "water_distance_minutes",
            "sanitation_type", "lighting_source", "cooking_fuel_type",
        ],
    ),
    (
        "g2p_register_household_programs",
        "household_programs.json",
        ["program_name", "program_start_date", "program_exit_date"],
    ),
]

COMMON_COLUMNS = [
    "internal_record_id", "functional_record_id",
    "link_internal_record_id", "link_foundational_id",
    "record_name", "record_image_document_id",
    "created_by", "created_at", "last_approved_at", "last_approved_by",
    "search_text", "record_status", "record_status_reason",
]


def insert_sub_table(cur, table: str, rows_json: list[dict], extra_cols: list[str]) -> None:
    if not rows_json:
        print(f"[load-sample-data]   -> {table}: 0 (empty)")
        return
    columns = COMMON_COLUMNS + extra_cols
    rows = []
    for r in rows_json:
        common = [
            r["internal_record_id"],
            r["functional_record_id"],
            r["link_internal_record_id"],
            r.get("link_foundational_id"),
            r["record_name"],
            r.get("record_image_document_id"),
            r.get("created_by", SEEDER),
            r.get("created_at", CREATED_AT),
            r.get("last_approved_at", CREATED_AT),
            r.get("last_approved_by", SEEDER),
            r["search_text"],
            r.get("record_status", "ACTIVE"),
            r.get("record_status_reason"),
        ]
        extras = [r.get(c) for c in extra_cols]
        rows.append(tuple(common + extras))

    sql = (
        f'INSERT INTO "public"."{table}" ('
        + ", ".join(f'"{c}"' for c in columns)
        + ") VALUES %s ON CONFLICT (\"internal_record_id\") DO NOTHING"
    )
    psycopg2.extras.execute_values(cur, sql, rows, template=None, page_size=200)
    print(f"[load-sample-data]   -> {table}: {len(rows)}")


def insert_scores(cur, scores: list[dict]) -> None:
    if not scores:
        return
    columns = [
        "internal_record_id", "register_id", "score_type", "score_definition_id",
        "link_internal_record_id", "triggered_by_cr_id", "triggered_by_submission_id",
        "computed_score", "computed_at",
    ]
    rows = [tuple(r.get(c) for c in columns) for r in scores]
    sql = (
        f'INSERT INTO "public"."g2p_register_scores" ('
        + ", ".join(f'"{c}"' for c in columns)
        + ") VALUES %s ON CONFLICT (\"internal_record_id\") DO NOTHING"
    )
    psycopg2.extras.execute_values(cur, sql, rows, template=None, page_size=200)
    print(f"[load-sample-data]   -> g2p_register_scores: {len(rows)}")


# Stable namespace so re-running the seed produces the same queue_id per
# (register, record, section) — combined with ON CONFLICT DO NOTHING this
# makes completion-score enqueueing idempotent.
_QUEUE_NS = uuid.UUID("a1b2c3d4-0000-4000-8000-000000000001")


def get_register_id(cur, mnemonic: str):
    cur.execute(
        'SELECT register_id FROM "public"."g2p_register_definitions" '
        "WHERE register_mnemonic = %s",
        (mnemonic,),
    )
    row = cur.fetchone()
    return row[0] if row else None


def qualifying_sections(cur, register_id: str) -> list[str]:
    """Sections enqueued for completion scoring: own-register sections plus any
    list section, EXCLUDING sections backed by a CORE_TABLE register (e.g. the
    Score section).

    The completion-score worker resolves each section's model as
    G2PRegister<section_register_mnemonic> from the extensions
    register_domain.models. CORE_TABLE registers (e.g. Score) have no such
    generated model — their model lives in registry-core — so enqueuing them
    makes the worker fail with "has no attribute 'G2PRegisterScore'"."""
    cur.execute(
        "SELECT s.section_id, s.section_register_id, s.is_list, d.register_purpose "
        'FROM "public"."g2p_register_sections" s '
        'LEFT JOIN "public"."g2p_register_definitions" d '
        "  ON d.register_id = s.section_register_id "
        "WHERE s.register_id = %s",
        (register_id,),
    )
    out = []
    for section_id, section_register_id, is_list, purpose in cur.fetchall():
        if section_register_id != register_id and not is_list:
            continue
        if purpose == "CORE_TABLE":
            continue
        out.append(section_id)
    return out


def enqueue_completion_scores(cur, register_id: str, record_ids: list[str]) -> None:
    """Seed PENDING g2p_completion_score_computation_queue rows for each
    (record, qualifying section) so the worker computes scores later."""
    if not register_id:
        print("[load-sample-data]   -> completion-score queue: register not found, skipped")
        return
    sections = qualifying_sections(cur, register_id)
    if not sections:
        print(f"[load-sample-data]   -> completion-score queue ({register_id}): no sections")
        return
    rows = []
    for rid in record_ids:
        for sid in sections:
            queue_id = str(uuid.uuid5(_QUEUE_NS, f"{register_id}:{rid}:{sid}"))
            rows.append((queue_id, register_id, rid, sid, None, None, "PENDING", 0))
    columns = [
        "queue_id", "register_id", "internal_record_id", "section_id",
        "change_request_id", "submission_id",
        "compute_status", "compute_number_of_attempts",
    ]
    sql = (
        'INSERT INTO "public"."g2p_completion_score_computation_queue" ('
        + ", ".join(f'"{c}"' for c in columns)
        + ") VALUES %s ON CONFLICT (queue_id) DO NOTHING"
    )
    psycopg2.extras.execute_values(cur, sql, rows, template=None, page_size=500)
    print(
        f"[load-sample-data]   -> completion-score queue: {len(rows)} rows "
        f"({len(record_ids)} records x {len(sections)} sections)"
    )


def main() -> None:
    print("[load-sample-data] Starting…")
    print(f"[load-sample-data] OPENG2P_DATA_DIR = {OPENG2P_DATA_DIR}")
    print(f"[load-sample-data] NSR_SEED_DATA_DIR = {NSR_DATA_DIR}")

    individuals = _read_csv_rows(DEMO_DIR / "individuals.csv", JSON_COLUMNS_INDIVIDUAL)
    households = _read_csv_rows(DEMO_DIR / "households.csv", JSON_COLUMNS_HOUSEHOLD)

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
        insert_individuals(cur, individuals)
        insert_households(cur, households)
        for table, fname, extras in SUB_TABLES:
            rows = load_json(NSR_DATA_DIR / fname)
            insert_sub_table(cur, table, rows, extras)
        scores = load_json(NSR_DATA_DIR / "scores.json")
        insert_scores(cur, scores)

        # Seed completion-score computation queue so the worker can compute
        # section completion scores for every seeded individual and household.
        enqueue_completion_scores(
            cur,
            get_register_id(cur, "Individual"),
            [ind["internal_record_id"] for ind in individuals],
        )
        enqueue_completion_scores(
            cur,
            get_register_id(cur, "Household"),
            [hh["internal_record_id"] for hh in households],
        )

        conn.commit()
        print("[load-sample-data] Done.")
    except Exception as exc:
        conn.rollback()
        print(f"[load-sample-data] FAILED: {exc}", file=sys.stderr)
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
