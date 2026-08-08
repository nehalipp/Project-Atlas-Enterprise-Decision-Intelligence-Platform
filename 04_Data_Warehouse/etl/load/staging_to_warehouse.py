"""
==========================================================
Project Atlas
Enterprise Decision Intelligence Platform

Staging → Warehouse Load

Source:
    staging schema

Target:
    warehouse schema

Load order:
    1. Dimensions
    2. Facts

Responsibilities:
    - Load staging data into warehouse dimensions
    - Generate surrogate keys using BIGSERIAL
    - Resolve dimension business keys to surrogate keys
    - Handle UNKNOWN dimension members
    - Normalize source business-key formats during lookup
    - Load warehouse fact tables
    - Support repeatable full warehouse loads

Data cleansing is NOT performed here.
Data cleansing is handled by raw → staging.

==========================================================
"""

from etl.database_connection import get_engine
from sqlalchemy import text


# ==========================================================
# DIMENSIONS
# ==========================================================

DIMENSION_LOADS = [
    {
        "target": "dim_account",
        "source": "stg_accounts",
        "surrogate_key": "account_key",
        "business_key": "account_id",
        "columns": [
            "account_id",
            "account_name",
            "account_type",
            "account_category",
            "department",
            "active_status",
        ],
    },

    {
        "target": "dim_customer",
        "source": "stg_customers",
        "surrogate_key": "customer_key",
        "business_key": "customer_id",
        "columns": [
            "customer_id",
            "customer_name",
            "industry",
            "customer_segment",
            "country",
            "region",
            "customer_since",
        ],
    },

    {
        "target": "dim_product",
        "source": "stg_products",
        "surrogate_key": "product_key",
        "business_key": "product_id",
        "columns": [
            "product_id",
            "product_name",
            "category",
            "unit_cost",
            "unit_price",
            "product_status",
        ],
    },

    {
        "target": "dim_supplier",
        "source": "stg_suppliers",
        "surrogate_key": "supplier_key",
        "business_key": "supplier_id",
        "columns": [
            "supplier_id",
            "supplier_name",
            "supplier_category",
            "country",
            "region",
            "performance_rating",
            "supplier_status",
        ],
    },

    {
        "target": "dim_location",
        "source": "stg_locations",
        "surrogate_key": "location_key",
        "business_key": "location_id",
        "columns": [
            "location_id",
            "facility_name",
            "location_type",
            "city",
            "state",
            "country",
            "region",
            "latitude",
            "longitude",
            "operating_status",
            "opening_date",
        ],
    },

    {
        "target": "dim_employee",
        "source": "stg_employees",
        "surrogate_key": "employee_key",
        "business_key": "employee_id",
        "columns": [
            "employee_id",
            "employee_name",
            "department",
            "job_title",
            "location_id",
            "manager_id",
            "hire_date",
            "salary",
            "employment_status",
            "performance_rating",
        ],
    },

    {
        "target": "dim_machine",
        "source": "stg_machines",
        "surrogate_key": "machine_key",
        "business_key": "machine_id",
        "columns": [
            "machine_id",
            "machine_name",
            "machine_type",
            "manufacturer",
            "location_id",
            "purchase_date",
            "warranty_expiry",
            "expected_life_years",
            "machine_status",
        ],
    },
]


# ==========================================================
# FACTS
# ==========================================================

