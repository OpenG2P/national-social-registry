INSERT INTO "public"."g2p_register_poverty_scores" (
  "pmt_score","pmt_score_type","pmt_variables","pmt_calculation_date","pmt_model_version",
  "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
  "record_name","record_image_storage_id","created_by","created_at","last_approved_at",
  "last_approved_by","search_text","record_status","record_status_reason"
) VALUES
(42.5,'PMT','{"size_total": 4, "tenure_status": "OWNED", "dwelling_type": "PERMANENT", "water_source_type": "PIPED"}','2026-02-01','v1.0',
 '40000000-0000-4000-8000-000000000001','PMT-NSR-0001','10000000-0000-4000-8000-000000000001',NULL,
 'PMT 42.5',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PMT 42.5 v1.0 PMT-NSR-0001 Poverty Score HH-NSR-0001','ACTIVE',NULL),

(68.3,'PMT','{"size_total": 5, "tenure_status": "RENTED", "dwelling_type": "SEMI_PERMANENT"}','2026-02-01','v1.0',
 '40000000-0000-4000-8000-000000000002','PMT-NSR-0002','10000000-0000-4000-8000-000000000002',NULL,
 'PMT 68.3',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PMT 68.3 v1.0 PMT-NSR-0002 Poverty Score HH-NSR-0002','ACTIVE',NULL),

(35.8,'PMT','{"size_total": 6, "tenure_status": "OWNED", "dwelling_type": "PERMANENT"}','2026-02-01','v1.0',
 '40000000-0000-4000-8000-000000000003','PMT-NSR-0003','10000000-0000-4000-8000-000000000003',NULL,
 'PMT 35.8',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PMT 35.8 v1.0 PMT-NSR-0003 Poverty Score HH-NSR-0003','ACTIVE',NULL),

(88.9,'MPI','{"deprivations": ["housing", "sanitation", "cooking_fuel", "water_access"]}','2026-02-01','mpi-2025',
 '40000000-0000-4000-8000-000000000004','PMT-NSR-0004','10000000-0000-4000-8000-000000000004',NULL,
 'MPI 88.9',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','MPI 88.9 mpi-2025 PMT-NSR-0004 Poverty Score HH-NSR-0004','ACTIVE',NULL),

(61.2,'PMT','{"size_total": 7, "livelihood": "LIVESTOCK", "pastoralist": true}','2026-02-01','v1.0',
 '40000000-0000-4000-8000-000000000005','PMT-NSR-0005','10000000-0000-4000-8000-000000000005',NULL,
 'PMT 61.2',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00',
 'seeder','PMT 61.2 v1.0 PMT-NSR-0005 Poverty Score HH-NSR-0005','ACTIVE',NULL);
