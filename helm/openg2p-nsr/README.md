# openg2p-nsr

Thin wrapper Helm chart for the **OpenG2P National Social Registry (NSR)**.

This chart does not define templates of its own. It depends on the OpenG2P
Registry Gen 2 base chart and supplies only the NSR-specific overrides:

1. Docker image names for the five NSR components
2. ID Generator `idTypes` — renames the farmer-oriented `farmer_id` type to
   `individual`

Everything else (deployments, services, ingresses, keycloak, postgres,
rabbitmq, helper jobs, …) comes from the base chart.

```
openg2p-registry (4.0.0-develop, base)    +    openg2p-nsr (0.0.0-develop, wrapper)
        │                                              │
        └──────────────────────  =  NSR install  ──────┘
```

## Versioning

Branch-name-equals-version convention:

| Branch | `Chart.yaml.version` | Depends on base chart |
|---|---|---|
| `develop` | `0.0.0-develop` | `4.0.0-develop` |
| `1.0.0` (release tag branch, future) | `1.0.0` | `4.0.0` |

When cutting a release, both `version` and the base chart `dependencies[0].version`
drop the `-develop` suffix together.

## What it overrides

### Images (five NSR services)

| Component | Image (built by this repo) |
|---|---|
| staffPortalApi | `openg2p/openg2p-nsr-staff-portal-api:develop` |
| partnerApi | `openg2p/openg2p-nsr-partner-api:develop` |
| staffPortalUi | `openg2p/openg2p-nsr-staff-portal-ui:develop` |
| celeryWorker / celeryBeat | `openg2p/openg2p-nsr-celery:develop` *(same image — mode picked by env vars)* |
| dbSeed | `openg2p/openg2p-nsr-db-seed:develop` |

### ID Generator `idTypes`

The base chart's `idTypes` is a **map** keyed by id-type name:

```yaml
# base chart default
idTypes:
  farmer:    { idLength: 12 }
  household: { idLength: 10 }
```

NSR adds an `individual` id-type alongside the base's existing entries:

```yaml
# NSR override
idTypes:
  individual:
    idLength: 12
  household:
    idLength: 10
```

After Helm merges the subchart values, the rendered config contains
`farmer`, `household`, and `individual`. The `farmer` entry is inherited
from the base and is **not removed** — Helm's subchart value-merge
treats maps additively and has no reliable way to delete a parent-chart
key via values.yaml (setting it to `null` triggers *"cannot overwrite
table with non table"*).

This is harmless: NSR registers use the mnemonics `Individual` and
`Household`, so the id-generator service is never invoked with `farmer`
as a type. If you need the key gone for cosmetic reasons, the only
clean options are:
- File an upstream change to make the base chart's `idTypes` fully
  replaceable (e.g. via a sentinel key or a `resetIdTypes: true` flag).
- Apply a post-render hook that strips `farmer` from the final manifest.

## Installing

### From this repo (dev / CI)

```bash
cd helm/openg2p-nsr
helm dependency update
helm install nsr . \
  --namespace openg2p-nsr \
  --create-namespace \
  --set openg2p-registry.global.domain=nsr.example.com
```

### From the published Helm repo (once released)

```bash
helm repo add openg2p https://openg2p.github.io/openg2p-helm
helm repo update
helm install nsr openg2p/openg2p-nsr \
  --version 0.0.0-develop \
  --namespace openg2p-nsr \
  --create-namespace
```

### With sample data (dev / test only)

```bash
helm install nsr . \
  --set openg2p-registry.dbSeed.loadSampleData=true
```

Loads the 5 demo households, 15 demo individuals, and supporting-table
demo rows from `nsr-extension/src/.../sample_data/` into the database.

## Upgrading

When the base chart releases a new version, bump the dependency in
`Chart.yaml`:

```yaml
dependencies:
  - name: openg2p-registry
    version: 4.1.0-develop      # was 4.0.0-develop
```

then run `helm dependency update`. For breaking changes, bump this
wrapper's major version too.

## Rejected alternatives (see strategy doc)

- Single chart + `values-nsr.yaml` → no per-variant chart versioning.
- Variant `if` branches inside base chart templates → anti-pattern.
- Wrapper charts inside the base repo → couples variant release cadence
  to base repo branching.
- Mono-repo with per-chart tags → breaks branch-name-equals-version.

## Rancher catalog

The chart ships a `questions.yaml` for Rancher UI installs with fields for:

- Base domain + namespace
- Per-image tag overrides
- DB-seeder toggle (and sample-data toggle)
- Individual id-type prefix / length

Advanced users should edit `values.yaml` directly.
