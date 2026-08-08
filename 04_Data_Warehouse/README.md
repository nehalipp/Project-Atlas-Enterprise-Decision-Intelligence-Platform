# Project Atlas — Data Warehouse & ETL

## Overview

This directory contains the **Data Warehouse and ETL layer** of Project Atlas: Enterprise Decision Intelligence Platform.

The purpose of this layer is to transform generated source data into a trusted, analytics-ready PostgreSQL data warehouse.

The implementation follows a layered ETL architecture:

```text
CSV Source Data
      │
      ▼
     RAW
      │
      ▼
   STAGING
      │
      ▼
  WAREHOUSE
      │
      ▼
 BI / Analytics
```

This directory is intentionally focused on data ingestion, transformation, warehouse loading, validation, metadata, and dimensional modeling.

For the complete Project Atlas architecture and all project components, see the repository-level `README.md`.

---

# Architecture

The Data Warehouse consists of three database layers.

## 1. Raw Layer

Schema:

```text
raw
```

Purpose:

* Ingest source CSV data
* Preserve source-level records
* Provide a reproducible ingestion layer
* Support traceability and debugging

Raw data is not intended to be directly consumed by BI users.

---

## 2. Staging Layer

Schema:

```text
staging
```

Purpose:

* Clean raw data
* Normalize string values
* Remove duplicate business keys
* Apply business validations
* Reject invalid records
* Add ETL metadata

Staging represents the trusted, transformed dataset used by the warehouse load.

---

## 3. Warehouse Layer

Schema:

```text
warehouse
```

Purpose:

* Store analytics-ready dimensional data
* Implement star-schema relationships
* Resolve surrogate keys
* Support BI reporting and analytical queries

The warehouse contains:

* 7 dimensions
* 9 fact tables
* 16 total warehouse tables

---

# Warehouse Model

## Dimensions

```text
dim_account
dim_customer
dim_employee
dim_location
dim_machine
dim_product
dim_supplier
```

## Facts

```text
fact_budget
fact_emissions
fact_energy_consumption
fact_financial_transactions
fact_inventory
fact_maintenance
fact_production
fact_sales
fact_waste
```

See:

```text
diagrams/star_schema.md
```

for the dimensional model and table relationships.

---

# ETL Pipeline

The complete pipeline is:

```text
1. Extract CSV files
        ↓
2. Load raw tables
        ↓
3. Transform raw → staging
        ↓
4. Validate staging data
        ↓
5. Truncate warehouse tables
        ↓
6. Load dimensions
        ↓
7. Resolve surrogate keys
        ↓
8. Load facts
        ↓
9. Run warehouse/data-quality validations
```

The primary orchestration script is:

```text
etl/run_pipeline.py
```

Run the complete pipeline from:

```text
04_Data_Warehouse_NEW/
```

using:

```bash
python3 -m etl.run_pipeline
```

---

# ETL Components

## Extract

Location:

```text
etl/extract/
```

Primary script:

```text
extract_csv_to_raw.py
```

Source configuration:

```text
etl/extract/config/source_config.py
```

The extraction process:

1. Reads the configured CSV.
2. Validates that the file exists.
3. Extracts the records using Pandas.
4. Truncates the corresponding raw table.
5. Loads the new dataset into PostgreSQL.

---

# Transform

Location:

```text
etl/transform/
```

Primary script:

```text
raw_to_staging.py
```

Transformation responsibilities include:

### String cleaning

Leading and trailing whitespace is removed from string fields.

### Null normalization

Blank and missing string values are normalized to:

```text
UNKNOWN
```

### Duplicate removal

Duplicate business keys are identified and removed.

Rejected duplicate records are stored under:

```text
logs/transform/rejected_records/
```

### Business validation

Domain-specific rules are applied before records enter staging.

Examples include:

* Negative quantities
* Invalid prices
* Invalid production quantities
* Negative inventory quantities

Invalid records are written to the rejected-record logs.

### ETL metadata

Staging records receive:

```text
etl_batch_id
etl_loaded_timestamp
source_file
```

---

# Warehouse Load

Location:

```text
etl/load/
```

Primary script:

```text
staging_to_warehouse.py
```

The warehouse loader:

1. Clears the existing warehouse load.
2. Loads all dimensions.
3. Resolves business keys to surrogate keys.
4. Loads all fact tables.
5. Reports inserted row counts.

The load order is important because facts depend on dimension surrogate keys.

---

# Surrogate Keys

Warehouse dimensions use generated surrogate keys.

For example:

```text
dim_customer.customer_key
dim_product.product_key
dim_location.location_key
dim_machine.machine_key
dim_account.account_key
```

Facts reference these surrogate keys.

Example:

```text
staging.stg_sales_transactions
            │
            │ customer_id
            ▼
warehouse.dim_customer
            │
            │ customer_key
            ▼
warehouse.fact_sales
```

---

# Data Quality Validation

Validation scripts are located under:

```text
sql/validation/
```

The validation framework covers:

* Row counts
* Duplicate records
* Referential integrity
* Business rules
* Pipeline-level validation

The primary validation orchestrator is:

```text
pipeline_validation.sql
```

---

# Row Count Validation

The row-count validation compares:

```text
raw
staging
warehouse
```

for all 16 datasets.

Expected behavior:

```text
staging_count <= raw_count
```

because transformation may remove duplicates or invalid records.

For a successful warehouse load:

```text
warehouse_count = staging_count
```

---

# Duplicate Validation

Duplicate validation checks business-key uniqueness within staging and warehouse data.

Examples:

