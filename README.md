# National Social Registry (NSR)

National Social Registry is a manifestation of the [OpenG2P Registry Platform](https://github.com/OpenG2P/openg2p-registry-gen2-core) with specifics related to a national-level social registry of poor and vulnerable individuals and households for targeting, enrolment, and delivery across social protection programmes.

```
OpenG2P Registry Platform  +  NSR Extensions  =  National Social Registry
```

This repository contains the NSR extensions — a pip-installable Python package that plugs into the OpenG2P Registry Platform.

## Registers

NSR defines two top-level registers:

1. **Individual Register** — personal demographics, vulnerability flags, livelihoods
2. **Household Register** — composition, headship, dwelling conditions, services

Individuals are linked to a household via `link_internal_record_id` on the Individual record (nullable — individuals may also exist independently).

## Supporting Tables

Multi-valued or time-series data is captured in supporting tables linked to an Individual or Household:

| Table | Parent |
|---|---|
| Program Participation | Individual or Household |
| Poverty Score | Household |
| Asset | Household |
| Shock | Individual |
| Consent | Individual |
| Grievance | Individual |
| Verification History | Individual or Household |

## Extension package

See [`openg2p-registry-nsr-extension/`](openg2p-registry-nsr-extension/).
