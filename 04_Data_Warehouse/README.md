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

This component is responsible for:

* Source data ingestion
* Raw data persistence
* Data cleaning and transformation
* Duplicate detection and removal
* Business-rule validation
* Rejected-record logging
* Dimensional modeling
* Surrogate-key resolution
* Fact-table loading
* Data-quality validation
* ETL execution logging
* End-to-end pipeline orchestration

For the complete Project Atlas architecture and project documentation, see the repository-level `README.md`.

---

# Architecture

The Data Warehouse consists of three primary database layers:

```text
raw
  │
  ▼
staging
  │
  ▼
warehouse
```

Each layer has a distinct responsibility.

---

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
* Maintain the original source record volume before transformation

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
* Preserve missing business and foreign keys as `NULL`
* Remove duplicate business keys
* Apply business-rule validation
* Reject invalid records
* Add ETL metadata

The staging layer represents the trusted, transformed dataset used by the warehouse loading process.

### Null-handling strategy

Business keys and foreign keys are handled differently from descriptive attributes.

Business and foreign keys preserve missing values as:

```text
NULL
```

Descriptive attributes with missing values are normalized to:

```text
UNKNOWN
```

This prevents invalid values such as:

```text
UNKNOWN
```

from being incorrectly treated as actual business-key identifiers.

---

## 3. Warehouse Layer

Schema:

```text
warehouse
```

Purpose:

* Store analytics-ready dimensional data
* Implement a star-schema architecture
* Generate surrogate keys
* Resolve business keys to surrogate keys
* Load fact tables
* Support BI reporting and analytical queries

The warehouse contains:

* 7 dimension tables
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

The dimensional model is documented in:

```text
diagrams/star_schema.md
```

---

# ETL Architecture

The ETL process is divided into three independent layers:

```text
             ┌──────────────────┐
             │  Source CSV Data │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │     EXTRACT      │
             │   CSV → RAW      │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │    TRANSFORM     │
             │ RAW → STAGING    │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │       LOAD       │
             │ STAGING → DW     │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │    VALIDATION    │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │   BI / ANALYTICS │
             └──────────────────┘
```

Each ETL layer can be executed independently.

The complete pipeline can also be executed through:

```text
etl/run_pipeline.py
```

---

# ETL Execution

## Run Complete Pipeline

From the `04_Data_Warehouse` directory:

```bash
python3 -m etl.run_pipeline
```

The complete process executes:

```text
Extract
   ↓
Transform
   ↓
Load
   ↓
Validation
```

---

# Extract Layer

Location:

```text
etl/extract/
```

Primary components:

```text
extract_csv_to_raw.py
run_extract.py
config/source_config.py
```

## Responsibilities

The extract layer:

1. Reads configured CSV source files.
2. Validates that source files exist.
3. Loads source data using Pandas.
4. Truncates the corresponding raw table.
5. Loads the source dataset into PostgreSQL.
6. Records extraction activity.

Source configuration is maintained in:

```text
etl/extract/config/source_config.py
```

The extraction layer is designed to make the raw database layer reproducible from the source datasets.

---

# Transform Layer

Location:

```text
etl/transform/
```

Primary components:

```text
raw_to_staging.py
run_transform.py
```

The transformation layer converts raw source data into trusted staging data.

## Transformation responsibilities

### String cleaning

Leading and trailing whitespace is removed from string fields.

### Null normalization

Blank and string representations of missing values are normalized to actual database `NULL` values.

For descriptive attributes, missing values are converted to:

```text
UNKNOWN
```

Business keys and foreign keys remain:

```text
NULL
```

when the source value is missing.

### Duplicate removal

Duplicate business-key records are identified and removed.

The first occurrence is retained.

Rejected duplicate records are written to:

```text
logs/transform/rejected_records/
```

### Business-rule validation

Domain-specific rules are applied before records enter staging.

Examples include:

* Negative sales quantities
* Invalid sales prices
* Negative inventory quantities
* Invalid production quantities

Records that fail business validation are removed from staging and written to the rejected-record directory.

### ETL metadata

Staging records receive:

```text
etl_batch_id
etl_loaded_timestamp
source_file
```

This provides basic lineage and execution-level traceability.

---

# Load Layer

Location:

```text
etl/load/
```

Primary components:

```text
staging_to_warehouse.py
run_load.py
```

The load layer transforms trusted staging data into the dimensional warehouse.

