INSERT INTO "public"."g2p_register_definitions" ("register_id","register_mnemonic","register_subject","register_description","master_register_id","register_rank","register_purpose","program_id","program_mnemonic","register_icon","has_image","dedup_is_enabled","dedup_threshold_score","functional_id_generation_required") VALUES
-- Top-level registers
('a0000000-0000-4000-8000-000000000001','Individual','Individuals','Individual register — personal demographics, vulnerability and inclusion indicators, livelihoods',NULL,1,'REGISTER',NULL,NULL,'','FALSE','TRUE',0.75,'TRUE'),
('a0000000-0000-4000-8000-000000000002','Household','Households','Household register — composition, headship, dwelling conditions and basic services',NULL,2,'REGISTER',NULL,NULL,'','FALSE','TRUE',0.7,'TRUE'),
-- Supporting tables attached to Individual
('b0000000-0000-4000-8000-000000000010','ProgramParticipation','Program Participations','Enrolment of individuals or households in social protection programmes','a0000000-0000-4000-8000-000000000001',10,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000040','Shock','Shocks','Shocks experienced by an individual (drought, flood, illness, etc.)','a0000000-0000-4000-8000-000000000001',40,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000050','Consent','Consents','Informed consent records for collection and sharing of personal data','a0000000-0000-4000-8000-000000000001',50,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000060','Grievance','Grievances','Grievance cases raised by individuals regarding registry data or programme inclusion','a0000000-0000-4000-8000-000000000001',60,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000070','VerificationHistory','Verification History','Update and verification audit trail for registry records','a0000000-0000-4000-8000-000000000001',70,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
-- Supporting tables attached to Household
('b0000000-0000-4000-8000-000000000020','PovertyScore','Poverty Scores','Poverty assessment scores (PMT, MPI, PPI, custom) for households','a0000000-0000-4000-8000-000000000002',20,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE'),
('b0000000-0000-4000-8000-000000000030','Asset','Assets','Household assets — land, livestock, productive tools, consumer durables','a0000000-0000-4000-8000-000000000002',30,'TABLE',NULL,NULL,NULL,'FALSE','FALSE',0,'FALSE');