FACT_LOADS = [

    {
        "target": "fact_sales",
        "source": "stg_sales_transactions",

        "columns": [
            "transaction_id",
            "transaction_date",
            "quantity",
            "unit_price",
            "discount_percentage",
            "revenue",
            "sales_channel",
        ],

        "lookups": [
            {
                "source_key": "customer_id",
                "dimension": "dim_customer",
                "dimension_key": "customer_id",
                "target_key": "customer_key",
                "lookup_expression": (
                    "COALESCE(NULLIF(TRIM(s.customer_id), ''), 'UNKNOWN')"
                ),
            },

            {
                "source_key": "product_id",
                "dimension": "dim_product",
                "dimension_key": "product_id",
                "target_key": "product_key",
                "lookup_expression": (
                    "TRIM(s.product_id)"
                ),
            },

            {
                "source_key": "location_id",
                "dimension": "dim_location",
                "dimension_key": "location_id",
                "target_key": "location_key",
                "lookup_expression": (
                    "CASE "
                    "WHEN s.location_id IS NULL "
                    "     OR TRIM(s.location_id) = '' "
                    "THEN NULL "
                    "ELSE 'LOC_' || LPAD("
                    "REGEXP_REPLACE(TRIM(s.location_id), '^LOC_', ''), "
                    "5, '0') "
                    "END"
                ),
            },
        ],
    },


    {
        "target": "fact_production",
        "source": "stg_production",

        "columns": [
            "production_id",
            "production_date",
            "shift",
            "units_produced",
            "defect_count",
            "defect_rate",
            "production_hours",
            "production_status",
        ],

        "lookups": [
            {
                "source_key": "machine_id",
                "dimension": "dim_machine",
                "dimension_key": "machine_id",
                "target_key": "machine_key",
                "lookup_expression": "TRIM(s.machine_id)",
            },

            {
                "source_key": "product_id",
                "dimension": "dim_product",
                "dimension_key": "product_id",
                "target_key": "product_key",
                "lookup_expression": "TRIM(s.product_id)",
            },

            {
                "source_key": "location_id",
                "dimension": "dim_location",
                "dimension_key": "location_id",
                "target_key": "location_key",
                "lookup_expression": (
                    "CASE "
                    "WHEN s.location_id IS NULL "
                    "     OR TRIM(s.location_id) = '' "
                    "THEN NULL "
                    "ELSE 'LOC_' || LPAD("
                    "REGEXP_REPLACE(TRIM(s.location_id), '^LOC_', ''), "
                    "5, '0') "
                    "END"
                ),
            },
        ],
    },


    {
        "target": "fact_maintenance",
        "source": "stg_maintenance",

        "columns": [
            "maintenance_id",
            "maintenance_date",
            "maintenance_type",
            "technician",
            "downtime_hours",
            "repair_cost",
            "maintenance_status",
        ],

        "lookups": [
            {
                "source_key": "machine_id",
                "dimension": "dim_machine",
                "dimension_key": "machine_id",
                "target_key": "machine_key",
                "lookup_expression": "TRIM(s.machine_id)",
            },
        ],
    },


    {
        "target": "fact_financial_transactions",
        "source": "stg_financial_transactions",

        "columns": [
            "transaction_id",
            "transaction_date",
            "department",
            "transaction_type",
            "amount",
            "currency",
            "vendor",
            "payment_status",
        ],

        "lookups": [
            {
                "source_key": "account_id",
                "dimension": "dim_account",
                "dimension_key": "account_id",
                "target_key": "account_key",
                "lookup_expression": "TRIM(s.account_id)",
            },
        ],
    },


    {
        "target": "fact_budget",
        "source": "stg_budget",

        "columns": [
            "budget_id",
            "fiscal_year",
            "department",
            "account_type",
            "budget_amount",
            "approved_by",
            "budget_status",
        ],

        "lookups": [],
    },


    {
        "target": "fact_energy_consumption",
        "source": "stg_energy_consumption",

        "columns": [
            "energy_id",
            "measurement_date",
            "energy_source",
            "consumption_kwh",
            "energy_cost",
        ],

        "lookups": [
            {
                "source_key": "location_id",
                "dimension": "dim_location",
                "dimension_key": "location_id",
                "target_key": "location_key",
                "lookup_expression": (
                    "CASE "
                    "WHEN s.location_id IS NULL "
                    "     OR TRIM(s.location_id) = '' "
                    "THEN NULL "
                    "ELSE 'LOC_' || LPAD("
                    "REGEXP_REPLACE(TRIM(s.location_id), '^LOC_', ''), "
                    "5, '0') "
                    "END"
                ),
            },
        ],
    },


    {
        "target": "fact_emissions",
        "source": "stg_emissions",

        "columns": [
            "emission_id",
            "measurement_date",
            "emission_type",
            "scope",
            "carbon_emission_tons",
        ],

        "lookups": [
            {
                "source_key": "location_id",
                "dimension": "dim_location",
                "dimension_key": "location_id",
                "target_key": "location_key",
                "lookup_expression": (
                    "CASE "
                    "WHEN s.location_id IS NULL "
                    "     OR TRIM(s.location_id) = '' "
                    "THEN NULL "
                    "ELSE 'LOC_' || LPAD("
                    "REGEXP_REPLACE(TRIM(s.location_id), '^LOC_', ''), "
                    "5, '0') "
                    "END"
                ),
            },
        ],
    },


    {
        "target": "fact_waste",
        "source": "stg_waste",

        "columns": [
            "waste_id",
            "measurement_date",
            "waste_type",
            "quantity_tons",
            "disposal_method",
        ],

        "lookups": [
            {
                "source_key": "location_id",
                "dimension": "dim_location",
                "dimension_key": "location_id",
                "target_key": "location_key",
                "lookup_expression": (
                    "CASE "
                    "WHEN s.location_id IS NULL "
                    "     OR TRIM(s.location_id) = '' "
                    "THEN NULL "
                    "ELSE 'LOC_' || LPAD("
                    "REGEXP_REPLACE(TRIM(s.location_id), '^LOC_', ''), "
                    "5, '0') "
                    "END"
                ),
            },
        ],
    },


    {
        "target": "fact_inventory",
        "source": "stg_inventory",

        "columns": [
            "inventory_id",
            "inventory_date",
            "inventory_quantity",
            "unit_cost",
            "inventory_value",
            "stock_status",
        ],

        "select_columns": [
            "s.inventory_id",
            "s.date",
            "s.inventory_quantity",
            "s.unit_cost",
            "s.inventory_value",
            "s.stock_status",
        ],

        "lookups": [
            {
                "source_key": "product_id",
                "dimension": "dim_product",
                "dimension_key": "product_id",
                "target_key": "product_key",
                "lookup_expression": "TRIM(s.product_id)",
            },

            {
                "source_key": "location_id",
                "dimension": "dim_location",
                "dimension_key": "location_id",
                "target_key": "location_key",
                "lookup_expression": (
                    "CASE "
                    "WHEN s.location_id IS NULL "
                    "     OR TRIM(s.location_id) = '' "
                    "THEN NULL "
                    "ELSE 'LOC_' || LPAD("
                    "REGEXP_REPLACE(TRIM(s.location_id), '^LOC_', ''), "
                    "5, '0') "
                    "END"
                ),
            },
        ],
    },
]


