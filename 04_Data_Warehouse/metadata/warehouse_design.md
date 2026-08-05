# Project Atlas
# Enterprise Data Warehouse Design

## Overview

The Project Atlas Enterprise Data Warehouse follows a dimensional modeling approach to support scalable business intelligence, analytics, and executive reporting.

The warehouse is organized into three logical layers:

- Raw Layer
- Staging Layer
- Warehouse Layer

Only validated and transformed data is promoted into the warehouse layer.

---

# Business Process

The primary business process modeled within Project Atlas is:

**Enterprise Sales**

Every record within the fact table represents a completed sales transaction.

This design supports analytics across customers, products, suppliers, employees, locations, and time.

---

# Fact Table Grain

The grain of the fact table is:

> One row represents one sales transaction for one product purchased by one customer at one location on one date.

This definition ensures consistent aggregation and prevents double counting.

---

# Star Schema

```text
                     dim_date
                        │
                        │
dim_customer ───────────┼────────── dim_product
                        │
                        │
                 fact_sales
                        │
                        │
          dim_location  │  dim_employee
                        │
                        │
                 dim_supplier
```

---

# Dimension Tables

## dim_customer

Purpose:

Stores customer master information.

Business Key:

customer_id

Surrogate Key:

customer_key

Attributes:

- customer_name
- industry
- customer_segment
- country
- region
- customer_since

---

## dim_product

Purpose:

Stores product master information.

Business Key:

product_id

Surrogate Key:

product_key

Attributes:

- product_name
- category
- supplier_id
- unit_cost
- unit_price
- product_status
- launch_date

---

## dim_supplier

Purpose:

Stores supplier information.

Business Key:

supplier_id

Surrogate Key:

supplier_key

Attributes:

- supplier_name
- supplier_country
- supplier_rating

---

## dim_employee

Purpose:

Stores employee information.

Business Key:

employee_id

Surrogate Key:

employee_key

Attributes:

- employee_name
- department
- designation
- manager
- hire_date

---

## dim_location

Purpose:

Stores geographic location information.

Business Key:

location_id

Surrogate Key:

location_key

Attributes:

- city
- state
- country
- region

---

## dim_date

Purpose:

Supports calendar-based reporting.

Surrogate Key:

date_key

Attributes:

- full_date
- day
- month
- month_name
- quarter
- year
- week_number
- weekday

---

# Fact Table

## fact_sales

Purpose:

Stores measurable business transactions.

Foreign Keys:

- customer_key
- product_key
- supplier_key
- employee_key
- location_key
- date_key

Measures:

- quantity
- unit_price
- discount_percentage
- revenue

---

# Surrogate Key Strategy

The warehouse uses surrogate keys for all dimension tables.

Benefits:

- Improved join performance
- Historical tracking
- Independence from source system identifiers
- Simplified Slowly Changing Dimensions

---

# Slowly Changing Dimensions

The following dimensions will support Slowly Changing Dimension (Type 2):

- Customer
- Product

Additional metadata:

- effective_start_date
- effective_end_date
- is_current

---

# Audit Columns

Every warehouse table will include:

- created_at
- updated_at
- source_system
- etl_run_id

These fields support governance, lineage, and ETL auditing.

---

# Warehouse Benefits

The dimensional model provides:

- Faster reporting
- Simplified SQL queries
- Consistent KPI calculations
- Historical tracking
- Optimized Power BI and Tableau performance