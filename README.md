# National Social Registry (NSR)

OpenG2P National Social Registry is a manifestation of the [OpenG2P Registry Platform](https://github.com/OpenG2P/openg2p-registry-gen2-core), tuned for a national-level registry of poor and vulnerable individuals and households used to target, enrol and deliver social-protection programmes.

📖 **Full documentation:** [docs.openg2p.org → National Social Registry](https://docs.openg2p.org/products/registry/national-social-registry)

The documentation covers the registers and supporting tables, the domain model, versioning, the Helm wrapper chart (and how it inherits from the base registry chart), the Docker images, meta-data seeding, and how NSR plugs into Rancher.

## Repository layout

```
nsr-extension/        Python package — SQLAlchemy models, Pydantic schemas,
                      domain services, ID generator, meta-data + sample SQL
docker/               Dockerfile + spec file for each of the five images
helm/openg2p-nsr/     Thin wrapper chart over the base registry chart
.github/workflows/    Path-scoped CI for docker images and the helm chart
```

## License

[Mozilla Public License 2.0](LICENSE)
