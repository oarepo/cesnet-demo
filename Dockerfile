# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
#
# Dockerfile that builds a fully functional image of your app.
FROM oarepo/oarepo-base:latest

COPY ./docker/overlay /
COPY ./ ./

# Ensure correct permissions on copied files
USER root

WORKDIR ./3rdparty
RUN git clone https://github.com/CESNET/invenio-cesnet-proxyidp.git
WORKDIR ../
RUN cat /etc/requirements.d/*.in
RUN cat /etc/requirements.d/*.in | pip-compile -U -o .requirements.txt -
RUN cat .requirements.txt
RUN pip install -r .requirements.txt
RUN chown -R invenio ./
RUN chmod -R +x /usr/bin/entrypoint
USER invenio