# ==========================================================
# TRUNCATE WAREHOUSE
# ==========================================================

def truncate_warehouse(connection):
    """
    Clear existing warehouse data before a full reload.

    RESTART IDENTITY resets BIGSERIAL surrogate keys.

    CASCADE handles dependencies between fact and
    dimension tables.
    """

    tables = [
        "warehouse.fact_sales",
        "warehouse.fact_production",
        "warehouse.fact_maintenance",
        "warehouse.fact_financial_transactions",
        "warehouse.fact_budget",
        "warehouse.fact_energy_consumption",
        "warehouse.fact_emissions",
        "warehouse.fact_waste",
        "warehouse.fact_inventory",

        "warehouse.dim_account",
        "warehouse.dim_customer",
        "warehouse.dim_product",
        "warehouse.dim_supplier",
        "warehouse.dim_location",
        "warehouse.dim_employee",
        "warehouse.dim_machine",
    ]

    table_list = ", ".join(tables)

    connection.execute(
        text(
            f"""
            TRUNCATE TABLE
                {table_list}
            RESTART IDENTITY
            CASCADE;
            """
        )
    )

    print("Warehouse tables truncated successfully.")


# ==========================================================
# LOAD DIMENSION
# ==========================================================

def load_dimension(connection, config):
    """
    Load one staging table into one warehouse dimension.

    PostgreSQL generates the BIGSERIAL surrogate key.

    The staging business key is preserved in the dimension.
    """

    target = config["target"]
    source = config["source"]
    columns = config["columns"]

    target_columns = ", ".join(columns)

    source_columns = ", ".join(
        f"s.{column}"
        for column in columns
    )

    sql = text(
        f"""
        INSERT INTO warehouse.{target}
            ({target_columns})
        SELECT
            {source_columns}
        FROM staging.{source} s;
        """
    )

    result = connection.execute(sql)

    print(
        f"  {target:<30} {result.rowcount:>10,} rows"
    )


# ==========================================================
# UNKNOWN DIMENSION MEMBERS
# ==========================================================

def ensure_unknown_customer(connection):
    """
    Create the default UNKNOWN customer dimension member.

    NULL or blank customer references from sales are resolved
    to this member during fact loading.
    """

    sql = text(
        """
        INSERT INTO warehouse.dim_customer
        (
            customer_id,
            customer_name,
            industry,
            customer_segment,
            country,
            region,
            customer_since
        )
        SELECT
            'UNKNOWN',
            'Unknown Customer',
            'UNKNOWN',
            'UNKNOWN',
            'UNKNOWN',
            'UNKNOWN',
            NULL
        WHERE NOT EXISTS
        (
            SELECT 1
            FROM warehouse.dim_customer
            WHERE customer_id = 'UNKNOWN'
        );
        """
    )

    result = connection.execute(sql)

    if result.rowcount == 1:
        print(
            "  dim_customer                   UNKNOWN member added"
        )
    else:
        print(
            "  dim_customer                   UNKNOWN member exists"
        )


