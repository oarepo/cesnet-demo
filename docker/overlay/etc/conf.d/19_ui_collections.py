
# OARepo UI collections API configuration.
# =======================================
INVENIO_OAREPO_UI_COLLECTIONS = {
    "records": {
        "title": {
            "cs-cz": "Ukázkové záznamy v repozitáři",
            "en-us": "Demo Repository Records"
        },
        "description": {
            "cs-cz": """
                Kolekce ukázkových záznamů odpovídajících DCObject metadatovému schematu.
                """,
            "en-us": """
                A collection of a Demo Records that adhere to the DCObject metadata schema.
                """
        },
        "rest": "/api/records/",
        "facet_filters": list(FILTERS.keys())
    }
}
