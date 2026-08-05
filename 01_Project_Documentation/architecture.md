# Project Atlas Architecture

## Overview

Project Atlas follows a modern analytics architecture where raw business data is transformed into structured analytical datasets and consumed through business intelligence tools.

The architecture follows an ELT/ETL layered approach:
Python Data Generation
        |
        v
CSV Source Files
        |
        v
PostgreSQL Raw Layer
        |
        v
PostgreSQL Staging Layer
        |
        v
Enterprise Data Warehouse
        |
        v
Power BI / Tableau
        |
        v
Business Insights


---

# Architecture Layers


## 1. Data Generation Layer

Purpose:

Generate realistic enterprise datasets for analytics development.

Technology:

- Python
- Faker
- Pandas


Generated datasets:

- Customers
- Products
- Suppliers
- Locations
- Employees
- Sales Transactions


Output:

CSV files containing raw enterprise data.


---

# 2. Raw Data Layer

Purpose:

Store source data before transformation.

Schema:
raw

Characteristics:

- Maintains original source structure
- Preserves source records
- Supports data auditing


Example tables:
raw.customers
raw.products
raw.suppliers
raw.locations
raw.employees
raw.sales_transactions


---

# 3. Staging Layer

Purpose:

Clean and standardize raw data before warehouse loading.

Schema:
staging


Transformations include:

- Removing invalid records
- Handling missing values
- Standardizing formats
- Applying business rules


Example:

Before:
USA
US
U.S.A


After:
United States


---

# 4. Enterprise Data Warehouse

Purpose:

Provide centralized analytical datasets.

Schema:
warehouse


The warehouse uses dimensional modeling.


## Star Schema Design


Dimension Tables:
dim_customer
dim_product
dim_supplier
dim_location
dim_employee
dim_date


Fact Table:
fact_sales


Relationship:

                 dim_date
                     |
                     |
dim_customer --- fact_sales --- dim_product
                     |
                     |
                 dim_location
                     |
                     |
                 dim_employee
                     |
                     |
                 dim_supplier


---

# 5. Business Intelligence Layer

Tools:

- Power BI
- Tableau


Purpose:

Deliver business insights through dashboards.


Analytics areas:

- Revenue analysis
- Sales trends
- Customer analysis
- Product performance


---

# Data Pipeline Flow

The complete pipeline execution:
Generate Data
        |
        v
Load Raw Tables
        |
        v
Transform Staging Tables
        |
        v
Load Dimensions
        |
        v
Load Fact Tables
        |
        v
Validate Warehouse
        |
        v
Build Dashboards


---

# Data Quality Framework

Validation checks include:

## Completeness

Checks missing required values.


## Duplicate Detection

Identifies duplicate records.


## Referential Integrity

Ensures relationships between fact and dimension tables.


## Business Rules

Examples:

- Revenue cannot be negative
- Customer IDs must exist
- Product references must be valid


---

# Architecture Benefits

This architecture provides:

- Centralized analytics data
- Reliable reporting
- Improved data quality
- Scalable warehouse design
- Faster business insights