The warehouse loader:

1. Clears the existing warehouse data.
2. Loads dimension tables.
3. Creates required default dimension members.
4. Resolves business keys to surrogate keys.
5. Loads fact tables.
6. Reports inserted row counts.
7. Rolls back the warehouse transaction if an error occurs.

---

# Full-Refresh Warehouse Design

The warehouse currently uses a **full-refresh loading strategy**.

Each warehouse execution:

```text
1. Truncates warehouse tables
2. Resets surrogate-key identities
3. Loads dimensions
4. Creates required UNKNOWN dimension members
5. Loads facts
```

This makes repeated pipeline execution deterministic and prevents accumulation of duplicate warehouse records.

Expected behavior:

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
Run 1 → 1× data
Run 2 → 2× data
Run 3 → 3× data
```

The complete warehouse load executes inside a database transaction.

If a dimension or fact load fails, the transaction is rolled back.

---

# Surrogate Keys

Warehouse dimensions use generated surrogate keys.

Examples:

```text
dim_account.account_key
dim_customer.customer_key
dim_product.product_key
dim_supplier.supplier_key
dim_location.location_key
dim_employee.employee_key
dim_machine.machine_key
```

The original business keys are retained in the dimensions.

For example:

```text
customer_id
    │
    ▼
dim_customer
    │
    └── customer_key
            │
            ▼
       fact_sales
```

Facts reference surrogate keys rather than relying directly on source-system identifiers.

---

# Business-Key Normalization

Source-system identifiers may not always use the same formatting convention as warehouse dimension identifiers.

The warehouse load therefore normalizes selected business keys during dimension lookup.

For example, location identifiers may appear in staging as:

```text
LOC_197
LOC_029
LOC_141
```

while the warehouse dimension may contain:

```text
LOC_00197
LOC_00029
LOC_00141
```

The load process normalizes the numeric portion and pads it to the required format before performing the dimension lookup.

This ensures that valid source references resolve to the correct warehouse surrogate key without modifying the trusted staging data.

---

# UNKNOWN Dimension Handling

Missing customer references are intentionally preserved as `NULL` in staging.

During warehouse fact loading, missing customer references are mapped to:

```text
UNKNOWN
```

The warehouse contains a default customer dimension member:

```text
customer_id   = UNKNOWN
customer_name = Unknown Customer
```

This allows fact records with missing customer references to remain in the warehouse while still maintaining a valid dimensional relationship.

Conceptually:

```text
staging.stg_sales_transactions
            │
            │ customer_id = NULL
            ▼
      UNKNOWN mapping
            │
            ▼
warehouse.dim_customer
            │
            │ customer_key
            ▼
warehouse.fact_sales
```

This approach follows the dimensional-modeling principle of using a default dimension member for unknown or unavailable dimensional references rather than dropping the fact record.

---

# Referential Integrity

Fact-table dimension references are resolved using dimension business keys.

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

The same pattern is applied to production, maintenance, financial, energy, emissions, waste, and inventory fact tables.

The warehouse validation layer verifies that populated fact foreign keys resolve to valid dimension surrogate keys.

---

# Data Quality Validation

Validation SQL is located under:

```text
sql/validation/
```

The validation framework covers:

* Row counts
* Duplicate records
* Referential integrity
* Business rules
* Pipeline-level validation

Primary validation files:

```text
business_rule_validation.sql
duplicate_validation.sql
pipeline_validation.sql
referential_integrity.sql
row_count_validation.sql
```

---

# Row Count Validation

The row-count validation compares record movement across:

```text
RAW
 ↓
STAGING
 ↓
