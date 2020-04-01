FROM python:3.7.4-alpine3.10

LABEL \
    maintainer="Mikhail Rubtcov <5494567@gmail.com>"

WORKDIR /app

COPY Pipfile* ./

RUN set -ex \
    && pip install -U \
        pip \
        pipenv \
    && apk add --no-cache -t build-deps \
        alpine-sdk \
        linux-headers \
        postgresql-dev \
    && apk add --no-cache \
        zlib-dev \
        postgresql-libs \
    && pipenv install --system --deploy \
    && apk del build-deps

COPY . .

WORKDIR /app/src

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]