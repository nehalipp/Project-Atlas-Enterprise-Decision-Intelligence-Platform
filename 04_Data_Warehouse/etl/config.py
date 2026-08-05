"""
Project Atlas
ETL Configuration
"""


# ---------------------------------------------------------
# Database Configuration
# ---------------------------------------------------------

DB_CONFIG = {

    "host": "localhost",

    "port": 5432,

    "database": "project_atlas_dw",

    "user": "postgres",

    "password": "postgres"

}



# ---------------------------------------------------------
# ETL Metadata Configuration
# ---------------------------------------------------------

SOURCE_SYSTEM = "Project Atlas"

RAW_SCHEMA = "raw"

STAGING_SCHEMA = "staging"

LOAD_CHUNK_SIZE = 5000