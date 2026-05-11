INSERT INTO
    "public"."g2p_intake_form_definitions" (
        "register_id",
        "form_id",
        "number_of_verifications",
        "form_mnemonic",
        "form_description",
        "used_only_in_ingestion_pipeline"
    )
VALUES
    (
        'a0000000-0000-4000-8000-000000000002',
        'c1000000-0000-4000-8000-000000000002',
        0,
        'household_intake_form',
        'This form captures household composition, dwelling conditions, and basic services information.',
        FALSE
    ),

    (
        'a0000000-0000-4000-8000-000000000001',
        'c1000000-0000-4000-8000-000000000001',
        0,
        'individual_intake_form',
        'This form captures personal, vulnerability, and livelihood information for an individual in the national social registry.',
        FALSE
    );
