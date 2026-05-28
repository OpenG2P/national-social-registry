# OpenG2P Registry NSR Extension

Extension package for the [OpenG2P Registry Platform](https://github.com/OpenG2P/openg2p-registry-gen2-core) that implements the domain of a **National Social Registry (NSR)** — a dynamic repository of poor and vulnerable individuals and households used for targeting, enrolment and delivery across social protection programmes.

Follows the same layout as [`openg2p-registry-farmer-extension`](https://github.com/OpenG2P/openg2p-registry-gen2-extensions/tree/1.0/openg2p-registry-farmer-extension).

## Registers

| Mnemonic | Table | Extends |
|---|---|---|
| `Individual` | `g2p_register_individuals` | `G2PRegister`, `G2PPerson`, `G2PGeo` |
| `Household` | `g2p_register_households` | `G2PRegister`, `G2PGeo` |

## Supporting Tables

| Mnemonic | Table | Parent (via `link_internal_record_id`) |
|---|---|---|
| `IndividualProgram` | `g2p_register_individual_programs` | Individual |
| `IndividualLand` | `g2p_register_individual_land` | Individual |
| `IndividualLivelihood` | `g2p_register_individual_livelihoods` | Individual |
| `IndividualLivestock` | `g2p_register_individual_livestock` | Individual |
| `IndividualVulnerability` | `g2p_register_individual_vulnerability` | Individual |
| `HouseholdProgram` | `g2p_register_household_programs` | Household |
| `HouseholdHousingAndServices` | `g2p_register_household_housing_and_services` | Household |
| `HouseholdAsset` | `g2p_register_household_assets` | Household |
| `IndividualShock` | `g2p_register_individual_shocks` | Individual |
| `IndividualDisability` | `g2p_register_individual_disabilities` | Individual (multi-row per WG functional domain) |

Every register and supporting table has a `*_history` twin for version snapshots.

> Verification / audit trail is provided by the registry-core platform itself (`g2p_register_verifications`); we do not duplicate it here.

## Metadata seed SQL

Portable INSERT scripts used by the National Social Registry docker DB seed job (and manual provisioning) live under `src/openg2p_registry_nsr_extension/meta_data/`:

| Path | Purpose |
|---|---|
| `register-metadata/g2p_register_definitions.sql` | Register/table definitions (`IndividualProgram`, `IndividualLand`, `IndividualLivelihood`, … `HouseholdHousingAndServices`, …) |
| `register-metadata/g2p_register_schemas.sql` | Dedup / search / filter UI schemas per `register_id` |
| `register-metadata/g2p_register_ui_tabs.sql` | Register workspace tabs (`in_*` / `hh_*` labels; not intake) |
| `register-metadata/g2p_register_ui_tab_sections.sql` | Which sections appear on each register tab (reuses `section_id` from sections) |
| `register-metadata/g2p_intake_form_ui_tabs.sql` | One UI tab per intake form (`form_id`) |
| `register-metadata/g2p_intake_form_ui_tab_sections.sql` | Intake tab → ordered sections (same `section_id` PKs as register sections) |
| `register-metadata/g2p_register_sections.sql` | Canonical section definitions (`section_id`); shared by intake + register UI |
| `lookup-data/g2p_attributes.sql` | Shared attribute catalogue (e.g. `PROGRAM_NAME`, `COPING_STRATEGY`) |
| `lookup-data/g2p_attribute_values.sql` | Values for those attributes |
| `data-models/data_models.sql` | Data model hooks |
| `registry-configurations/g2p_registry_configuration.sql` | Registry branding/config |

The seed container runs **all** `.sql` files under `meta_data/` in sorted path order.

## Install (from source)

```bash
pip install openg2p-registry-nsr-extension/
```
