# Project Atlas — Data Dictionary

## Purpose

This document provides the business and technical definitions for the tables in the Project Atlas Data Warehouse.

The warehouse contains:

* 7 dimension tables
* 9 fact tables
* 16 staging tables
* Corresponding raw source tables

---

# Dimension Tables

## dim_account

| Column           | Type         | Description                    |
| ---------------- | ------------ | ------------------------------ |
| account_key      | BIGSERIAL    | Warehouse surrogate key        |
| account_id       | VARCHAR(50)  | Source business key            |
| account_name     | VARCHAR(255) | Account name                   |
| account_type     | VARCHAR(100) | Account classification         |
| account_category | VARCHAR(100) | Account category               |
| department       | VARCHAR(100) | Associated department          |
| active_status    | VARCHAR(50)  | Account active/inactive status |

---

## dim_customer

| Column           | Type         | Description                      |
| ---------------- | ------------ | -------------------------------- |
| customer_key     | BIGSERIAL    | Warehouse surrogate key          |
| customer_id      | VARCHAR(50)  | Source business key              |
| customer_name    | VARCHAR(255) | Customer name                    |
| industry         | VARCHAR(100) | Customer industry                |
| customer_segment | VARCHAR(100) | Customer segment                 |
| country          | VARCHAR(100) | Customer country                 |
| region           | VARCHAR(100) | Customer region                  |
| customer_since   | DATE         | Customer relationship start date |

---

## dim_product

| Column         | Type          | Description             |
| -------------- | ------------- | ----------------------- |
| product_key    | BIGSERIAL     | Warehouse surrogate key |
| product_id     | VARCHAR(50)   | Source business key     |
| product_name   | VARCHAR(255)  | Product name            |
| category       | VARCHAR(100)  | Product category        |
| unit_cost      | NUMERIC(18,2) | Product unit cost       |
| unit_price     | NUMERIC(18,2) | Product selling price   |
| product_status | VARCHAR(50)   | Product status          |

---

## dim_supplier

| Column             | Type         | Description                 |
| ------------------ | ------------ | --------------------------- |
| supplier_key       | BIGSERIAL    | Warehouse surrogate key     |
| supplier_id        | VARCHAR(50)  | Source business key         |
| supplier_name      | VARCHAR(255) | Supplier name               |
| supplier_category  | VARCHAR(100) | Supplier classification     |
| country            | VARCHAR(100) | Supplier country            |
| region             | VARCHAR(100) | Supplier region             |
| performance_rating | NUMERIC(5,2) | Supplier performance rating |
| supplier_status    | VARCHAR(50)  | Supplier status             |

---

## dim_location

| Column           | Type          | Description                      |
| ---------------- | ------------- | -------------------------------- |
| location_key     | BIGSERIAL     | Warehouse surrogate key          |
| location_id      | VARCHAR(50)   | Source business key              |
| facility_name    | VARCHAR(255)  | Facility name                    |
| location_type    | VARCHAR(100)  | Facility/location classification |
| city             | VARCHAR(100)  | City                             |
| state            | VARCHAR(100)  | State or province                |
| country          | VARCHAR(100)  | Country                          |
| region           | VARCHAR(100)  | Geographic region                |
| latitude         | NUMERIC(10,6) | Latitude                         |
| longitude        | NUMERIC(10,6) | Longitude                        |
| operating_status | VARCHAR(50)   | Operational status               |
| opening_date     | DATE          | Facility opening date            |

---

## dim_employee

| Column             | Type          | Description                 |
| ------------------ | ------------- | --------------------------- |
| employee_key       | BIGSERIAL     | Warehouse surrogate key     |
| employee_id        | VARCHAR(50)   | Source business key         |
| employee_name      | VARCHAR(255)  | Employee name               |
| department         | VARCHAR(100)  | Employee department         |
| job_title          | VARCHAR(150)  | Job title                   |
| location_id        | VARCHAR(50)   | Employee source location    |
| manager_id         | VARCHAR(50)   | Manager source identifier   |
| hire_date          | DATE          | Employee hire date          |
| salary             | NUMERIC(18,2) | Employee salary             |
| employment_status  | VARCHAR(50)   | Employment status           |
| performance_rating | NUMERIC(5,2)  | Employee performance rating |

