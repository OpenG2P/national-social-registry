# NSR DB-seed image.
#
# Small Postgres-client image that ships the extension's SQL seed scripts
# (meta_data + optional sample data) and, at container-run time, applies them
# against a target Postgres via the entrypoint script.
#
# Build context = repo root (so that nsr-extension/ and docker/db-seed/ are
# both reachable). Based on the pattern from openg2p-registry-gen2-extensions,
# with the source folder renamed from configurations/ to meta_data/.

ARG EXTENSION_FOLDER=nsr-extension

FROM postgres:16-alpine

ARG EXTENSION_FOLDER
ARG GIT_COMMIT=dev
ARG BUILD_TIME=dev

ENV GIT_COMMIT=${GIT_COMMIT} \
    BUILD_TIME=${BUILD_TIME} \
    EXTENSION_FOLDER=${EXTENSION_FOLDER}

# Copy seed SQL scripts from the extension source tree:
#   meta_data/   — register definitions, schemas, tabs, sections, attributes, registry-config
#   sample_data/ — demo rows (households, individuals, supporting tables)
COPY ${EXTENSION_FOLDER}/src/ /tmp/ext-src/

# The Python package folder inside src/ varies, so use `find` to locate the
# meta_data/ and sample_data/ folders wherever they live under src/.
RUN mkdir -p /seed/meta_data /seed/sample_data && \
    find /tmp/ext-src -maxdepth 2 -type d -name meta_data | while read d; do \
      cp -r "$d"/* /seed/meta_data/ 2>/dev/null || true; \
    done && \
    find /tmp/ext-src -maxdepth 2 -type d -name sample_data | while read d; do \
      cp -r "$d"/* /seed/sample_data/ 2>/dev/null || true; \
    done && \
    rm -rf /tmp/ext-src

COPY docker/db-seed/entrypoint.sh /seed/entrypoint.sh
RUN chmod +x /seed/entrypoint.sh

ENTRYPOINT ["/seed/entrypoint.sh"]