```text
customer_id
product_id
transaction_id
production_id
inventory_id
```

---

# Referential Integrity Validation

Fact tables are checked to ensure that dimensional foreign-key relationships resolve correctly.

Examples:

```text
fact_sales.customer_key
        ↓
dim_customer.customer_key
```

```text
fact_sales.product_key
        ↓
dim_product.product_key
```

```text
fact_sales.location_key
        ↓
dim_location.location_key
```

---

# Business Rule Validation

Business rules verify that warehouse-ready data does not contain known invalid values.

Examples include:

* Missing business keys
* Negative quantities
* Negative monetary values
* Invalid prices
* Invalid operational measurements

---

# Validation Output

The validation framework returns structured results containing:

```text
validation_type
table_name / rule_name
record counts
status
```

Status values:

```text
PASS
FAIL
```

This makes the output suitable for:

* Manual QA
* ETL troubleshooting
* Portfolio demonstration
* Future automated monitoring

---

# Rejected Records

Records rejected during transformation are stored in:

```text
logs/transform/rejected_records/
```

Typical files include:

```text
customers_duplicates.csv
sales_transactions_validation_errors.csv
production_validation_errors.csv
```

These files provide visibility into why source records did not reach staging.

---

# Directory Structure

```text
04_Data_Warehouse_NEW/
│
├── config/
│
├── database/
│   ├── staging/
│   └── warehouse/
│
├── diagrams/
│   └── star_schema.md
│
├── etl/
│   ├── extract/
│   │   ├── config/
│   │   │   └── source_config.py
│   │   └── extract_csv_to_raw.py
│   │
│   ├── transform/
│   │   └── raw_to_staging.py
│   │
│   ├── load/
│   │   └── staging_to_warehouse.py
│   │
│   ├── database_connection.py
│   └── run_pipeline.py
│
├── logs/
│   └── transform/
│       └── rejected_records/
│
├── metadata/
│   ├── data_dictionary.md
│   └── table_mapping.md
│
├── sql/
│   └── validation/
│       ├── pipeline_validation.sql
│       ├── row_count_validation.sql
│       ├── duplicate_validation.sql
│       ├── referential_integrity_validation.sql
│       └── business_rule_validation.sql
│
├── README.md
└── requirements.txt
```

---

# Database Schemas

The PostgreSQL database contains:

```text
raw
staging
warehouse
```

The warehouse database is:

```text
project_atlas_dw
```

---

# Current Warehouse Scale

The generated dataset is intentionally large enough to demonstrate realistic ETL behavior.

Representative volumes include:

| Dataset                | Raw Records | Staging Records |
| ---------------------- | ----------: | --------------: |
| Accounts               |         500 |             500 |
| Customers              |      51,000 |          50,000 |
| Products               |       5,000 |           5,000 |
| Suppliers              |       1,000 |           1,000 |
| Locations              |         255 |             250 |
| Employees              |      10,000 |          10,000 |
| Machines               |       1,500 |           1,500 |
| Sales                  |     510,000 |         497,500 |
| Production             |     306,000 |         300,000 |
| Maintenance            |     100,000 |         100,000 |
| Financial Transactions |     510,000 |         500,000 |
| Budget                 |       5,000 |           5,000 |
| Energy Consumption     |     150,000 |         150,000 |
| Emissions              |     150,000 |         150,000 |
| Waste                  |     100,000 |         100,000 |
| Inventory              |     250,000 |         250,000 |

The difference between raw and staging counts is intentional and represents duplicate/invalid records removed during transformation.

---

# Technology Stack

| Technology | Purpose                                |
| ---------- | -------------------------------------- |
| Python     | ETL orchestration and transformation   |
| Pandas     | CSV processing and data transformation |
| PostgreSQL | Raw, staging, and warehouse database   |
| SQLAlchemy | Python/PostgreSQL connectivity         |
| psycopg2   | PostgreSQL driver                      |
| SQL        | Warehouse creation and validation      |
| Git        | Version control                        |

---

# Operational Design

The pipeline is designed as a **full-refresh ETL process**.

Each execution:

1. Refreshes the raw layer from source CSV files.
2. Rebuilds the staging load.
3. Truncates warehouse tables.
4. Reloads dimensions.
5. Reloads facts.
6. Runs validation checks.

Therefore, repeated pipeline executions should **not accumulate duplicate warehouse records**.

The expected behavior is:

```text
Run 1
Warehouse = current staging dataset

Run 2
Warehouse = current staging dataset

Run 3
Warehouse = current staging dataset
```

rather than:

```text
Run 1 → 1x data
Run 2 → 2x data
Run 3 → 3x data
```

---

# Documentation

Additional technical documentation:

```text
diagrams/star_schema.md
metadata/data_dictionary.md
metadata/table_mapping.md
```

Validation documentation and SQL:

```text
sql/validation/
```

---

# Project-Level Documentation

This README documents only the **Data Warehouse / ETL component** of Project Atlas.

For the complete project, including:

* Data generation
* Data quality
* Analytics
* BI dashboards
* Business intelligence use cases
* Architecture
* Project objectives

refer to the repository-level:

```text
README.md
```

---

# Status

The Data Warehouse layer currently implements:

* CSV ingestion
* Raw layer
* Staging layer
* Data cleaning
* Duplicate handling
* Business validation
* Rejected-record logging
* Dimension loading
* Fact loading
* Surrogate key resolution
* Row-count validation
* Duplicate validation
* Referential integrity validation
* Business rule validation
* End-to-end ETL orchestration
* ETL documentation and metadata
