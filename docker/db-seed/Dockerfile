# National Social Registry — DB-seed image.
#
# Thin extension of the registry-platform db-seed base image. The base ships the
# seeding machinery (entrypoint.sh, the shared openg2p-data clone, geo loader,
# template uploader) plus the reference registry's seed content. This image
# replaces the seed content with NSR's, and overrides the two loaders that are
# NOT domain-agnostic.
#
# WHICH LOADERS ARE DOMAIN-SPECIFIC
#   The base image's load_sample_data.py and upload_images.py are written against
#   the FARMER schema — they INSERT into g2p_register_farmers/crops/lands/... and
#   read farmers.json, crops.json, lands.json. NSR has none of those tables or
#   files (it has g2p_register_individuals plus individual_*/household_* sub
#   tables), so inheriting them makes the Job crash-loop on LOAD_SAMPLE_DATA=true.
#   NSR therefore ships its own, copied over the inherited ones below.
#
#   Genuinely generic and inherited unchanged: entrypoint.sh, load_geo_data.py
#   (geo is registry-agnostic), upload_templates.py, requirements.txt.
#
# The entrypoint (inherited) reads /seed/* at container-run time; behaviour is
# toggled entirely via env from the Helm Job.
#
# Build context = repo root (so nsr-extension/ and docker/db-seed/ are both
# reachable).
ARG RP_VERSION=0.0.0-develop.299
FROM openg2p/openg2p-registry-db-seed:${RP_VERSION}

# The RP db-seed image ships the reference registry's seed; clear it so only
# NSR's seed is applied.
RUN rm -rf /seed/meta_data/* /seed/awe_meta_data/* /seed/templates/* /seed/seed-data/*

COPY nsr-extension/src/openg2p_registry_nsr_extension/meta_data/     /seed/meta_data/
COPY nsr-extension/src/openg2p_registry_nsr_extension/awe_meta_data/ /seed/awe_meta_data/
COPY nsr-extension/src/openg2p_registry_nsr_extension/templates/     /seed/templates/
COPY docker/db-seed/seed-data/                                       /seed/seed-data/

# NSR's domain-specific loaders, overriding the base image's farmer-shaped ones.
COPY docker/db-seed/load_sample_data.py /seed/load_sample_data.py
COPY docker/db-seed/upload_images.py    /seed/upload_images.py

# NSR's reporting layer. Unlike the sample generator — which lives in
# openg2p-data and is already present via the base image's clone at
# /openg2p-data — these views are NSR's own schema and ship with this image.
COPY docker/db-seed/reporting_views.sql /seed/reporting_views.sql
RUN chmod +x /seed/load_sample_data.py /seed/upload_images.py
