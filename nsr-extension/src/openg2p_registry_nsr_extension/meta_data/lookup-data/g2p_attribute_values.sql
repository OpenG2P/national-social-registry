INSERT INTO "public"."g2p_attribute_values" ("value_id","attribute_id","value_code","value_display","parent_value_id") VALUES
-- Programme names (generic placeholders)
('PROG_CASH_TRANSFER','PROGRAM_NAME','CASH_TRANSFER','Cash Transfer Programme',NULL),
('PROG_FOOD_SUPPORT','PROGRAM_NAME','FOOD_SUPPORT','Food Support Programme',NULL),
('PROG_HEALTH_INSURANCE','PROGRAM_NAME','HEALTH_INSURANCE','Health Insurance Scheme',NULL),
('PROG_DISABILITY_ALLOWANCE','PROGRAM_NAME','DISABILITY_ALLOWANCE','Disability Allowance',NULL),
('PROG_ELDERLY_PENSION','PROGRAM_NAME','ELDERLY_PENSION','Elderly Pension',NULL),
('PROG_SCHOOL_FEEDING','PROGRAM_NAME','SCHOOL_FEEDING','School Feeding Programme',NULL),
('PROG_PUBLIC_WORKS','PROGRAM_NAME','PUBLIC_WORKS','Public Works Programme',NULL),

-- Primary livelihood (ISCO-aligned broad groupings)
('LVH_AGRICULTURE','PRIMARY_LIVELIHOOD','AGRICULTURE','Agriculture, Forestry and Fishing',NULL),
('LVH_LIVESTOCK','PRIMARY_LIVELIHOOD','LIVESTOCK','Livestock Rearing',NULL),
('LVH_CRAFT','PRIMARY_LIVELIHOOD','CRAFT','Craft and Related Trades',NULL),
('LVH_SERVICES','PRIMARY_LIVELIHOOD','SERVICES','Services and Sales',NULL),
('LVH_WAGE_LABOUR','PRIMARY_LIVELIHOOD','WAGE_LABOUR','Casual Wage Labour',NULL),
('LVH_PETTY_TRADE','PRIMARY_LIVELIHOOD','PETTY_TRADE','Petty Trading',NULL),
('LVH_GOVT_EMPLOYMENT','PRIMARY_LIVELIHOOD','GOVT_EMPLOYMENT','Government Employment',NULL),
('LVH_UNEMPLOYED','PRIMARY_LIVELIHOOD','UNEMPLOYED','Unemployed / No Livelihood',NULL),
('LVH_OTHER','PRIMARY_LIVELIHOOD','OTHER','Other',NULL),

-- Coping strategies
('CS_REDUCE_MEALS','COPING_STRATEGY','REDUCE_MEALS','Reduce number or size of meals',NULL),
('CS_BORROW','COPING_STRATEGY','BORROW','Borrow from family/friends',NULL),
('CS_SELL_ASSETS','COPING_STRATEGY','SELL_ASSETS','Sell productive assets',NULL),
('CS_MIGRATE','COPING_STRATEGY','MIGRATE','Migrate for work',NULL),
('CS_WITHDRAW_SCHOOL','COPING_STRATEGY','WITHDRAW_SCHOOL','Withdraw children from school',NULL),
('CS_SEEK_AID','COPING_STRATEGY','SEEK_AID','Seek emergency aid',NULL),
('CS_NONE','COPING_STRATEGY','NONE','No coping strategy',NULL),

-- Data source
('DS_SELF_REPORT','DATA_SOURCE','SELF_REPORT','Self-report',NULL),
('DS_FIELD_VERIFICATION','DATA_SOURCE','FIELD_VERIFICATION','Field verification',NULL),
('DS_PROGRAMME_MIS','DATA_SOURCE','PROGRAMME_MIS','Programme MIS integration',NULL),
('DS_FOUNDATIONAL_ID','DATA_SOURCE','FOUNDATIONAL_ID','Foundational ID API',NULL),
('DS_COMMUNITY_VALIDATION','DATA_SOURCE','COMMUNITY_VALIDATION','Community validation',NULL),

-- Grievance resolution rationale
('GR_VALID','GRIEVANCE_RESOLUTION_RATIONALE','VALID','Valid — corrective action taken',NULL),
('GR_INVALID','GRIEVANCE_RESOLUTION_RATIONALE','INVALID','Invalid — claim not supported',NULL),
('GR_DUPLICATE','GRIEVANCE_RESOLUTION_RATIONALE','DUPLICATE','Duplicate case',NULL),
('GR_OUT_OF_SCOPE','GRIEVANCE_RESOLUTION_RATIONALE','OUT_OF_SCOPE','Out of registry scope — referred',NULL),
('GR_INSUFFICIENT_EVIDENCE','GRIEVANCE_RESOLUTION_RATIONALE','INSUFFICIENT_EVIDENCE','Insufficient evidence',NULL);
