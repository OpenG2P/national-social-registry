INSERT INTO "public"."g2p_register_definitions" ("register_id","register_mnemonic","register_subject","register_description","master_register_id","register_rank","register_purpose","program_id","program_mnemonic","register_icon","has_image","dedup_is_enabled","dedup_threshold_score","functional_id_generation_required") VALUES
-- Top-level registers
-- Household is the master register (rank 2). Individual nests under Household
-- via master_register_id, mirroring the pattern used by farmer & original NSR.
('a0000000-0000-4000-8000-000000000002','Household','Households','Household register — composition, headship, dwelling conditions and basic services',NULL,2,'REGISTER',NULL,NULL,'','FALSE','TRUE',0.7,'TRUE'),
('a0000000-0000-4000-8000-000000000001','Individual','Individuals','Individual register — personal demographics, vulnerability and inclusion indicators, livelihoods','a0000000-0000-4000-8000-000000000002',1,'REGISTER',NULL,NULL,'','FALSE','TRUE',0.75,'TRUE'),
-- Supporting tables attached to Individual
('b0000000-0000-4000-8000-000000000010','IndividualProgram','Individual Programs','Programme enrolments linked to an individual','a0000000-0000-4000-8000-000000000001',10,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000012','IndividualLand','Individual Land','Land access, plot size and productive assets linked to an individual','a0000000-0000-4000-8000-000000000001',11,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000013','IndividualLivelihood','Individual Livelihoods','Primary and secondary livelihood, employment and coping indicators','a0000000-0000-4000-8000-000000000001',12,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000014','IndividualLivestock','Individual Livestock','Livestock species and herd-size bands per individual','a0000000-0000-4000-8000-000000000001',13,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000015','IndividualVulnerability','Individual Vulnerability','Structured vulnerability and mobility indicators per individual','a0000000-0000-4000-8000-000000000001',14,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000040','IndividualShock','Individual Shocks','Shocks experienced by an individual (drought, flood, illness, etc.)','a0000000-0000-4000-8000-000000000001',40,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000080','IndividualDisability','Individual Disabilities','Per-domain functional difficulty (Washington Group Short Set) with severity — one row per domain','a0000000-0000-4000-8000-000000000001',80,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
-- Supporting tables attached to Household
('b0000000-0000-4000-8000-000000000090','HouseholdProgram','Household Programs','Programme enrolments linked to a household','a0000000-0000-4000-8000-000000000002',25,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000011','HouseholdHousingAndServices','Household Housing and Services','Dwelling materials, water, sanitation, lighting and cooking fuel (household-level detail rows)','a0000000-0000-4000-8000-000000000002',20,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000030','HouseholdAsset','Household Assets','Household assets — land, livestock, productive tools, consumer durables','a0000000-0000-4000-8000-000000000002',30,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE');
