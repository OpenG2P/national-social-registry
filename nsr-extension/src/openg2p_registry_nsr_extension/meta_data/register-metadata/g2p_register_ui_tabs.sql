-- Register workspace tabs (`g2p_register_ui_tabs`). Intake is *not* a register tab —
-- each tab groups sections from `g2p_register_sections` via `g2p_register_ui_tab_sections`.
INSERT INTO public.g2p_register_ui_tabs (
    tab_id,
    register_id,
    tab_label,
    tab_order,
    is_active
)
VALUES
    -- Household register (`9055ab43-…` → NSR canonical household id)
    ('household_info_tab', 'a0000000-0000-4000-8000-000000000002', 'household_info_tab', 1, TRUE),
    ('household_membership_tab', 'a0000000-0000-4000-8000-000000000002', 'household_membership_tab', 2, TRUE),
    ('housing_services_tab', 'a0000000-0000-4000-8000-000000000002', 'housing_services_tab', 3, TRUE),
    ('household_programs', 'a0000000-0000-4000-8000-000000000002', 'household_programs', 4, TRUE),

    -- Individual register (`a1a4d25a-…` → NSR canonical individual id)
    ('individual_info_tab', 'a0000000-0000-4000-8000-000000000001', 'individual_info', 1, TRUE),
    ('individual_livelihood_tab', 'a0000000-0000-4000-8000-000000000001', 'livelihood', 2, TRUE),
    ('individual_vulnerability_tab', 'a0000000-0000-4000-8000-000000000001', 'vulnerability', 5, TRUE),
    ('individual_programs_tab', 'a0000000-0000-4000-8000-000000000001', 'programs', 9, TRUE);