WAREHOUSE
```

For each dataset, the validation reports:

```text
raw_count
staging_count
warehouse_count
```

It also calculates:

```text
raw_to_staging_difference
staging_to_warehouse_difference
```

Expected behavior:

```text
staging_count <= raw_count
```

because duplicate and invalid records may be removed during transformation.

For standard dimension and fact tables:

```text
warehouse_count = staging_count
```

The customer dimension is a special case because the warehouse contains one additional default member:

```text
customer_id = 'UNKNOWN'
```

Therefore, customer validation compares the warehouse customer count **excluding the UNKNOWN member** against the staging customer count.

This prevents the intentionally created default dimension member from being incorrectly reported as an ETL row-count failure.

---

# Duplicate Validation

Duplicate validation checks business-key uniqueness.

Examples include:

```text
customer_id
product_id
supplier_id
location_id
employee_id
machine_id
transaction_id
production_id
maintenance_id
inventory_id
```

Duplicates are addressed during the raw-to-staging transformation process.

The validation layer confirms that the resulting trusted data maintains expected business-key uniqueness.

---

# Referential Integrity Validation

The referential integrity validation verifies that warehouse fact foreign keys resolve to valid dimension members.

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

The validation is particularly important for confirming that business-key normalization and UNKNOWN-member handling are functioning correctly.

---

# Business Rule Validation

Business-rule validation checks for known invalid business conditions.

Examples include:

* Negative quantities
* Invalid monetary values
* Invalid prices
* Invalid production measurements
* Invalid operational measurements
* Missing required business keys

Business-rule validation complements the transformation layer.

The transformation layer prevents invalid records from entering trusted staging data, while the validation layer provides an independent verification mechanism.

---

# Pipeline Validation

The pipeline validation framework combines multiple validation categories into an overall data-quality assessment.

Validation results use:

```text
PASS
FAIL
```

This allows the ETL process to be evaluated systematically rather than relying only on successful script execution.

A successfully completed pipeline should therefore satisfy both:

```text
ETL execution success
```

and:

```text
Data-quality validation success
```

---

# Rejected Records

Transformation-level rejected records are stored under:

```text
logs/transform/rejected_records/
```

Examples currently generated by the pipeline include:

```text
customers_duplicates.csv
financial_transactions_duplicates.csv
locations_duplicates.csv
production_duplicates.csv
sales_transactions_duplicates.csv
sales_transactions_validation_errors.csv
```

Rejected records provide visibility into records that were intentionally excluded from the trusted staging layer.

These files support:

* ETL troubleshooting
* Data-quality investigation
* Source-data analysis
* Auditability
* Portfolio demonstration

---

# ETL Logging

Pipeline and ETL execution logs are organized under:

```text
logs/
```

Structure:

```text
logs/
├── extract/
├── load/
├── pipeline.log
└── transform/
    └── rejected_records/
```

The logging structure separates execution artifacts by ETL stage.

The main pipeline execution log is:

```text
logs/pipeline.log
```

---

# Database Scripts

Database creation scripts are located under:

```text
database/
```

## Database initialization

```text
database/create_database.sql
```

## Schema creation

```text
database/create_schemas.sql
```

## Raw tables

```text
database/raw/create_raw_tables.sql
```

## Staging tables

```text
database/staging/create_staging_tables.sql
```

## Warehouse dimensions

```text
database/warehouse/create_dimensions.sql
```

## Warehouse facts

```text
database/warehouse/create_facts.sql
```

The database scripts define the PostgreSQL structures required by the ETL pipeline.

---

# Configuration

Database configuration is located at:

```text
config/database_config.py
```

Database connectivity is centralized through:

```text
etl/database_connection.py
```

This separates database connection logic from individual ETL components.

---

# Metadata

Metadata documentation is located under:

```text
metadata/
```

Files:

```text
metadata/data_dictionary.md
metadata/table_mapping.md
```

## Data Dictionary

Documents:

* Tables
* Columns
* Data types
* Business meaning
* Key definitions

## Table Mapping

Documents relationships between:

```text
Source
  ↓
Raw
  ↓
Staging
  ↓
