# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Records API."""

from __future__ import absolute_import, print_function

from datetime import datetime

from flask import url_for
from flask_login import current_user
from invenio_records_files.api import Record as FilesRecord
from oarepo_rdm_records.marshmallow import MetadataSchemaV1
from oarepo_records_draft.record import DraftRecordMixin
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin,\
    FilesKeepingRecordMixin
from .constants import ALLOWED_SCHEMAS, PREFERRED_SCHEMA


class Record(SchemaKeepingRecordMixin,
             ReferenceEnabledRecordMixin,
             MarshmallowValidatedRecordMixin,
             FilesRecord):
    """CESNET DEMO record."""
    ALLOWED_SCHEMAS = ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = MetadataSchemaV1

    _schema = "record-v1.0.0.json"

    @property
    def canonical_url(self):
        return url_for('invenio_records_rest.recid',
                       pid_value=self['id'], _external=True)


class DraftRecord(DraftRecordMixin, FilesKeepingRecordMixin):
    """CESNET DEMO draft record class."""
    def validate(self, *args, **kwargs):
        if 'created' not in self:
            self['created'] = datetime.date.today().strftime('%Y-%m-%d')
        if 'creator' not in self:
            if current_user.is_authenticated:
                self['creator'] = current_user.email
            else:
                self['creator'] = 'anonymous'

        self['modified'] = datetime.date.today().strftime('%Y-%m-%d')
        return super().validate(*args, **kwargs)

    @property
    def canonical_url(self):
        return url_for('invenio_records_rest.drecid',
                       pid_value=self['id'], _external=True)

