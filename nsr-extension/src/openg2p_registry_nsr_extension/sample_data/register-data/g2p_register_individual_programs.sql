INSERT INTO "public"."g2p_register_individual_programs" (
  "program_name","program_mnemonic","program_start_date","program_exit_date",
  "legacy_program_id","payment_channel_preference","payment_account_token","payment_verification_status",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Alex Rivera (IND-NSR-0001) enrolled in Cash Transfer
('PROG_CASH_TRANSFER','CASH_TRANSFER','2025-01-01',NULL,
 'LEG-CT-00001','BANK','TOK-bank-****0001','VERIFIED',
 '30000000-0000-4000-8000-000000000001','PP-NSR-0001','20000000-0000-4000-8000-000000000001',NULL,
 'Cash Transfer Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0001 Cash Transfer Programme CASH_TRANSFER BANK VERIFIED','ACTIVE',NULL),

-- Morgan Cole (IND-NSR-0004) enrolled in Health Insurance
('PROG_HEALTH_INSURANCE','HEALTH_INSURANCE','2024-06-01',NULL,
 'LEG-HI-00120','CASH',NULL,'VERIFIED',
 '30000000-0000-4000-8000-000000000003','PP-NSR-0003','20000000-0000-4000-8000-000000000004',NULL,
 'Health Insurance Scheme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0003 Health Insurance Scheme','ACTIVE',NULL),

-- Rin Lee (IND-NSR-0009) elderly pension
('PROG_ELDERLY_PENSION','ELDERLY_PENSION','2023-01-01',NULL,
 'LEG-EP-00088','BANK','TOK-bank-****0088','VERIFIED',
 '30000000-0000-4000-8000-000000000004','PP-NSR-0004','20000000-0000-4000-8000-000000000009',NULL,
 'Elderly Pension',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0004 Elderly Pension BANK','ACTIVE',NULL),

-- Taylor Brooks (IND-NSR-0010) disability allowance
('PROG_DISABILITY_ALLOWANCE','DISABILITY_ALLOWANCE','2025-03-01',NULL,
 'LEG-DA-00021','MOBILE_MONEY','TOK-momo-****0021','PENDING',
 '30000000-0000-4000-8000-000000000005','PP-NSR-0005','20000000-0000-4000-8000-000000000010',NULL,
 'Disability Allowance',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0005 Disability Allowance PENDING','ACTIVE',NULL),

-- Noah Rivera (IND-NSR-0003) school feeding
('PROG_SCHOOL_FEEDING','SCHOOL_FEEDING','2024-09-01',NULL,
 'LEG-SF-00712','OTHER',NULL,'VERIFIED',
 '30000000-0000-4000-8000-000000000007','PP-NSR-0007','20000000-0000-4000-8000-000000000003',NULL,
 'School Feeding Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0007 School Feeding Programme','ACTIVE',NULL),

-- Asha Hayes (IND-NSR-0015) school feeding
('PROG_SCHOOL_FEEDING','SCHOOL_FEEDING','2024-09-01',NULL,
 'LEG-SF-00713','OTHER',NULL,'VERIFIED',
 '30000000-0000-4000-8000-000000000008','PP-NSR-0008','20000000-0000-4000-8000-000000000015',NULL,
 'School Feeding Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0008 School Feeding Programme','ACTIVE',NULL),

-- Sam Hayes (IND-NSR-0013) exited public works
('PROG_PUBLIC_WORKS','PUBLIC_WORKS','2023-01-01','2024-12-31',
 'LEG-PW-00999','CASH',NULL,'VERIFIED',
 '30000000-0000-4000-8000-000000000009','PP-NSR-0009','20000000-0000-4000-8000-000000000013',NULL,
 'Public Works Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0009 Public Works Programme exited','INACTIVE','EXITED');
