# CESNET OA Repository Demo Site
[![Build Status](https://img.shields.io/travis/oarepo/cesnet-demo.svg)](https://travis-ci.org/oarepo/cesnet-demo)
[![image](https://img.shields.io/coveralls/oarepo/cesnet-demo.svg)](https://coveralls.io/r/CESNET/cesnet-demo)
[![image](https://img.shields.io/github/license/oarepo/cesnet-demo.svg)](https://github.com/oarepo/cesnet-demo/blob/master/LICENSE)

CESNET Demo Repository API containing a collection of ACL-enabled
records conforming to the DCObject metadata schema. Docker deployment
is based on the [OARepo base](https://github.com/oarepo/oarepo-base) docker image.

### Environment variables

This deployment inherits environment variables that are provided by the
[OARepo base](https://github.com/oarepo/oarepo-base) image. See
[.env-example](https://github.com/oarepo/oarepo-base/blob/master/.env-example) for further reference:

- ``OAREPO_VERSION=3.2.1``
- ``OAREPO_ES_VERSION=es7``
- ``WORKING_DIR=/opt/invenio``
- ``INVENIO_INSTANCE_PATH=/opt/invenio/var/instance``
- ``INVENIO_USER_ID=1000``
- ``INVENIO_APP_ALLOWED_HOSTS``
- ``INVENIO_APP_ENABLE_SECURE_HEADERS``
- ``INVENIO_SERVER_NAME``
- ``OAREPO_ADMIN_PASSWORD``
- ``OAREPO_ADMIN_USER``
- ``INVENIO_SEARCH_ELASTIC_HOSTS``
- ``INVENIO_JSONSCHEMAS_HOST``
- ``INVENIO_SQLALCHEMY_DATABASE_URI``
- ``INVENIO_BROKER_URL``
- ``INVENIO_CELERY_BROKER_URL``
- ``INVENIO_CELERY_RESULT_BACKEND``
- ``INVENIO_CACHE_TYPE``
- ``INVENIO_CACHE_REDIS_URL``
- ``INVENIO_ACCOUNTS_SESSION_REDIS_URL``
- ``INVENIO_RATELIMIT_STORAGE_URL``
- ``INVENIOSEARCH_INDEX_PREFIX``
- ``INVENIO_JSONSCHEMAS_RESOLVER_CLS``
- ``PROXYIDP_URL``
- ``PROXYIDP_KEY``
- ``PROXYIDP_SECRET``
- ``PROXYIDP_AUTHORIZE_URL``
- ``INVENIO_APPLICATION_ROOT``

To use them in the `docker-compose` files, feel free to copy over and modify the `.env-example` to the `.env` file.
Any additional environment variables that are supported by Invenio can be added to your environment.

## Usage

### Build

To build the CESNET demo docker images, run the following command from the project root:

```
./docker/build-images.sh
```

### Deployment

To deploy the CESNET demo instance for a first time on your existing infrastructure, run the
image with the `deploy` command within a correct environment:

```
docker run oarepo-cesnet-demo deploy
```

This will prepare the database tables, initialize ElasticSearch indices and
message queues and run all another deployment scripts.

### Quickstart

To quickly try things out in a local environment the following compose files are prepared:

```
docker-compose -f docker-compose.deploy.yml up --abort-on-container-exit
```
Runs the basic Invenio infrastracture and executes all the deployment scripts on it.

```
docker-compose -f docker-compose.yml up -d
```
After CESNET demo is deployed, you can use this to run the instance with just a minimal set of services (you
will need to have the reverse proxy set up externally in order to access the API).

```
docker-compose -f docker-compose.full.yml up -d
```
Spins up a full production-like infrastructure for CESNET demo.

### Test

After the instance is deployed and running, you should be able to verify its healthiness by going to the following address:
```
curl -k https://localhost/.well-known/heartbeat/liveliness                                                                                                                                                                      master  33s ⬡
{"status": true, "checks": {"database": {"time": 0.008396387100219727, "status": true}, "redis": {"time": 0.0006849765777587891, "status": true}, "elasticsearch": {"time": 0.008124113082885742, "status": true}}}%
```

## License

Copyright (C) 2020 CESNET.

OARepo Docker is free software; you can redistribute it and/or modify it
under the terms of the MIT License; see LICENSE file for more details.


Further documentation is available on:
https://oarepo-cesnet-demo.readthedocs.io/
