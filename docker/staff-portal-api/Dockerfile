FROM python:3.12.11-alpine3.22

RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers make \
 && apk add --no-cache bash git gettext libpq-dev libmagic

WORKDIR /app

# Copy local package sources (may be empty for remote-only builds)
COPY local_deps/ /app/local_deps/

# Install dependencies from the generated requirements file
COPY adapters.requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apk del --no-network .build-deps

ENV PYTHONUNBUFFERED=1
ENV STAFF_PORTAL_WORKER_TYPE=gunicorn
ENV STAFF_PORTAL_HOST=0.0.0.0
ENV STAFF_PORTAL_PORT=8000
# Default worker count kept low (3) for predictable memory; the Helm chart
# overrides this per-deployment via STAFF_PORTAL_NO_OF_WORKERS in envVars.
ENV STAFF_PORTAL_NO_OF_WORKERS=3

# Run as a non-root user (uid/gid 1001) instead of root. uid/gid match the
# chart's runAsUser/fsGroup so enabling the pod securityContext is consistent.
# The app only needs read access to the root-owned site-packages (world-readable)
# and write access to /app and /tmp — both fine for uid 1001. Binds to port 8000
# (>1024) so no NET_BIND_SERVICE capability is required.
RUN addgroup -g 1001 openg2p \
 && adduser -D -u 1001 -G openg2p -h /home/openg2p openg2p \
 && chown -R 1001:1001 /app
USER 1001
ENV HOME=/home/openg2p

# Use module path for migrate and Gunicorn WSGI app
CMD python3 -m openg2p_registry_staff_portal_api.main migrate; \
    ${STAFF_PORTAL_WORKER_TYPE} "openg2p_registry_staff_portal_api.main:app" --workers ${STAFF_PORTAL_NO_OF_WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind ${STAFF_PORTAL_HOST}:${STAFF_PORTAL_PORT}
