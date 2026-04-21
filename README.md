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

See [`nsr-extension/`](nsr-extension/).

## Docker images

All Docker build definitions live under [`docker/`](docker/). Four images are produced:

| Image | Built from | Spec file |
|---|---|---|
| `openg2p/openg2p-nsr-staff-portal-api:<branch>` | `docker/staff-portal-api/Dockerfile` | [`docker/staff-portal-api/develop.txt`](docker/staff-portal-api/develop.txt) |
| `openg2p/openg2p-nsr-partner-api:<branch>` | `docker/partner-api/Dockerfile` | [`docker/partner-api/develop.txt`](docker/partner-api/develop.txt) |
| `openg2p/openg2p-nsr-celery:<branch>` | `docker/celery/Dockerfile` | [`docker/celery/develop.txt`](docker/celery/develop.txt) |
| `openg2p/openg2p-nsr-staff-portal-ui:<branch>` | `docker/staff-portal-ui/Dockerfile` | [`docker/staff-portal-ui/develop.txt`](docker/staff-portal-ui/develop.txt) |

Each spec file pins the OpenG2P platform libraries (fastapi-common, iam-core, registry-core, registry-apis, celery) to specific versions, and references the NSR extension as a **local path** (`./nsr-extension`) so the image always bakes in the current working tree. The Docker build context is `docker/`; the NSR extension source is copied into `docker/local_deps/nsr-extension/` at build time.

### Building locally

Run the script from the project root. Service-file paths are relative to `docker/`:

```bash
# Build a single service
./docker/scripts/build.sh staff-portal-api/develop.txt

# Build all four defaults (no push)
./docker/scripts/build.sh

# Build and push to Docker Hub (requires docker/scripts/.env with DOCKER_HUB_USERNAME + DOCKER_HUB_TOKEN)
./docker/scripts/build.sh --push staff-portal-api/develop.txt
```

See [`docker/scripts/README.md`](docker/scripts/README.md) for all options (multi-arch, no-cache, custom Dockerfile, etc.).

### Building in CI

Two manually-triggered GitHub Actions workflows are provided:

- **Build & Push Backend Dockers** — `.github/workflows/docker-build-backend.yml`
- **Build & Push UI Dockers** — `.github/workflows/docker-build-ui.yml`

Trigger them from the Actions tab; each accepts a `service_file` input (defaults to `docker/.../develop.txt`).

### Building for a different branch

The image tag is read from the first line of the spec file (`#!openg2p/...:<tag>`). To build for a new branch:

1. Copy `develop.txt` to `<branch-name>.txt` inside the service directory under `docker/`
2. Update the `#!` image tag on line 1
3. Optionally change any pinned version references
4. Run the build locally or trigger the workflow with the new spec file path
