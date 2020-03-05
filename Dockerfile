# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
#
# Dockerfile that builds a fully functional image of your app.

ARG OAREPO_TAG
FROM oarepo/oarepo-base:3.2.1-es7

COPY ./docker/overlay /

RUN cat /etc/requirements.d/*.in | pip-compile -U -o .requirements.txt -
RUN pip install -r .requirements.txt
