# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_indexer.api import RecordIndexer
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all, check_elasticsearch
from invenio_search import RecordsSearch

from cesnet_demo.records.record import Record, DraftRecord


def _(x):
    """Identity function for string extraction."""
    return x


ACL_OBJECT_ALLOWED_SCHEMAS = ('record-v1.0.0.json',)
ACL_OBJECT_PREFERRED_SCHEMA = 'record-v1.0.0.json'

RECORDS_DRAFT_ENDPOINTS = {
    'recid': dict(
        draft='drecid',
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        default_endpoint_prefix=True,
        record_class=Record,
        search_class=RecordsSearch,
        indexer_class=RecordIndexer,
        search_index='records',
        search_type=None,
        record_serializers={
            'application/json': 'oarepo_validate:json_response',
        },
        search_serializers={
            'application/json': 'oarepo_validate:json_search',
        },
        record_loaders={
            'application/json': 'oarepo_validate:json_loader',
        },
        list_route='/records/',
        item_route='/records/<pid(recid,'
                   'record_class="cesnet_demo.records.record.Record")'
                   ':pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),

    ),
    'drecid': dict(
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=allow_all,
        update_permission_factory_imp=allow_all,
        delete_permission_factory_imp=allow_all,
        list_permission_factory_imp=allow_all,
        record_class='cesnet_demo.records.record.DraftRecord',
        files=dict(
            put_file_factory=allow_all,
            get_file_factory=allow_all,
            delete_file_factory=allow_all,
        )
    )
}
"""REST API for cesnet-demo."""

PIDSTORE_RECID_FIELD = 'id'

OAREPO_DEMO_ENDPOINTS_ENABLED = True
"""Enable/disable automatic endpoint registration."""

RECORDS_REST_FACETS = dict(
    records=dict(
        aggs=dict(
            type=dict(terms=dict(field='type')),
            keywords=dict(terms=dict(field='keywords'))
        ),
        post_filters=dict(
            type=terms_filter('type'),
            keywords=terms_filter('keywords'),
        )
    )
)
"""Introduce searching facets."""

RECORDS_REST_SORT_OPTIONS = dict(
    records=dict(
        bestmatch=dict(
            title=_('Best match'),
            fields=['_score'],
            default_order='desc',
            order=1,
        ),
    )
)
"""Setup sorting options."""

RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(
        query='bestmatch',
        noquery='mostrecent',
    )
)
"""Set default sorting options."""

FILES_REST_PERMISSION_FACTORY = \
    'cesnet_demo.records.permissions:files_permission_factory'
"""Files-REST permissions factory."""

FILES_REST_STORAGE_FACTORY = 'oarepo_s3.storage.s3_storage_factory'
