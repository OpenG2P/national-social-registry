# National Social Registry (NSR)

An installable **National Social Registry** built as a thin extension of the
OpenG2P [registry platform](https://github.com/OpenG2P/registry-platform). Under
the inverted build model the platform publishes the runnable base images and the
`openg2p-registry` Helm chart; this repo adds **only** the NSR domain on top.

## What this repo owns

| Path | Purpose |
|---|---|
| `nsr-extension/` | The NSR domain package — Individual and Household registers and their sub-registers, schemas, services, seed metadata (registers, AWE policy, DCI templates) |
| `docker/` | Thin Dockerfiles (`FROM openg2p/openg2p-registry-*` + `pip install nsr-extension`) selected at runtime by `REGISTRY_EXTENSION_MODULE` (Option C), plus NSR's sample seed JSON |
| `helm/openg2p-nsr/` | A thin wrapper chart: pins `openg2p-registry` as a dependency and supplies the NSR values overlay (no templates) |

There is **no NSR sanity suite in this repo**: NSR's registers, tables
(`g2p_register_individuals`), DCI template shape, register id, UI tab and section
are the same ones the platform's reference registry ships — the reference was
derived from NSR — so the published `openg2p-registry-sanity-tests` image applies
unchanged. It is enabled from the chart values.

The `openg2p-registry` base image tag (`RP_VERSION` in each Dockerfile) and the
chart dependency version in `helm/openg2p-nsr/Chart.yaml` are **hardcoded and
pinned together**. The NSR images and the wrapper chart are versioned in lockstep
by CI (one version per commit).

## Deploy

```bash
helm repo add openg2p https://openg2p.github.io/openg2p-helm
helm dependency build ./helm/openg2p-nsr
helm install nsr ./helm/openg2p-nsr \
  --set global.registryHostname=nsr.example.org
```

Set `registry.sanity.runE2e=true` to run the end-to-end sanity suite after install.

See the deployment & extension docs at [docs.openg2p.org](https://docs.openg2p.org).
