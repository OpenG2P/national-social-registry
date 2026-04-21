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
| `ProgramParticipation` | `g2p_register_program_participations` | Individual or Household |
| `PovertyScore` | `g2p_register_poverty_scores` | Household |
| `Asset` | `g2p_register_assets` | Household |
| `Shock` | `g2p_register_shocks` | Individual |
| `Consent` | `g2p_register_consents` | Individual |
| `Grievance` | `g2p_register_grievances` | Individual |
| `VerificationHistory` | `g2p_register_verification_history` | Individual or Household |

Every register and supporting table has a `*_history` twin for version snapshots.

## Install (from source)

```bash
pip install openg2p-registry-nsr-extension/
```