def ensure_unknown_dimension_members(connection):
    """
    Create required default dimension members.
    """

    print("\n------------------------------------------")
    print("Ensuring Default Dimension Members")
    print("------------------------------------------")

    ensure_unknown_customer(connection)


# ==========================================================
# LOAD ALL DIMENSIONS
# ==========================================================

def load_dimensions(connection):
    """
    Load dimensions before facts.
    """

    print("\n------------------------------------------")
    print("Loading Dimensions")
    print("------------------------------------------")

    for config in DIMENSION_LOADS:
        load_dimension(connection, config)

    ensure_unknown_dimension_members(connection)


# ==========================================================
# LOAD FACT
# ==========================================================

def load_fact(connection, config):
    """
    Load one staging fact into its warehouse fact table.

    Business keys from staging are converted into warehouse
    surrogate keys through LEFT JOINs.

    Lookup expressions allow source business-key normalization
    without modifying the staging data.

    This is especially important for:

        Sales customer NULL
            -> UNKNOWN customer member

        Sales location LOC_0197
            -> dimension location LOC_00197

    LEFT JOIN is intentionally used so source records are
    never silently dropped during warehouse loading.
    """

    target = config["target"]
    source = config["source"]
    columns = config["columns"]
    lookups = config["lookups"]

    # ------------------------------------------------------
    # Target warehouse columns
    # ------------------------------------------------------

    target_columns = list(columns)

    # ------------------------------------------------------
    # Source SELECT columns
    # ------------------------------------------------------

    if "select_columns" in config:

        select_columns = list(
            config["select_columns"]
        )

    else:

        select_columns = [
            f"s.{column}"
            for column in columns
        ]

    # ------------------------------------------------------
    # Dimension surrogate-key lookups
    # ------------------------------------------------------

    joins = []

    for index, lookup in enumerate(lookups):

        dimension = lookup["dimension"]
        dimension_key = lookup["dimension_key"]
        target_key = lookup["target_key"]

        alias = f"d{index}"

        lookup_expression = lookup.get(
            "lookup_expression",
            f"s.{lookup['source_key']}"
        )

        target_columns.append(
            target_key
        )

        select_columns.append(
            f"{alias}.{target_key}"
        )

        joins.append(
            f"""
            LEFT JOIN warehouse.{dimension} {alias}
                ON {lookup_expression} = {alias}.{dimension_key}
            """
        )

    # ------------------------------------------------------
    # Build SQL
    # ------------------------------------------------------

    target_sql = ", ".join(
        target_columns
    )

    select_sql = ", ".join(
        select_columns
    )

    joins_sql = "\n".join(
        joins
    )

    sql = text(
        f"""
        INSERT INTO warehouse.{target}
        (
            {target_sql}
        )

        SELECT
            {select_sql}

        FROM staging.{source} s

        {joins_sql};
        """
    )

    result = connection.execute(sql)

    print(
        f"  {target:<30} {result.rowcount:>10,} rows"
    )


# ==========================================================
# LOAD ALL FACTS
# ==========================================================

def load_facts(connection):
    """
    Load all facts after dimensions are available.
    """

    print("\n------------------------------------------")
    print("Loading Facts")
    print("------------------------------------------")

    for config in FACT_LOADS:

        load_fact(
            connection,
            config
        )


# ==========================================================
# MAIN
# ==========================================================

def run_warehouse_load():
    """
    Execute complete staging → warehouse load.

    The entire warehouse load executes inside one database
    transaction.

    If any dimension or fact load fails, the transaction
    rolls back.
    """

    engine = get_engine()

    print("\n==========================================")
    print("Project Atlas")
    print("Staging → Warehouse Load")
    print("==========================================")

    try:

        with engine.begin() as connection:

            print(
                "\nStep 1: Clearing warehouse..."
            )

            truncate_warehouse(
                connection
            )

            print(
                "\nStep 2: Loading dimensions..."
            )

            load_dimensions(
                connection
            )

            print(
                "\nStep 3: Loading facts..."
            )

            load_facts(
                connection
            )

        print(
            "\n=========================================="
        )

        print(
            "Warehouse Load Completed Successfully"
        )

        print(
            "=========================================="
        )

    except Exception as error:

        print(
            "\n=========================================="
        )

        print(
            "Warehouse Load Failed"
        )

        print(
            "=========================================="
        )

        print(
            f"Error: {error}"
        )

        raise


# ==========================================================
# SCRIPT ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    run_warehouse_load()