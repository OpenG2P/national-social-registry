INSERT INTO "public"."approval_stage" (
    "id",
    "policy_id",
    "stage_order",
    "name",
    "mode",
    "mode_value",
    "sla_hours",
    "parallel_group",
    "skip_if",
    "on_empty",
    "on_breach",
    "escalation_rules_json",
    "created_at",
    "updated_at"
)
SELECT v."id", v."policy_id", v."stage_order"::int, v."name", v."mode",
       v."mode_value"::int, v."sla_hours"::int, v."parallel_group"::int,
       v."skip_if"::json, v."on_empty", v."on_breach",
       v."escalation_rules_json"::json, v."created_at"::timestamptz, v."updated_at"::timestamptz
FROM (VALUES
    ('b1000000-0000-4000-8000-000000000101', 'a1000000-0000-4000-8000-000000000001', 1, 'Stage 1 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000102', 'a1000000-0000-4000-8000-000000000001', 2, 'Stage 2 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000201', 'a1000000-0000-4000-8000-000000000002', 1, 'Stage 1 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000202', 'a1000000-0000-4000-8000-000000000002', 2, 'Stage 2 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000111', 'a1000000-0000-4000-8000-000000000011', 1, 'Stage 1 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000112', 'a1000000-0000-4000-8000-000000000011', 2, 'Stage 2 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000121', 'a1000000-0000-4000-8000-000000000012', 1, 'Stage 1 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW()),
    ('b1000000-0000-4000-8000-000000000122', 'a1000000-0000-4000-8000-000000000012', 2, 'Stage 2 Officers', 'all', NULL, NULL, NULL, 'null', 'block', NULL, 'null', NOW(), NOW())
) AS v("id","policy_id","stage_order","name","mode","mode_value","sla_hours",
        "parallel_group","skip_if","on_empty","on_breach","escalation_rules_json",
        "created_at","updated_at")
-- Skip stages whose policy is absent: a policy row can legitimately be skipped
-- above (another registry already owns that policy_key), and without this filter
-- the orphan's FK violation aborts the statement, taking valid stages with it.
WHERE EXISTS (SELECT 1 FROM "public"."approval_policy" p WHERE p.id = v."policy_id")
ON CONFLICT DO NOTHING;
