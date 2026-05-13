-- One intake-form tab per `g2p_intake_form_definitions.form_id` (farmer: single tab per form).
-- The tab references the same `section_id` rows as the register definitions — no duplicate section rows.
INSERT INTO public.g2p_intake_form_ui_tabs (
    tab_id,
    form_id,
    tab_label,
    tab_order
)
VALUES
    (
        'nsr_form_tab_household_intake',
        'c1000000-0000-4000-8000-000000000002',
        'household_intake_form',
        1
    ),
    (
        'nsr_form_tab_individual_intake',
        'c1000000-0000-4000-8000-000000000001',
        'individual_intake_form',
        1
    );
