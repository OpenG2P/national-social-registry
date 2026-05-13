INSERT INTO "public"."g2p_register_individual_livelihoods" (
  "primary_livelihood","secondary_livelihood","employment_status","coping_strategies_index","mobile_phone_type",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Secondary diversified activity for household head Alex Rivera (individual row also has primary job)
('BUSINESS_TRADE','UNEMPLOYED','SELF_EMPLOYED',1,'SMARTPHONE',
 '62000000-0000-4000-8000-000000000001','LIV-NSR-0001','20000000-0000-4000-8000-000000000001',NULL,
 'Petty trade supplement',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'LIV-NSR-0001 BUSINESS_TRADE SMARTPHONE','ACTIVE',NULL),

-- Morgan Cole — farm + casual labour rotation
('AGRICULTURE','WAGE_LABOR','UNEMPLOYED',4,'BASIC',
 '62000000-0000-4000-8000-000000000002','LIV-NSR-0002','20000000-0000-4000-8000-000000000004',NULL,
 'Agricultural livelihood row',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'LIV-NSR-0002 AGRICULTURE WAGE_LABOR','ACTIVE',NULL),

-- Sam Hayes — pastoralist bands
('LIVESTOCK',NULL,'SELF_EMPLOYED',6,'NONE',
 '62000000-0000-4000-8000-000000000003','LIV-NSR-0003','20000000-0000-4000-8000-000000000013',NULL,
 'Livestock primary',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'LIV-NSR-0003 LIVESTOCK','ACTIVE',NULL);