Warehouse
```

This provides traceability across the ETL architecture.

---

# Dimensional Model Documentation

The warehouse star schema is documented in:

```text
diagrams/star_schema.md
```

The diagram documents:

* Dimension tables
* Fact tables
* Primary keys
* Foreign keys
* Major dimensional relationships

---

# Directory Structure

```text
04_Data_Warehouse/
│
├── config/
│   └── database_config.py
│
├── database/
│   ├── create_database.sql
│   ├── create_schemas.sql
│   ├── raw/
│   │   └── create_raw_tables.sql
│   ├── staging/
│   │   └── create_staging_tables.sql
│   └── warehouse/
│       ├── create_dimensions.sql
│       └── create_facts.sql
│
├── diagrams/
│   └── star_schema.md
│
├── etl/
│   ├── __init__.py
│   ├── database_connection.py
│   │
│   ├── extract/
│   │   ├── __init__.py
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── source_config.py
│   │   ├── extract_csv_to_raw.py
│   │   └── run_extract.py
│   │
│   ├── transform/
│   │   ├── __init__.py
│   │   ├── raw_to_staging.py
│   │   └── run_transform.py
│   │
│   ├── load/
│   │   ├── __init__.py
│   │   ├── run_load.py
│   │   └── staging_to_warehouse.py
│   │
│   └── run_pipeline.py
│
├── logs/
│   ├── extract/
│   ├── load/
│   ├── pipeline.log
│   └── transform/
│       └── rejected_records/
│
├── metadata/
│   ├── data_dictionary.md
│   └── table_mapping.md
│
├── sql/
│   └── validation/
│       ├── business_rule_validation.sql
│       ├── duplicate_validation.sql
│       ├── pipeline_validation.sql
│       ├── referential_integrity.sql
│       └── row_count_validation.sql
│
├── README.md
└── requirements.txt
```

---

# Database Schemas

The PostgreSQL database contains three primary schemas:

```text
raw
staging
warehouse
```

Database:

```text
project_atlas_dw
```

---

# Current Warehouse Scale

The generated datasets are intentionally large enough to demonstrate realistic ETL behavior.

Representative volumes:

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

Differences between raw and staging volumes are intentional and result from duplicate removal and business-rule validation during transformation.

The warehouse is expected to contain the corresponding trusted staging volume, subject to explicitly documented warehouse members such as the `UNKNOWN` customer dimension member.

---

# Technology Stack

| Technology | Purpose                                              |
| ---------- | ---------------------------------------------------- |
| Python     | ETL orchestration and transformation                 |
| Pandas     | CSV processing and data transformation               |
| PostgreSQL | Raw, staging, and warehouse database                 |
| SQLAlchemy | Python/PostgreSQL connectivity                       |
| psycopg2   | PostgreSQL database driver                           |
| SQL        | Database creation, warehouse loading, and validation |
| Git        | Version control                                      |

---

# Operational Design

The Data Warehouse layer is designed as a **repeatable full-refresh ETL pipeline**.

Each execution refreshes the complete data flow:

```text
Source CSV
    ↓
RAW
    ↓
STAGING
    ↓
WAREHOUSE
    ↓
VALIDATION
```

The staging layer is rebuilt during transformation.

The warehouse layer is truncated and reloaded during the warehouse load.

This design provides:

* Repeatability
* Deterministic results
* Easier troubleshooting
* Consistent development environments
* Prevention of warehouse record accumulation

---

# ETL Execution Options

## Run Extract Only

From:

```text
04_Data_Warehouse/
```

run:

```bash
python3 -m etl.extract.run_extract
```

## Run Transformation Only

```bash
python3 -m etl.transform.run_transform
```

## Run Warehouse Load Only

```bash
python3 -m etl.load.run_load
```

## Run Complete Pipeline

```bash
python3 -m etl.run_pipeline
```

The complete pipeline is the recommended execution method when rebuilding the entire Data Warehouse.

---

# Validation Workflow

After the pipeline completes, validation SQL can be executed from:

```text
sql/validation/
```

Recommended validation sequence:

```text
1. Row Count Validation
2. Duplicate Validation
3. Referential Integrity Validation
4. Business Rule Validation
5. Pipeline Validation
```

The validation process should confirm:

```text
PASS
```

for all expected validation checks.

Successful ETL execution alone is not considered sufficient; the resulting data should also pass the warehouse validation framework.

---

# Documentation

Additional technical documentation is available in:

```text
diagrams/star_schema.md
metadata/data_dictionary.md
metadata/table_mapping.md
```

Validation SQL is available in:

```text
sql/validation/
```

---

# Project-Level Documentation

This README documents only the **Data Warehouse and ETL component** of Project Atlas.

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

The Data Warehouse and ETL layer currently implements:

* CSV ingestion
* Raw data persistence
* Staging transformation
* Data cleaning
* Null normalization
* Business-key preservation
* Foreign-key preservation
* Duplicate detection and removal
* Business-rule validation
* Rejected-record logging
* ETL metadata
* Dimensional modeling
* Surrogate-key generation
* Business-key normalization
* UNKNOWN dimension-member handling
* Dimension loading
* Fact loading
* Referential integrity validation
* Row-count validation
* Duplicate validation
* Business-rule validation
* Pipeline-level validation
* ETL execution logging
* Full-refresh warehouse loading
* Transactional warehouse loading
* End-to-end ETL orchestration

The Data Warehouse layer is ready to support the downstream BI and analytics components of Project Atlas.
