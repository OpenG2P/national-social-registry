INSERT INTO "public"."approval_policy" (
    "id",
    "policy_key",
    "version",
    "name",
    "description",
    "status",
    "artifact_type",
    "created_by",
    "forbid_self_approval",
    "forbid_repeat_approvers",
    "created_at",
    "updated_at"
) VALUES
    ('a1000000-0000-4000-8000-000000000001', 'registry.change_request.individual', 1, 'Policy for Individual Change Request', NULL, 'active', 'registry.change_request', 'seed', 'FALSE', 'FALSE', NOW(), NOW()),
    ('a1000000-0000-4000-8000-000000000002', 'registry.change_request.household', 1, 'Policy for Household Change Request', NULL, 'active', 'registry.change_request', 'seed', 'FALSE', 'FALSE', NOW(), NOW()),
    ('a1000000-0000-4000-8000-000000000011', 'registry.intake_form.individual', 1, 'Policy for Individual Intake Form', NULL, 'active', 'registry.intake_form', 'seed', 'FALSE', 'FALSE', NOW(), NOW()),
    ('a1000000-0000-4000-8000-000000000012', 'registry.intake_form.household', 1, 'Policy for Household Intake Form', NULL, 'active', 'registry.intake_form', 'seed', 'FALSE', 'FALSE', NOW(), NOW())
-- Untargeted DO NOTHING, not ON CONFLICT ("id"): `approval_policy` also carries
-- uq_policy_key_version. AWE is shared across registries, so another registry can
-- already own the same policy_key under a DIFFERENT id; targeting "id" leaves that
-- natural-key clash unguarded and the whole multi-row statement aborts, landing
-- none of the policies. Untargeted skips only the offending row.
ON CONFLICT DO NOTHING;
