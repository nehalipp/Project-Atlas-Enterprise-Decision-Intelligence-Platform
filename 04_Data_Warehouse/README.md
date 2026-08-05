# Enterprise Data Warehouse

## Overview

The Project Atlas Data Warehouse provides a centralized analytical layer for business reporting and analytics.

The warehouse transforms cleaned staging data into structured dimensional models optimized for reporting.

---

# Architecture

The warehouse follows a layered architecture:
                Raw Layer
                     |
                     v
                Staging Layer
                     |
                     v
                Warehouse Layer
                     |
                     v
                BI Analytics

---

# Database Technology

- PostgreSQL

---

# Warehouse Design

Project Atlas uses dimensional modeling.

Model:

Star Schema


## Dimension Tables
dim_customer
dim_product
dim_supplier
dim_location
dim_employee
dim_date

## Fact Tables
fact_sales

---

# ETL Pipeline

The pipeline executes:

## Step 1: Load Raw Data

Source:

CSV generated datasets


Destination:
raw schema


---

## Step 2: Transform Data

Activities:

- Cleaning
- Standardization
- Validation


Destination:
staging schema


---

## Step 3: Load Warehouse

Process:

- Load dimensions
- Generate surrogate keys
- Load fact tables


Destination:
warehouse schema

---

# Data Validation

Validation framework checks:

## Row Counts

Ensures data completeness.


## Duplicate Records

Identifies duplicate business records.


## Null Validation

Checks mandatory fields.


## Referential Integrity

Validates dimension relationships.


## Business Rules

Validates:

- Revenue values
- Transaction consistency
- Business constraints


---

# Pipeline Execution

Run:
python3 etl/run_pipeline.py

Validate:
python3 validation/warehouse_validation.py

## Business Value

The warehouse enables:

Reliable reporting
Consistent KPIs
Faster analytics
Scalable BI solutions


---


# Status

Completed MVP