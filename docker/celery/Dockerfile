FROM python:3.12.11-alpine3.22

# Git refs for the OpenG2P packages this image installs. Defaults track the
# moving `develop` branches. In CI the central pipeline (openg2p-packaging @v1)
# resolves each of these to a commit SHA BEFORE the build, passes it as the
# build-arg, and records it as an `org.openg2p.pin.<arg>` OCI image label — so a
# built image is traceable to the exact source commits and is reproducible.
# Locally you can pin explicitly, e.g. --build-arg REGISTRY_PLATFORM_REF=<sha>.
ARG REGISTRY_PLATFORM_REF=develop
ARG FASTAPI_COMMON_REF=develop
ARG IAM_CORE_REF=develop

RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers make \
 && apk add --no-cache bash git gettext libpq-dev libffi-dev openssl-dev

WORKDIR /app

# NSR extension — this repo's working tree (build context = repo root).
COPY nsr-extension/ /app/nsr-extension/

# Both celery components (workers + beat producers) are installed so the single
# image can run as worker or beat, selected at runtime via CELERY_APP.
RUN pip install --no-cache-dir \
      "git+https://github.com/openg2p/openg2p-fastapi-common@${FASTAPI_COMMON_REF}#subdirectory=openg2p-fastapi-common" \
      "git+https://github.com/openg2p/openg2p-fastapi-common@${FASTAPI_COMMON_REF}#subdirectory=openg2p-fastapi-auth" \
      "git+https://github.com/openg2p/iam-service@${IAM_CORE_REF}#subdirectory=iam-core" \
      "git+https://github.com/openg2p/registry-platform@${REGISTRY_PLATFORM_REF}#subdirectory=core/openg2p-registry-core" \
      "git+https://github.com/openg2p/registry-platform@${REGISTRY_PLATFORM_REF}#subdirectory=celery/openg2p-registry-celery-beat-producers" \
      "git+https://github.com/openg2p/registry-platform@${REGISTRY_PLATFORM_REF}#subdirectory=celery/openg2p-registry-celery-workers" \
      /app/nsr-extension \
 && apk del --no-network .build-deps

ENV PYTHONUNBUFFERED=1
ENV CELERY_APP=openg2p_registry_celery_workers.main.celery_app
ENV CELERY_OPTS="worker --loglevel=info"
ENV CELERY_IMPORTS=""

# Build context = repo root.
COPY docker/celery/run_celery.py /app/run_celery.py

# Run as a non-root user (uid/gid 1001) instead of root. uid/gid match the
# chart's runAsUser/fsGroup so enabling the pod securityContext is consistent.
# The app reads root-owned site-packages (world-readable) and writes only to
# /app and /tmp (celery-beat's schedule db lives at /tmp/...), both fine for
# uid 1001. Placed AFTER the run_celery.py copy so that file is owned by 1001.
RUN addgroup -g 1001 openg2p \
 && adduser -D -u 1001 -G openg2p -h /home/openg2p openg2p \
 && chown -R 1001:1001 /app
USER 1001
ENV HOME=/home/openg2p

# Always use the python wrapper to handle imports and startup
CMD ["python3", "/app/run_celery.py"]
