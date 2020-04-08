# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_explicit_acls.marshmallow import ACLRecordSchemaMixinV1, SchemaEnforcingMixin
from invenio_oarepo_dc.marshmallow import DCObjectSchemaV1Mixin
from invenio_oarepo_invenio_model.marshmallow import InvenioRecordSchemaV1Mixin
from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import GenFunction, \
    PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, missing

from cesnet_demo.records.config import ACL_OBJECT_ALLOWED_SCHEMAS, ACL_OBJECT_PREFERRED_SCHEMA


def files_from_context(_, context):
    """Get the record's files from context."""
    record = (context or {}).get('record', {})
    return record.get('_files', missing)


class MetadataSchemaV1(SchemaEnforcingMixin,
                       InvenioRecordSchemaV1Mixin,
                       DCObjectSchemaV1Mixin,
                       StrictKeysMixin):
    """Schema for the record metadata."""
    ALLOWED_SCHEMAS = [*ACL_OBJECT_ALLOWED_SCHEMAS]
    PREFERRED_SCHEMA = ACL_OBJECT_PREFERRED_SCHEMA


class RecordSchemaV1(StrictKeysMixin, ACLRecordSchemaMixinV1):
    """Record schema."""

    metadata = fields.Nested(MetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
    files = GenFunction(
        serialize=files_from_context, deserialize=files_from_context)
