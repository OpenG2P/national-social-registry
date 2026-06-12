# openg2p-nsr

Self-sufficient Helm chart for the **OpenG2P National Social Registry (NSR)**.

This chart owns its templates directly. It was derived from the OpenG2P
Registry Gen 2 base chart (`openg2p-registry`) — those templates and defaults
now live in this chart, so it **no longer depends on `openg2p-registry`**. The
only NSR-specific differences from the base defaults are:

1. NSR-branded Docker images for the NSR components.
2. `global.registryVariant: nsr`.
3. ID Generator `idTypes`: `individual` (12) + `household` (10).

Everything else (deployments, services, gateways/virtualservices, db-seed Job,
helper subcharts, …) comes from the inlined base-chart templates.

## Sub-dependencies

Same set as the base chart, declared in `Chart.yaml` and fetched from the
OpenG2P Helm repo (the packaged `.tgz` are gitignored, as in the base chart):

| Subchart | Version |
|---|---|
| common | 2.30.0 |
| postgres-init | 1.1.0 |
| redis | 19.6.4 |
| openg2p-id-generator (alias `idgenerator`) | 1.0.0 |
| keycloak-init | 1.1.1 |
| openg2p-awe | 0.0.0-develop |

Run `helm dependency build` (or `update`) before packaging/installing from a
fresh checkout.

## Versioning

Branch-name-equals-version convention:

| Branch | `Chart.yaml.version` |
|---|---|
| `develop` | `0.0.0-develop` |
| `1.0.0` (release tag branch, future) | `1.0.0` |

## Images

| Component | Image |
|---|---|
| staffPortalApi | `openg2p/openg2p-nsr-staff-portal-api:develop` |
| partnerApi | `openg2p/openg2p-nsr-partner-api:develop` |
| staffPortalUi | `openg2p/openg2p-registry-staff-portal-ui:develop` *(built by the `registry-platform` repo)* |
| celeryBeatProducer / celeryWorker | `openg2p/openg2p-nsr-celery:develop` *(same image — mode picked by env vars)* |
| dbSeed | `openg2p/openg2p-nsr-db-seed:develop` |

All NSR API/celery/db-seed images are built by this repo's docker workflows;
the Staff Portal UI image is built by the `registry-platform` repo.

## ID Generator `idTypes`

```yaml
idgenerator:
  idGenerator:
    appConfig:
      idTypes:
        individual:
          idLength: 12
        household:
          idLength: 10
```

## Installing

### From this repo (dev / CI)

```bash
cd helm/openg2p-nsr
helm dependency build
helm install nsr . \
  --namespace openg2p-nsr \
  --create-namespace \
  --set global.registryHostname=nsr.example.com
```

Component URLs are auto-computed from `global.registryHostname`
(default `{{ .Release.Name }}.{{ .Release.Namespace }}.openg2p.org`).

### With sample data (dev / test only)

```bash
helm install nsr . --set dbSeed.loadSampleData=true
```

## Rancher catalog

The chart ships a `questions.yaml` for Rancher UI installs (hostnames,
per-component enable toggles, image repo/tag overrides, db-seed toggles,
id-type note). Advanced users should edit `values.yaml` directly.
