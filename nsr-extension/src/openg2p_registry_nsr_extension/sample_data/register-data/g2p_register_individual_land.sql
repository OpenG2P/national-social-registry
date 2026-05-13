INSERT INTO "public"."g2p_register_individual_land" (
  "land_access","land_size","productive_assets",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Agricultural household member (IND-NSR-0004, Morgan Cole)
(TRUE, 0.5, '["PLOUGH", "OTHER"]'::jsonb,
 '61000000-0000-4000-8000-000000000001','LND-NSR-0001','20000000-0000-4000-8000-000000000004',NULL,
 'Land row 1',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'LND-NSR-0001 ACCESS 0.5','ACTIVE',NULL),

-- Pastoral-linked member (IND-NSR-0013, Sam Hayes): shared grazing access only
(TRUE, NULL, NULL,
 '61000000-0000-4000-8000-000000000002','LND-NSR-0002','20000000-0000-4000-8000-000000000013',NULL,
 'Land row 2',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'LND-NSR-0002 ACCESS','ACTIVE',NULL);
