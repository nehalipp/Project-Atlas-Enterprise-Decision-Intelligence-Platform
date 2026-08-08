"""
==========================================================
Project Atlas

Raw To Staging Transformation Layer

Purpose:
    Clean and transform raw data into trusted staging data.

Flow:

    raw.*
       |
       |
       ↓

    staging.stg_*

Invalid records:
    logs/transform/rejected_records

Key Design Principles:
    1. Business keys and foreign keys preserve NULL values.
    2. Descriptive attributes use "UNKNOWN" for missing values.
    3. Duplicate business keys are removed.
    4. Business-rule violations are rejected and logged.
    5. Staging tables are rebuilt on every pipeline execution.
    6. ETL metadata is added to every staging record.

==========================================================
"""

import os
import uuid
import pandas as pd

from datetime import datetime

from sqlalchemy import text

from etl.database_connection import get_engine


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

REJECTED_PATH = "logs/transform/rejected_records"

os.makedirs(
    REJECTED_PATH,
    exist_ok=True
)


# ---------------------------------------------------------
# Table Mapping
# ---------------------------------------------------------

TABLE_MAPPING = {

    "accounts": "stg_accounts",
    "customers": "stg_customers",
    "products": "stg_products",
    "suppliers": "stg_suppliers",
    "locations": "stg_locations",
    "employees": "stg_employees",
    "machines": "stg_machines",

    "sales_transactions": "stg_sales_transactions",
    "production": "stg_production",
    "maintenance": "stg_maintenance",
    "financial_transactions": "stg_financial_transactions",
    "budget": "stg_budget",
    "energy_consumption": "stg_energy_consumption",
    "emissions": "stg_emissions",
    "waste": "stg_waste",
    "inventory": "stg_inventory"

}


# ---------------------------------------------------------
# Business Keys
# ---------------------------------------------------------

PRIMARY_KEYS = {

    "accounts": "account_id",
    "customers": "customer_id",
    "products": "product_id",
    "suppliers": "supplier_id",
    "locations": "location_id",
    "employees": "employee_id",
    "machines": "machine_id",

    "sales_transactions": "transaction_id",
    "production": "production_id",
    "maintenance": "maintenance_id",
    "financial_transactions": "transaction_id",
    "budget": "budget_id",
    "energy_consumption": "energy_id",
    "emissions": "emission_id",
    "waste": "waste_id",
    "inventory": "inventory_id"

}


# ---------------------------------------------------------
# Foreign Keys
# ---------------------------------------------------------
#
# Missing values in these columns MUST remain NULL.
#
# We do NOT convert missing business/foreign keys to
# "UNKNOWN" because "UNKNOWN" is not a valid business key.
#
# Descriptive attributes may still use "UNKNOWN".
# ---------------------------------------------------------

FOREIGN_KEYS = {

    "sales_transactions": [
        "customer_id",
        "product_id",
        "location_id"
    ],

    "production": [
        "product_id",
        "machine_id"
    ],

    "maintenance": [
        "machine_id"
    ],

    "financial_transactions": [
        "account_id"
    ],

    "energy_consumption": [
        "location_id"
    ],

    "emissions": [
        "location_id"
    ],

    "waste": [
        "location_id"
    ],

    "inventory": [
        "product_id",
        "location_id"
    ]

}


# ---------------------------------------------------------
# Cleaning Functions
# ---------------------------------------------------------

def clean_strings(
        df,
        table
):
    """
    Clean string columns while preserving NULL values
    for business keys and foreign keys.

    Business keys / foreign keys:
        Missing values remain NULL.

    Descriptive attributes:
        Missing values are converted to "UNKNOWN".
    """

    # Primary key for the current table
    primary_key = PRIMARY_KEYS.get(table)

    # Foreign keys for the current table
    foreign_keys = FOREIGN_KEYS.get(
        table,
        []
    )

    # Columns that must preserve NULL
    key_columns = set(
        foreign_keys
    )

    if primary_key:
        key_columns.add(
            primary_key
        )

    # Process string columns
    for col in df.select_dtypes(
        include="object"
    ).columns:

        # Strip whitespace from actual strings
        df[col] = df[col].apply(
            lambda x: x.strip()
            if isinstance(x, str)
            else x
        )

        # Convert blank/string representations of
        # missing values into actual NULL/NaN
        df[col] = df[col].replace(
            [
                "",
                "nan",
                "None",
                "NULL",
                "null"
            ],
            pd.NA
        )

        # Preserve NULL for keys.
        #
        # Only descriptive attributes receive UNKNOWN.
        if col not in key_columns:

            df[col] = df[col].fillna(
                "UNKNOWN"
            )

    return df


# ---------------------------------------------------------
# Duplicate Removal
# ---------------------------------------------------------

