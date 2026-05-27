FROM python:3.12.11-alpine3.22

# build-deps: compilers for psycopg2 (libpq) + any sdist builds.
# runtime libs: libpq (psycopg2); jpeg/zlib/freetype for Pillow; cairo for cairosvg (SVG card → PDF).
RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers make libffi-dev \
 && apk add --no-cache bash git gettext libpq-dev libmagic jpeg-dev zlib-dev freetype-dev cairo

WORKDIR /app

# Copy local package sources (nsr-extension provides openg2p_registry_extensions)
COPY local_deps/ /app/local_deps/

# Install dependencies from the generated requirements file
COPY adapters.requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apk del --no-network .build-deps

ENV PYTHONUNBUFFERED=1
ENV AGENT_PORTAL_WORKER_TYPE=gunicorn
ENV AGENT_PORTAL_HOST=0.0.0.0
ENV AGENT_PORTAL_PORT=8000
ENV AGENT_PORTAL_NO_OF_WORKERS=4

# Phase-1 VC issuance backend. Owns no schema (reads beneficiary_vc_view), so
# no `migrate` step — just serve the Gunicorn/Uvicorn app.
CMD ${AGENT_PORTAL_WORKER_TYPE} "openg2p_registry_agent_portal_api.main:app" --workers ${AGENT_PORTAL_NO_OF_WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind ${AGENT_PORTAL_HOST}:${AGENT_PORTAL_PORT}
