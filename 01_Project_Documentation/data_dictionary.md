# Project Atlas Data Dictionary

## Overview

This document describes the analytical warehouse tables used in Project Atlas.

The warehouse follows a star schema design consisting of:

- Dimension tables
- Fact tables


---

# Warehouse Schema

Schema:
warehouse


---

# Dimension Tables


# dim_customer

## Purpose

Stores customer master information.

## Grain

One record per customer.


| Column | Description |
|---|---|
| customer_key | Warehouse surrogate key |
| customer_id | Source customer identifier |
| customer_name | Customer name |
| industry | Customer industry |
| customer_segment | Customer classification |
| country | Customer country |
| region | Geographic region |
| effective_date | Record effective date |


---

# dim_product

## Purpose

Stores product information.

## Grain

One record per product.


| Column | Description |
|---|---|
| product_key | Warehouse key |
| product_id | Product identifier |
| product_name | Product name |
| category | Product category |
| supplier_key | Supplier reference |
| unit_cost | Product cost |
| unit_price | Selling price |


---

# dim_supplier

## Purpose

Stores supplier information.


| Column | Description |
|---|---|
| supplier_key | Warehouse key |
| supplier_id | Supplier identifier |
| supplier_name | Supplier name |
| country | Supplier location |
| supplier_category | Supplier type |


---

# dim_location

## Purpose

Stores business location information.


| Column | Description |
|---|---|
| location_key | Warehouse key |
| facility_name | Facility name |
| city | City |
| country | Country |
| region | Region |


---

# dim_employee

## Purpose

Stores employee information.


| Column | Description |
|---|---|
| employee_key | Warehouse key |
| employee_id | Employee identifier |
| department | Department |
| job_title | Employee role |
| location | Work location |


---

# dim_date

## Purpose

Provides calendar attributes for reporting.


| Column | Description |
|---|---|
| date_key | Date surrogate key |
| full_date | Calendar date |
| month_name | Month |
| quarter | Quarter |
| year | Year |


---

# Fact Tables


# fact_sales

## Purpose

Stores sales transaction data.

## Grain

One record per sales transaction.


| Column | Description |
|---|---|
| sales_key | Transaction identifier |
| date_key | Transaction date |
| customer_key | Customer reference |
| product_key | Product reference |
| location_key | Location reference |
| employee_key | Employee reference |
| quantity_sold | Units sold |
| unit_price | Selling price |
| sales_amount | Revenue amount |


---

# Data Quality Rules


## Customer Data

Rules:

- Customer ID cannot be null
- Customer name must exist


## Product Data

Rules:

- Product ID must exist
- Category cannot be empty


## Sales Data

Rules:

- Revenue cannot be negative
- Quantity must be greater than zero
- Dimension keys must exist


---

# Data Ownership

| Domain | Owner |
|---|---|
| Customers | Sales / CRM |
| Products | Product Management |
| Suppliers | Procurement |
| Employees | HR |
| Sales | Sales Operations |