# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import GenFunction, \
    PersistentIdentifier
from marshmallow import fields, missing


def files_from_context(_, context):
    """Get the record's files from context."""
    record = (context or {}).get('record', {})
    return record.get('_files', missing)


class MetadataSchemaV1(StrictKeysMixin):
    """Schema for the record metadata."""


class RecordSchemaV1(StrictKeysMixin):
    """Record schema."""

    metadata = fields.Nested(MetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
    files = GenFunction(
        serialize=files_from_context, deserialize=files_from_context)
