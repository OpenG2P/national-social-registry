FROM python:3.12.11-alpine3.22

RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers make \
 && apk add --no-cache bash git gettext libpq-dev libffi-dev openssl-dev

WORKDIR /app

# Copy local package sources (may be empty for remote-only builds)
COPY local_deps/ /app/local_deps/

# Install dependencies from the generated requirements file
COPY adapters.requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apk del --no-network .build-deps

ENV PYTHONUNBUFFERED=1
ENV CELERY_APP=openg2p_registry_celery_workers.main.celery_app
ENV CELERY_OPTS="worker --loglevel=info"
ENV CELERY_IMPORTS=""

COPY celery/run_celery.py /app/run_celery.py

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