def remove_duplicates(
        df,
        table
):
    """
    Remove duplicate business-key records.

    The first occurrence is retained.

    Duplicate records are written to the rejected-record
    directory for auditability.
    """

    key = PRIMARY_KEYS.get(
        table
    )

    if key and key in df.columns:

        duplicate_rows = df[
            df.duplicated(
                subset=[key],
                keep="first"
            )
        ]

        if len(duplicate_rows) > 0:

            duplicate_rows.to_csv(
                f"{REJECTED_PATH}/{table}_duplicates.csv",
                index=False
            )

        df = df.drop_duplicates(
            subset=[key],
            keep="first"
        )

    return df


# ---------------------------------------------------------
# Business Validation
# ---------------------------------------------------------

def validate_records(
        df,
        table
):
    """
    Apply table-specific business rules.

    Invalid records are removed from staging and written
    to the rejected-record directory.
    """

    rejected = pd.DataFrame()

    # -----------------------------------------------------
    # Sales
    # -----------------------------------------------------

    if table == "sales_transactions":

        rejected = df[
            (df["quantity"] <= 0)
            |
            (df["unit_price"] <= 0)
        ]

        df = df.drop(
            rejected.index
        )

    # -----------------------------------------------------
    # Inventory
    # -----------------------------------------------------

    elif table == "inventory":

        rejected = df[
            df["inventory_quantity"] < 0
        ]

        df = df.drop(
            rejected.index
        )

    # -----------------------------------------------------
    # Production
    # -----------------------------------------------------

    elif table == "production":

        rejected = df[
            df["units_produced"] < 0
        ]

        df = df.drop(
            rejected.index
        )

    # -----------------------------------------------------
    # Write rejected records
    # -----------------------------------------------------

    if len(rejected) > 0:

        rejected.to_csv(
            f"{REJECTED_PATH}/{table}_validation_errors.csv",
            index=False
        )

    return df


# ---------------------------------------------------------
# Transform Single Table
# ---------------------------------------------------------

def transform_table(
        raw_table,
        staging_table
):
    """
    Transform one raw table into its staging table.
    """

    engine = get_engine()

    print(
        f"Processing {raw_table}"
    )

    # -----------------------------------------------------
    # Extract from RAW
    # -----------------------------------------------------

    df = pd.read_sql(
        f"SELECT * FROM raw.{raw_table}",
        engine
    )

    original_count = len(
        df
    )

    # -----------------------------------------------------
    # Clean
    # -----------------------------------------------------

    df = clean_strings(
        df,
        raw_table
    )

    # -----------------------------------------------------
    # Remove duplicates
    # -----------------------------------------------------

    df = remove_duplicates(
        df,
        raw_table
    )

    # -----------------------------------------------------
    # Business validation
    # -----------------------------------------------------

    df = validate_records(
        df,
        raw_table
    )

    # -----------------------------------------------------
    # ETL metadata
    # -----------------------------------------------------

    batch_id = str(
        uuid.uuid4()
    )

    df["etl_batch_id"] = (
        batch_id
    )

    df["etl_loaded_timestamp"] = (
        datetime.now()
    )

    df["source_file"] = (
        f"raw.{raw_table}"
    )

    # -----------------------------------------------------
    # Clear previous staging load
    # -----------------------------------------------------
    #
    # This is important because the pipeline is designed
    # as a full-refresh ETL process.
    #
    # Without TRUNCATE, repeated pipeline executions would
    # append duplicate staging records.
    # -----------------------------------------------------

    with engine.begin() as connection:

        connection.execute(
            text(
                f"""
                TRUNCATE TABLE
                staging.{staging_table};
                """
            )
        )

    # -----------------------------------------------------
    # Load STAGING
    # -----------------------------------------------------

    df.to_sql(
        staging_table,
        engine,
        schema="staging",
        if_exists="append",
        index=False,
        method="multi",
        chunksize=5000
    )

    # -----------------------------------------------------
    # Transformation summary
    # -----------------------------------------------------

    rejected_count = (
        original_count
        - len(df)
    )

    print(
        f"""
Completed:
{raw_table}

Original Records: {original_count}
Loaded Records:   {len(df)}
Rejected Records: {rejected_count}

"""
    )


# ---------------------------------------------------------
# Run Transform
# ---------------------------------------------------------

def run_transform():

    print(
        "=" * 60
    )

    print(
        "Starting Transformation"
    )

    print(
        "=" * 60
    )

    for raw_table, staging_table in TABLE_MAPPING.items():

        transform_table(
            raw_table,
            staging_table
        )

    print(
        "=" * 60
    )

    print(
        "Transformation Completed"
    )

    print(
        "=" * 60
    )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    run_transform()