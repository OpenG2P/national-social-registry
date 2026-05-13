INSERT INTO "public"."g2p_register_household_housing_and_services" (
  "dwelling_type","roof_material","wall_material","floor_material","tenure_status",
  "water_source_type","water_distance_minutes","sanitation_type","lighting_source","cooking_fuel_type",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Detail row augmenting dwelling characteristics for HH-NSR-0002 (kitchen / water hardship)
('SEMI_PERMANENT','THATCH','STONE','EARTH','RENTED',
 'WELL',25,'SHARED','SOLAR','FIREWOOD',
 '55000000-0000-4000-8000-000000000001','HHS-NSR-0001','10000000-0000-4000-8000-000000000002',NULL,
 'Secondary dwelling block',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'HHS-NSR-0001 SEMI_PERMANENT WELL','ACTIVE',NULL),

-- HH-NSR-0005 displaced/hosted transient structure
('TEMPORARY','THATCH','BAMBOO','EARTH','HOSTED',
 'PUBLIC_TAP',45,'SHARED','GRID','OTHER',
 '55000000-0000-4000-8000-000000000002','HHS-NSR-0002','10000000-0000-4000-8000-000000000005',NULL,
 'Temporary shelter utilities',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'HHS-NSR-0002 TEMP HOSTED TAP','ACTIVE',NULL);
