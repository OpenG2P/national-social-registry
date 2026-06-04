# NSR DB-seed image.
#
# Postgres-client image that ships:
#   - meta_data SQL from the nsr-extension (register definitions, schemas, etc.)
#   - flat Jinja templates from the nsr-extension
#   - openg2p-data repo (cloned at build time) containing demography JSON,
#     NSR sub-table JSON and profile images
# At container-run time it:
#   - applies meta_data SQL against Postgres
#   - optionally loads sample data from openg2p-data JSON via load_sample_data.py
#   - optionally uploads profile images to MinIO via upload_images.py
#   - optionally uploads Jinja templates to MinIO via upload_templates.py
#
# Build context = repo root (so that nsr-extension/ and docker/db-seed/ are
# both reachable).

ARG EXTENSION_FOLDER=nsr-extension

FROM postgres:16-alpine

ARG EXTENSION_FOLDER
ARG GIT_COMMIT=dev
ARG BUILD_TIME=dev
ARG OPENG2P_DATA_REPO=https://github.com/psnappz/openg2p-data.git
ARG OPENG2P_DATA_BRANCH=2.0

ENV GIT_COMMIT=${GIT_COMMIT} \
    BUILD_TIME=${BUILD_TIME} \
    EXTENSION_FOLDER=${EXTENSION_FOLDER} \
    OPENG2P_DATA_DIR=/openg2p-data

RUN apk add --no-cache python3 py3-pip git

COPY docker/db-seed/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir --break-system-packages -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Copy meta-data SQL and flat templates from the extension source tree.
# (sample_data/ no longer exists in the extension — data lives in openg2p-data.)
COPY ${EXTENSION_FOLDER}/src/ /tmp/ext-src/

RUN mkdir -p /seed/meta_data /seed/templates && \
    find /tmp/ext-src -maxdepth 2 -type d -name meta_data | while read d; do \
      cp -r "$d"/* /seed/meta_data/ 2>/dev/null || true; \
    done && \
    find /tmp/ext-src -maxdepth 2 -type d -name templates | while read d; do \
      find "$d" -maxdepth 1 -type f -name '*.j2' -exec cp {} /seed/templates/ \; ; \
    done && \
    rm -rf /tmp/ext-src

# Clone openg2p-data (demography JSON, NSR sub-table JSON, images, users).
RUN git clone --depth 1 -b ${OPENG2P_DATA_BRANCH} ${OPENG2P_DATA_REPO} /openg2p-data \
    && rm -rf /openg2p-data/.git

COPY docker/db-seed/entrypoint.sh /seed/entrypoint.sh
COPY docker/db-seed/upload_templates.py /seed/upload_templates.py
COPY docker/db-seed/upload_images.py /seed/upload_images.py
COPY docker/db-seed/load_sample_data.py /seed/load_sample_data.py
RUN chmod +x /seed/entrypoint.sh \
             /seed/upload_templates.py \
             /seed/upload_images.py \
             /seed/load_sample_data.py

ENTRYPOINT ["/seed/entrypoint.sh"]
