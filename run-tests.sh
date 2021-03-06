#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

pydocstyle cesnet_demo tests docs && \
isort -rc -c -df && \
check-manifest --ignore ".travis-*" && \
python setup.py test
