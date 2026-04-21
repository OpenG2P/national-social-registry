INSERT INTO "public"."g2p_register_consents" (
  "consent_captured","consent_date","consent_scope","consent_method","consent_evidence_ref","data_sharing_restrictions",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
('TRUE','2026-04-01','["TARGETING","PROGRAM_ENROLMENT","GRIEVANCE_MANAGEMENT"]','DIGITAL','doc-store://consent/0001',NULL,
 '70000000-0000-4000-8000-000000000001','CNS-NSR-0001','20000000-0000-4000-8000-000000000001',NULL,
 'DIGITAL 2026-04-01',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'CNS-NSR-0001 DIGITAL 2026-04-01 consent_captured TRUE','ACTIVE',NULL),

('TRUE','2026-04-01','["TARGETING","PROGRAM_ENROLMENT"]','DIGITAL','doc-store://consent/0002',NULL,
 '70000000-0000-4000-8000-000000000002','CNS-NSR-0002','20000000-0000-4000-8000-000000000002',NULL,
 'DIGITAL 2026-04-01',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'CNS-NSR-0002 DIGITAL 2026-04-01','ACTIVE',NULL),

('TRUE','2026-04-01','["TARGETING","PROGRAM_ENROLMENT","HEALTH_DATA_SHARING"]','SIGNED','doc-store://consent/0004',
 '{"restrict_commercial_use": true}',
 '70000000-0000-4000-8000-000000000003','CNS-NSR-0003','20000000-0000-4000-8000-000000000004',NULL,
 'SIGNED 2026-04-01',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'CNS-NSR-0003 SIGNED 2026-04-01','ACTIVE',NULL),

('TRUE','2026-04-01','["TARGETING"]','VERBAL',NULL,'{"restrict_cross_border_transfer": true}',
 '70000000-0000-4000-8000-000000000004','CNS-NSR-0004','20000000-0000-4000-8000-000000000010',NULL,
 'VERBAL 2026-04-01',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'CNS-NSR-0004 VERBAL 2026-04-01 displaced','ACTIVE',NULL),

('TRUE','2026-04-01','["TARGETING","PROGRAM_ENROLMENT"]','BIOMETRIC','doc-store://consent/0013',NULL,
 '70000000-0000-4000-8000-000000000005','CNS-NSR-0005','20000000-0000-4000-8000-000000000013',NULL,
 'BIOMETRIC 2026-04-01',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'CNS-NSR-0005 BIOMETRIC 2026-04-01','ACTIVE',NULL),

('FALSE','2026-04-01','[]','VERBAL',NULL,'{"refusal_reason": "minor_without_guardian_consent"}',
 '70000000-0000-4000-8000-000000000006','CNS-NSR-0006','20000000-0000-4000-8000-000000000012',NULL,
 'VERBAL 2026-04-01',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder',
 'CNS-NSR-0006 VERBAL 2026-04-01 not_captured','ACTIVE',NULL);
