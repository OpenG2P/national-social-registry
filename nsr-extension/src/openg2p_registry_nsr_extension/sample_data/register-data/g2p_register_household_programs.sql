-- HouseholdProgram rows (`g2p_register_household_programs`). Columns match
-- ``G2PRegisterHouseholdProgram`` / ``ProgramEnum`` (`PROGRAM_NAME` value_ids).
INSERT INTO "public"."g2p_register_household_programs" (
  "program_name","program_start_date","program_exit_date",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
-- Morgan Cole household (HH-NSR-0002)
('PROG_CASH_TRANSFER','2024-06-01',NULL,
 '30000000-0000-4000-8000-000000000002','HPP-NSR-0001','10000000-0000-4000-8000-000000000002',NULL,
 'Cash Transfer Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','HPP-NSR-0001 PROG_CASH_TRANSFER','ACTIVE',NULL),

-- Sam Hayes household (HH-NSR-0005)
('PROG_FOOD_SUPPORT','2025-10-01',NULL,
 '30000000-0000-4000-8000-000000000006','HPP-NSR-0002','10000000-0000-4000-8000-000000000005',NULL,
 'Food Support Programme',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','HPP-NSR-0002 PROG_FOOD_SUPPORT','ACTIVE',NULL);
