..
    Copyright (C) 2020 CESNET.

    CESNET OA Repository Demo is free software; you can redistribute it
    and/or modify it under the terms of the MIT License; see LICENSE file for
    more details.

Installation
============

Start all dependent services using docker-compose (this will start PostgreSQL,
Elasticsearch 7, RabbitMQ and Redis):

.. code-block:: console

    $ docker-compose up -d

.. note::

    Make sure you have `enough virtual memory
    <https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode>`_
    for Elasticsearch in Docker:

    .. code-block:: shell

        # Linux
        $ sysctl -w vm.max_map_count=262144

        # macOS
        $ screen ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
        <enter>
        linut00001:~# sysctl -w vm.max_map_count=262144

# FIXME: change following section to deploy compose script
Next, bootstrap the instance (this will install all Python dependencies and
build all static assets):

.. code-block:: console

    $ ./scripts/bootstrap

Next, create database tables, search indexes and message queues:

.. code-block:: console

    $ ./scripts/setup

Running
-------
Start the webserver and the celery worker:

# FIXME: change following section to deploy run script

.. code-block:: console

    $ ./scripts/server

Start a Python shell:

.. code-block:: console

    $ ./scripts/console

Testing
-------
Run the test suite via the provided script:

.. code-block:: console

    $ ./run-tests.sh

By default, end-to-end tests are skipped. You can include the E2E tests like
this:

.. code-block:: console

    $ env E2E=yes ./run-tests.sh

For more information about end-to-end testing see `pytest-invenio
<https://pytest-invenio.readthedocs.io/en/latest/usage.html#running-e2e-tests>`_

Production environment
----------------------
You can use simulate a full production environment using the
``docker-compose.full.yml``. You can start it like this:

.. code-block:: console

    $ ./docker/build-images.sh
    $ docker-compose -f docker-compose.full.yml up -d
    $ ./docker/wait-for-services.sh --full

Remember to create database tables, search indexes and message queues if not
already done:

#FIXME: change to deploy compose script

.. code-block:: console

    $ docker-compose -f docker-compose.full.yml run --rm web-ui ./scripts/setup

In addition to the normal ``docker-compose.yml``, this one will start:

- HAProxy (load balancer) -- https://127.0.0.1 and http://127.0.0.1:8080
- Nginx (web frontend)
- UWSGI (application container)
- Celery (background task worker)
- Flower (Celery monitoring) -- http://127.0.0.1:5555
- Kibana (Elasticsearch inspection) -- http://127.0.0.1:5601
- RabbitMQ (message queue) -- http://guest:guest@127.0.0.1:15672
