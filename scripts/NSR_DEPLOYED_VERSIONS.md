# NSR deployed image tags (read-only snapshot)

Captured **2026-05-28** via `openg2p2.yaml` → `kubectl -n nsr`. **Do not modify the NSR cluster.**

```bash
export KUBECONFIG=/path/to/openg2p2.yaml
```

## Registry stack (`nsr` namespace)

| Workload | Image |
|----------|--------|
| registry-staff-portal-api | `mkumar02/openg2p-nsr-registry-staff-portal-api:develop-3` |
| registry-partner-api | `asierneb/openg2p-nsr-registry-partner-api:nsr-fix5` |
| registry-celery-beat-producer | `mkumar02/openg2p-nsr-registry-celery:develop-2` |
| registry-celery-worker | `mkumar02/openg2p-nsr-registry-celery:develop-2` |
| registry-staff-portal-ui | `qniranjan01/openg2p-registry-gen2-staff-portal-ui:nsr-demo-2` |
| registry-id-generator | `openg2p/openg2p-id-generator:1.0.0` |
| registry-db-seed (Job) | `openg2p/openg2p-farmer-registry-db-seed:1.0.3` ⚠️ **wrong** — base-chart default |

Helm release: `registry` → base chart **`openg2p-registry-4.0.0-develop`** (`helm.sh/chart` on deployments).

## Related commons (`nsr` namespace)

| Workload | Image |
|----------|--------|
| commons-services-iam-staff-portal-api | `openg2p/iam-staff-portal-api:1.0` |
| commons-services-master-data-api | `mkumar02/openg2p-gen2-master-data:nsr-demo` |
| commons-services-superset | `asierneb/superset-nsr:4.0.1-ethiopia-drill-v8` |

## Git branches pinned in `docker/*/develop.txt`

Backend/celery images on sandbox are built from **mkumar-02** forks on `develop` (see `docker/*/develop.txt`). UI from **Q-Niranjan** on `develop` (deploy tag `nsr-demo-2`).

| Dependency | Repository | Branch / tag |
|------------|------------|----------------|
| core | `mkumar-02/openg2p-registry-gen2-core` | `develop` |
| apis (staff + partner) | `mkumar-02/openg2p-registry-gen2-apis` | `develop` |
| celery | `mkumar-02/openg2p-registry-gen2-celery` | `develop` |
| iam | `mkumar-02/openg2p-iam-service` | `develop` |
| staff-portal-ui | `Q-Niranjan/openg2p-registry-gen2-staff-portal-ui` | `develop` (image tag `nsr-demo-2`) |
| fastapi-common | `openg2p/openg2p-fastapi-common` | `v1.1.6` |

Partner API **image tag** on sandbox is `nsr-fix5`; source build still tracks `mkumar-02/openg2p-registry-gen2-apis` @ `develop`.

### DB seed (NSR-specific)

| | Image | Seeds |
|---|--------|--------|
| **Cluster today (job image)** | `openg2p/openg2p-farmer-registry-db-seed:1.0.3` | Wrong image on the hook job — **DB content is already NSR** (see below) |
| **Helm target** (`values.yaml` + `values-sandbox.yaml`) | `openg2p/openg2p-nsr-db-seed:develop` | **Configuration only** — `meta_data/` (+ templates); `loadSampleData: false` (no demo individuals/households) |

**Sandbox DB checked 2026-05-28** (`commons-postgresql` / `registry`): 17 register **definitions** (configuration). Live individuals/households on sandbox are operational data — **not** included in the db-seed image.

`meta_data/register-metadata/*.sql` was **re-exported with `pg_dump`** from sandbox (register defs, sections, intake forms, scores config, etc.). Refresh:

```bash
export KUBECONFIG=/path/to/openg2p2.yaml
REG_PASS=$(kubectl get secret registry -n nsr -o jsonpath='{.data.registry-db-user}' | base64 -d)
kubectl exec -n nsr commons-postgresql-0 -- env PGPASSWORD="$REG_PASS" \
  pg_dump -U registry_user -d registry --data-only --inserts -t g2p_register_definitions
```

Built by `.github/workflows/docker-build-db-seed.yml` (`EXTENSION_FOLDER=nsr-extension`). After Helm points at `openg2p-nsr-db-seed:develop`, re-run the db-seed hook on empty DBs only — do not re-seed production without a wipe.

### Refresh commands (read-only)

```bash
export KUBECONFIG=/path/to/openg2p2.yaml

kubectl -n nsr get deploy -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.template.spec.containers[0].image}{"\n"}{end}' \
  | grep -E '^registry-'

kubectl -n nsr get job registry-db-seed -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```
