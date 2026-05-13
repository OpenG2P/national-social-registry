-- IndividualProgram rows (`g2p_register_individual_programs`). Columns match
-- ``G2PRegisterIndividualProgram`` / ``ProgramEnum`` (`PROGRAM_NAME` value_ids).
INSERT INTO "public"."g2p_register_individual_programs" (
  "program_name","program_start_date","program_exit_date",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Alex Rivera (IND-NSR-0001)
('PROG_CASH_TRANSFER','2025-01-01',NULL,
 '30000000-0000-4000-8000-000000000001','PP-NSR-0001','20000000-0000-4000-8000-000000000001',NULL,
 'Cash Transfer Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0001 PROG_CASH_TRANSFER','ACTIVE',NULL),

-- Morgan Cole (IND-NSR-0004)
('PROG_HEALTH_INSURANCE','2024-06-01',NULL,
 '30000000-0000-4000-8000-000000000003','PP-NSR-0003','20000000-0000-4000-8000-000000000004',NULL,
 'Health Insurance Scheme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0003 PROG_HEALTH_INSURANCE','ACTIVE',NULL),

-- Rin Lee (IND-NSR-0009)
('PROG_ELDERLY_PENSION','2023-01-01',NULL,
 '30000000-0000-4000-8000-000000000004','PP-NSR-0004','20000000-0000-4000-8000-000000000009',NULL,
 'Elderly Pension',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0004 PROG_ELDERLY_PENSION','ACTIVE',NULL),

-- Taylor Brooks (IND-NSR-0010)
('PROG_DISABILITY_ALLOWANCE','2025-03-01',NULL,
 '30000000-0000-4000-8000-000000000005','PP-NSR-0005','20000000-0000-4000-8000-000000000010',NULL,
 'Disability Allowance',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0005 PROG_DISABILITY_ALLOWANCE','ACTIVE',NULL),

-- Noah Rivera (IND-NSR-0003)
('PROG_SCHOOL_FEEDING','2024-09-01',NULL,
 '30000000-0000-4000-8000-000000000007','PP-NSR-0007','20000000-0000-4000-8000-000000000003',NULL,
 'School Feeding Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0007 PROG_SCHOOL_FEEDING','ACTIVE',NULL),

-- Asha Hayes (IND-NSR-0015)
('PROG_SCHOOL_FEEDING','2024-09-01',NULL,
 '30000000-0000-4000-8000-000000000008','PP-NSR-0008','20000000-0000-4000-8000-000000000015',NULL,
 'School Feeding Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0008 PROG_SCHOOL_FEEDING','ACTIVE',NULL),

-- Sam Hayes (IND-NSR-0013) exited public works
('PROG_PUBLIC_WORKS','2023-01-01','2024-12-31',
 '30000000-0000-4000-8000-000000000009','PP-NSR-0009','20000000-0000-4000-8000-000000000013',NULL,
 'Public Works Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PP-NSR-0009 PROG_PUBLIC_WORKS','INACTIVE','EXITED');
