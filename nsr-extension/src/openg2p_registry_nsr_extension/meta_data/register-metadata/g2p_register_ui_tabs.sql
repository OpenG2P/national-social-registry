INSERT INTO
    public.g2p_register_ui_tabs (
        "tab_id",
        "register_id",
        "tab_label",
        "tab_order",
        "is_active"
    )
VALUES
    -- Individual register tabs (same tab_id / register_id / label / order as before; intake metadata moved to g2p_intake_form_definitions)
    ('individual_intake_form_tab', 'a0000000-0000-4000-8000-000000000001', '', 0, TRUE),
    ('individual_individual_tab', 'a0000000-0000-4000-8000-000000000001', 'individual', 1, TRUE),
    ('individual_household_tab', 'a0000000-0000-4000-8000-000000000001', 'household', 2, TRUE),
    ('individual_program_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_programs', 3, TRUE),
    ('individual_land_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_land', 4, TRUE),
    ('individual_livelihood_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_livelihoods', 5, TRUE),
    ('individual_livestock_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_livestock', 6, TRUE),
    ('individual_vulnerability_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_vulnerability', 7, TRUE),
    ('individual_shock_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_shocks', 8, TRUE),
    ('individual_disability_tab', 'a0000000-0000-4000-8000-000000000001', 'disabilities', 9, TRUE),

    -- Household register tabs
    ('household_intake_form_tab', 'a0000000-0000-4000-8000-000000000002', '', 0, TRUE),
    ('household_household_tab', 'a0000000-0000-4000-8000-000000000002', 'household', 1, TRUE),
    ('household_individual_tab', 'a0000000-0000-4000-8000-000000000002', 'individual', 2, TRUE),
    ('household_housing_and_services_tab', 'a0000000-0000-4000-8000-000000000002', 'household_housing_and_services', 3, TRUE),
    ('household_asset_tab', 'a0000000-0000-4000-8000-000000000002', 'household_assets', 4, TRUE),
    ('household_program_tab', 'a0000000-0000-4000-8000-000000000002', 'household_programs', 5, TRUE);
