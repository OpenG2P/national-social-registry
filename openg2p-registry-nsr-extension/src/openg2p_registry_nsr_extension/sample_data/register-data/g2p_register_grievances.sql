INSERT INTO "public"."g2p_register_grievances" (
  "grievance_case_id","grievance_type","submission_channel","grievance_status",
  "submission_date","resolution_date","resolution_code","resolution_rationale","protection_referral_flag",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Alex Rivera — exclusion complaint, resolved
('GRV-2026-0001','EXCLUSION','PHONE','RESOLVED',
 '2026-02-15','2026-03-01','ADDED','GR_VALID','FALSE',
 '80000000-0000-4000-8000-000000000001','GRV-NSR-0001','20000000-0000-4000-8000-000000000001',NULL,
 'GRV-2026-0001 EXCLUSION',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'GRV-NSR-0001 GRV-2026-0001 EXCLUSION PHONE RESOLVED ADDED','ACTIVE',NULL),

-- Taylor Brooks — protection concern, referred
('GRV-2026-0002','PROTECTION','IN_PERSON','REFERRED',
 '2026-03-05',NULL,'REFERRED','GR_OUT_OF_SCOPE','TRUE',
 '80000000-0000-4000-8000-000000000002','GRV-NSR-0002','20000000-0000-4000-8000-000000000010',NULL,
 'GRV-2026-0002 PROTECTION',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'GRV-NSR-0002 GRV-2026-0002 PROTECTION IN_PERSON REFERRED','ACTIVE',NULL),

-- Morgan Cole — data error open
('GRV-2026-0003','DATA_ERROR','COMMUNITY_COMMITTEE','UNDER_REVIEW',
 '2026-03-20',NULL,NULL,NULL,'FALSE',
 '80000000-0000-4000-8000-000000000003','GRV-NSR-0003','20000000-0000-4000-8000-000000000004',NULL,
 'GRV-2026-0003 DATA_ERROR',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'GRV-NSR-0003 GRV-2026-0003 DATA_ERROR UNDER_REVIEW','ACTIVE',NULL),

-- Sam Hayes — payment delay
('GRV-2026-0004','PAYMENT','USSD','OPEN',
 '2026-03-28',NULL,NULL,NULL,'FALSE',
 '80000000-0000-4000-8000-000000000004','GRV-NSR-0004','20000000-0000-4000-8000-000000000013',NULL,
 'GRV-2026-0004 PAYMENT',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'GRV-NSR-0004 GRV-2026-0004 PAYMENT USSD OPEN','ACTIVE',NULL);