---

## dim_machine

| Column              | Type          | Description              |
| ------------------- | ------------- | ------------------------ |
| machine_key         | BIGSERIAL     | Warehouse surrogate key  |
| machine_id          | VARCHAR(50)   | Source business key      |
| machine_name        | VARCHAR(255)  | Machine name             |
| machine_type        | VARCHAR(100)  | Machine classification   |
| manufacturer        | VARCHAR(150)  | Machine manufacturer     |
| location_id         | VARCHAR(50)   | Machine source location  |
| purchase_date       | DATE          | Machine purchase date    |
| warranty_expiry     | DATE          | Warranty expiration date |
| expected_life_years | NUMERIC(10,2) | Expected useful life     |
| machine_status      | VARCHAR(50)   | Machine status           |

---

# Fact Tables

## fact_sales

**Grain:** One valid sales transaction.

| Column              | Description                   |
| ------------------- | ----------------------------- |
| sales_key           | Warehouse surrogate fact key  |
| transaction_id      | Source transaction identifier |
| customer_key        | Customer dimension key        |
| product_key         | Product dimension key         |
| location_key        | Location dimension key        |
| transaction_date    | Transaction date              |
| quantity            | Quantity sold                 |
| unit_price          | Selling price per unit        |
| discount_percentage | Applied discount              |
| revenue             | Transaction revenue           |
| sales_channel       | Sales channel                 |

---

## fact_production

**Grain:** One production event.

Measures include:

* units produced
* defect count
* defect rate
* production hours

Dimension keys:

* machine_key
* product_key
* location_key

---

## fact_maintenance

**Grain:** One maintenance event.

Measures include:

* downtime hours
* repair cost

Dimension key:

* machine_key

---

## fact_financial_transactions

**Grain:** One financial transaction.

Measures include:

* amount

Dimension key:

* account_key

---

## fact_budget

**Grain:** One budget record.

Measures include:

* budget amount

---

## fact_energy_consumption

**Grain:** One energy measurement.

Measures:

* consumption kWh
* energy cost

Dimension key:

* location_key

---

## fact_emissions

**Grain:** One emissions measurement.

Measure:

* carbon emission tons

Dimension key:

* location_key

---

## fact_waste

**Grain:** One waste measurement.

Measure:

* quantity tons

Dimension key:

* location_key

---

## fact_inventory

**Grain:** One inventory measurement.

Measures:

* inventory quantity
* unit cost
* inventory value

Dimension keys:

* product_key
* location_key

---

# Audit Columns

Staging tables include ETL metadata:

| Column               | Description                               |
| -------------------- | ----------------------------------------- |
| etl_batch_id         | UUID identifying the ETL batch            |
| etl_loaded_timestamp | Timestamp when the record entered staging |
| source_file          | Source/raw table identifier               |

These fields provide basic ETL traceability and auditability.

---

# Data Quality Handling

The transformation layer performs:

* String trimming
* Null/blank normalization
* Duplicate detection
* Business rule validation
* Invalid-record rejection
* ETL metadata assignment

Rejected records are written to:

```text
logs/transform/rejected_records/
```

---

# Naming Conventions

| Convention    | Meaning                    |
| ------------- | -------------------------- |
| `*_key`       | Warehouse surrogate key    |
| `*_id`        | Source/business identifier |
| `dim_*`       | Dimension table            |
| `fact_*`      | Fact table                 |
| `stg_*`       | Staging table              |
| `raw.*`       | Raw ingestion table        |
| `warehouse.*` | Analytics warehouse table  |
