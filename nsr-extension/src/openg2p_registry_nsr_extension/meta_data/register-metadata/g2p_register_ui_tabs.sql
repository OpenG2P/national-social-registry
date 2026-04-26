INSERT INTO "public"."g2p_register_ui_tabs" ("tab_id","register_id","tab_label","tab_order","used_for_new_intake_form","no_of_verifications_required","intake_form_name","intake_form_description","intake_form_auto_approve","is_active") VALUES
-- Individual register tabs
('individual_intake_form_tab','a0000000-0000-4000-8000-000000000001','',0,'TRUE',0,'Individual Intake Form','This form captures personal, vulnerability, and livelihood information for an individual in the national social registry.','TRUE','TRUE'),
('individual_individual_tab','a0000000-0000-4000-8000-000000000001','individual',1,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('individual_household_tab','a0000000-0000-4000-8000-000000000001','household',2,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('individual_program_tab','a0000000-0000-4000-8000-000000000001','programs',3,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('individual_shock_tab','a0000000-0000-4000-8000-000000000001','shocks',4,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('individual_consent_tab','a0000000-0000-4000-8000-000000000001','consents',5,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('individual_grievance_tab','a0000000-0000-4000-8000-000000000001','grievances',6,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('individual_disability_tab','a0000000-0000-4000-8000-000000000001','disabilities',7,'FALSE',0,NULL,NULL,'FALSE','TRUE'),

-- Household register tabs
('household_intake_form_tab','a0000000-0000-4000-8000-000000000002','',0,'TRUE',0,'Household Intake Form','This form captures household composition, dwelling conditions, and basic services information.','TRUE','TRUE'),
('household_household_tab','a0000000-0000-4000-8000-000000000002','household',1,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('household_individual_tab','a0000000-0000-4000-8000-000000000002','individual',2,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('household_poverty_tab','a0000000-0000-4000-8000-000000000002','poverty_scores',3,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('household_asset_tab','a0000000-0000-4000-8000-000000000002','assets',4,'FALSE',0,NULL,NULL,'FALSE','TRUE'),
('household_program_tab','a0000000-0000-4000-8000-000000000002','programs',5,'FALSE',0,NULL,NULL,'FALSE','TRUE');
