#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

INVENIO_VERSION=${OAREPO_VERSION:-"3.3.0"}
ES_VERSION=${OAREPO_ES_VERSION:-"es7"}
OAREPO_TAG=${INVENIO_VERSION}-${ES_VERSION}

docker-compose -f docker-compose.full.yml build
