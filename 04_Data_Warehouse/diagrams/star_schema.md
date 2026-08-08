# Project Atlas — Star Schema

## Overview

The Project Atlas Data Warehouse uses a **dimensional star schema** designed to support enterprise analytics across sales, production, maintenance, finance, inventory, energy, emissions, and waste.

The warehouse separates:

* **Dimension tables** — descriptive business entities
* **Fact tables** — measurable business events and activities
* **Surrogate keys** — warehouse-generated identifiers used by fact tables
* **Business keys** — identifiers originating from source systems

The warehouse schema is:

```text
warehouse
│
├── Dimensions
│   ├── dim_account
│   ├── dim_customer
│   ├── dim_employee
│   ├── dim_location
│   ├── dim_machine
│   ├── dim_product
│   └── dim_supplier
│
└── Facts
    ├── fact_budget
    ├── fact_emissions
    ├── fact_energy_consumption
    ├── fact_financial_transactions
    ├── fact_inventory
    ├── fact_maintenance
    ├── fact_production
    ├── fact_sales
    └── fact_waste
```

---

# Dimensions

## dim_account

**Grain:** One row per account.

Contains financial account master data.

Primary surrogate key:

```text
account_key
```

Business key:

```text
account_id
```

Used by:

```text
fact_financial_transactions
```

---

## dim_customer

**Grain:** One row per customer.

Contains customer master and segmentation information.

Primary surrogate key:

```text
customer_key
```

Business key:

```text
customer_id
```

Used by:

```text
fact_sales
```

---

## dim_product

**Grain:** One row per product.

Contains product classification and pricing information.

Primary surrogate key:

```text
product_key
```

Business key:

```text
product_id
```

Used by:

```text
fact_sales
fact_production
fact_inventory
```

---

## dim_supplier

**Grain:** One row per supplier.

Contains supplier classification, geography, performance, and status.

Primary surrogate key:

```text
supplier_key
```

Business key:

```text
supplier_id
```

---

## dim_location

**Grain:** One row per operational location.

Contains facility, geographic, and operating information.

Primary surrogate key:

```text
location_key
```

Business key:

```text
location_id
```

Used by:

```text
fact_sales
fact_production
fact_energy_consumption
fact_emissions
fact_waste
fact_inventory
```

---

## dim_employee

**Grain:** One row per employee.

Contains employee, organizational, compensation, and performance information.

Primary surrogate key:

```text
employee_key
```

Business key:

```text
employee_id
```

---

## dim_machine

**Grain:** One row per machine.

Contains machine ownership, location, lifecycle, warranty, and operational status.

Primary surrogate key:

```text
machine_key
```

Business key:

```text
machine_id
```

Used by:

```text
fact_production
fact_maintenance
```

---

# Fact Tables

## fact_sales

**Grain:** One row per valid sales transaction.

Measures:

* quantity
* unit price
* discount percentage
* revenue

Dimension relationships:

```text
customer_key → dim_customer
product_key  → dim_product
location_key → dim_location
```

---

## fact_production

**Grain:** One row per production event.

Measures:

* units produced
* defect count
* defect rate
* production hours

Dimension relationships:

```text
machine_key  → dim_machine
product_key  → dim_product
location_key → dim_location
```

---

## fact_maintenance

**Grain:** One row per maintenance event.

Measures:

* downtime hours
* repair cost

Dimension relationship:

```text
machine_key → dim_machine
```

---

## fact_financial_transactions

**Grain:** One row per financial transaction.

Measure:

* amount

Dimension relationship:

```text
account_key → dim_account
```

---

## fact_budget

**Grain:** One row per budget record.

Measure:

* budget amount

The current model stores department and account type directly in the fact.

---

## fact_energy_consumption

**Grain:** One row per energy measurement.

Measures:

* consumption kWh
* energy cost

Dimension relationship:

```text
location_key → dim_location
```

---

## fact_emissions

**Grain:** One row per emissions measurement.

Measure:

* carbon emission tons

Dimension relationship:

```text
location_key → dim_location
```

---

## fact_waste

**Grain:** One row per waste measurement.

Measure:

* quantity tons

Dimension relationship:

```text
location_key → dim_location
```

---

## fact_inventory

**Grain:** One row per inventory measurement.

Measures:

* inventory quantity
* unit cost
* inventory value

Dimension relationships:

```text
product_key  → dim_product
location_key → dim_location
```

---

# Surrogate Key Strategy

Warehouse dimensions use PostgreSQL-generated surrogate keys:

```text
BIGSERIAL
```

Example:

```text
customer_key
product_key
location_key
```

Fact tables store these surrogate keys rather than relying exclusively on source-system business keys.

Business keys remain available where appropriate for traceability.

---

# ETL Relationship

The warehouse is populated through the following flow:

```text
CSV Source Files
      │
      ▼
Raw Schema
      │
      │ Extract
      ▼
raw.*
      │
      │ Transform
      │ - Trim strings
      │ - Normalize nulls
      │ - Remove duplicates
      │ - Apply business validations
      │ - Reject invalid records
      ▼
staging.stg_*
      │
      │ Load
      │ - Load dimensions
      │ - Resolve surrogate keys
      │ - Load facts
      ▼
warehouse.*
```

---

# Warehouse Loading Order

Dimensions are loaded first:

```text
dim_account
dim_customer
dim_product
dim_supplier
dim_location
dim_employee
dim_machine
```

Facts are then loaded:

```text
fact_sales
fact_production
fact_maintenance
fact_financial_transactions
fact_budget
fact_energy_consumption
fact_emissions
fact_waste
fact_inventory
```

This ordering ensures that dimension surrogate keys are available when fact records are loaded.

---

# Design Principles

The warehouse follows these principles:

1. Use dimensional modeling for analytics.
2. Separate descriptive attributes from measurable events.
3. Use surrogate keys for warehouse relationships.
4. Preserve source business keys for traceability.
5. Clean and validate data before warehouse loading.
6. Load dimensions before facts.
7. Keep raw data unchanged for auditability.
8. Use staging as the trusted transformation layer.
9. Validate row counts and data quality after ETL execution.
10. Keep the warehouse optimized for BI and analytical workloads.
