# Project Atlas — Table Mapping

## Purpose

This document defines the end-to-end mapping between source datasets, raw tables, staging tables, and warehouse tables.

The ETL architecture follows:

```text
CSV
 ↓
RAW
 ↓
STAGING
 ↓
WAREHOUSE
```

---

# Complete Table Mapping

| #  | Source Dataset             | Raw Table                  | Staging Table                      | Warehouse Table                       | Type      |
| -- | -------------------------- | -------------------------- | ---------------------------------- | ------------------------------------- | --------- |
| 1  | accounts.csv               | raw.accounts               | staging.stg_accounts               | warehouse.dim_account                 | Dimension |
| 2  | customers.csv              | raw.customers              | staging.stg_customers              | warehouse.dim_customer                | Dimension |
| 3  | products.csv               | raw.products               | staging.stg_products               | warehouse.dim_product                 | Dimension |
| 4  | suppliers.csv              | raw.suppliers              | staging.stg_suppliers              | warehouse.dim_supplier                | Dimension |
| 5  | locations.csv              | raw.locations              | staging.stg_locations              | warehouse.dim_location                | Dimension |
| 6  | employees.csv              | raw.employees              | staging.stg_employees              | warehouse.dim_employee                | Dimension |
| 7  | machines.csv               | raw.machines               | staging.stg_machines               | warehouse.dim_machine                 | Dimension |
| 8  | sales_transactions.csv     | raw.sales_transactions     | staging.stg_sales_transactions     | warehouse.fact_sales                  | Fact      |
| 9  | production.csv             | raw.production             | staging.stg_production             | warehouse.fact_production             | Fact      |
| 10 | maintenance.csv            | raw.maintenance            | staging.stg_maintenance            | warehouse.fact_maintenance            | Fact      |
| 11 | financial_transactions.csv | raw.financial_transactions | staging.stg_financial_transactions | warehouse.fact_financial_transactions | Fact      |
| 12 | budget.csv                 | raw.budget                 | staging.stg_budget                 | warehouse.fact_budget                 | Fact      |
| 13 | energy_consumption.csv     | raw.energy_consumption     | staging.stg_energy_consumption     | warehouse.fact_energy_consumption     | Fact      |
| 14 | emissions.csv              | raw.emissions              | staging.stg_emissions              | warehouse.fact_emissions              | Fact      |
| 15 | waste.csv                  | raw.waste                  | staging.stg_waste                  | warehouse.fact_waste                  | Fact      |
| 16 | inventory.csv              | raw.inventory              | staging.stg_inventory              | warehouse.fact_inventory              | Fact      |

---

# ETL Flow

## 1. Extract

CSV files are read from the Data Generation layer.

The extraction process:

1. Reads the configured CSV file.
2. Validates that the file exists.
3. Loads records into the corresponding raw table.
4. Truncates the previous raw load before inserting the new batch.

Raw tables preserve the source structure as closely as possible.

---

# 2. Transform

Raw data is transformed into staging data.

Transformation operations include:

* String trimming
* Blank value normalization
* Duplicate removal
* Business rule validation
* Invalid record rejection
* ETL batch metadata assignment

Records rejected during transformation are written to:

```text
logs/transform/rejected_records/
```

---

# 3. Load

Staging data is loaded into the warehouse.

The loading sequence is:

```text
1. Truncate warehouse tables
2. Load dimensions
3. Resolve dimension surrogate keys
4. Load facts
5. Execute validation checks
```

---

# Dimension Key Resolution

Fact tables do not directly store source business keys as their dimensional relationships.

Instead, business keys from staging are resolved to warehouse surrogate keys.

Example:

```text
stg_sales_transactions.customer_id
             │
             ▼
dim_customer.customer_id
             │
             ▼
dim_customer.customer_key
             │
             ▼
fact_sales.customer_key
```

The same pattern is used for products, locations, machines, and accounts.

---

# Dimension Lookup Mapping

| Fact                        | Staging Business Key | Dimension    | Warehouse Key |
| --------------------------- | -------------------- | ------------ | ------------- |
| fact_sales                  | customer_id          | dim_customer | customer_key  |
| fact_sales                  | product_id           | dim_product  | product_key   |
| fact_sales                  | location_id          | dim_location | location_key  |
| fact_production             | machine_id           | dim_machine  | machine_key   |
| fact_production             | product_id           | dim_product  | product_key   |
| fact_production             | location_id          | dim_location | location_key  |
| fact_maintenance            | machine_id           | dim_machine  | machine_key   |
| fact_financial_transactions | account_id           | dim_account  | account_key   |
| fact_energy_consumption     | location_id          | dim_location | location_key  |
| fact_emissions              | location_id          | dim_location | location_key  |
| fact_waste                  | location_id          | dim_location | location_key  |
| fact_inventory              | product_id           | dim_product  | product_key   |
| fact_inventory              | location_id          | dim_location | location_key  |

---

# Data Quality Expectations

The ETL process intentionally allows staging counts to be lower than raw counts when invalid or duplicate records are removed.

Expected relationship:

```text
warehouse_count = staging_count
```

For most tables:

```text
staging_count <= raw_count
```

The exception is not expected to be a normal condition; warehouse loads should not create additional fact or dimension rows beyond the staging data.

---

# Lineage

The complete lineage is:

```text
02_Data_Generation
        │
        ▼
    CSV Files
        │
        ▼
     raw.*
        │
        ▼
   staging.stg_*
        │
        ├───────────────┐
        │               │
        ▼               ▼
 Dimensions          Facts
        │               │
        └───────┬───────┘
                ▼
          warehouse.*
                │
                ▼
        BI / Analytics
```
