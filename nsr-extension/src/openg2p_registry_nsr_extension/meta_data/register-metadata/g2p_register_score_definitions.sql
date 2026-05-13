-- Poverty score keyed to the Household subject register (`register_id`).
-- Contributing attributes align with NSR household columns; weights mirrored from farmer-extension (45% household size, 55% young children density proxy).
INSERT INTO "public"."g2p_register_score_definitions" ("score_definition_id","register_id","score_type","contributing_attributes","score_config","is_enabled") VALUES
('e0000000-0000-4000-8000-000000000001','a0000000-0000-4000-8000-000000000002','POVERTY','["size_total","size_children_u5"]','{"weights":{"size_total":0.45,"size_children_u5":0.55}}',TRUE);
