# Project Atlas: Enterprise Decision Intelligence Platform

# Enterprise Data Model

## Document Purpose

This document defines the enterprise analytical data model for Project Atlas.

The purpose of this model is to establish a scalable dimensional warehouse structure that integrates data across multiple business domains while enabling consistent reporting and analytics.

---

# Data Modeling Approach

Project Atlas follows:

## Dimensional Modeling

Based on:

- Star schema architecture
- Business process modeling
- Fact and dimension design
- Historical data tracking

---

# Enterprise Warehouse Structure

The warehouse will contain:

## Dimension Tables

Used to provide descriptive context.

Primary dimensions:

- Date
- Customer
- Product
- Supplier
- Employee
- Location
- Machine

---

## Fact Tables

Used to store measurable business events.

Primary facts:

- Sales
- Finance
- Inventory
- Production
- Maintenance
- Energy Consumption

---

# Dimension Model Design

---

# DIM_DATE

## Purpose

Provides standardized time intelligence for all analytical reporting.

## Grain

One record per calendar date.

## Attributes

| Column | Description |
|---|---|
| date_key | Surrogate key |
| full_date | Actual date |
| day | Day number |
| month | Month number |
| month_name | Month description |
| quarter | Quarter |
| year | Calendar year |
| fiscal_period | Fiscal reporting period |

## Usage

Supports:

- Year-over-year analysis
- Monthly trends
- Quarterly reporting

---

# DIM_CUSTOMER

## Purpose

Stores customer master information.

## Grain

One record per customer version.

## Attributes

| Column | Description |
|---|---|
| customer_key | Surrogate key |
| customer_id | Source identifier |
| customer_name | Customer name |
| industry | Customer industry |
| segment | Customer segment |
| country | Customer country |
| region | Geographic region |
| effective_date | Record start date |
| expiration_date | Record end date |

---

## Slowly Changing Dimension Strategy

Type 2 SCD will be used.

Purpose:

Maintain customer history.

Example:

Customer changes region:

Before:
Customer A
Region: North America

After:
Customer A
Region: Europe

Both versions remain available historically.

---

# DIM_PRODUCT

## Purpose

Stores product information.

## Grain

One record per product.

## Attributes

| Column | Description |
|---|---|
| product_key | Surrogate key |
| product_id | Source identifier |
| product_name | Product name |
| category | Product category |
| supplier | Supplier |
| unit_cost | Product cost |
| unit_price | Selling price |

---

# DIM_SUPPLIER

## Purpose

Stores supplier information.

## Attributes

| Column | Description |
|---|---|
| supplier_key | Surrogate key |
| supplier_id | Source identifier |
| supplier_name | Supplier name |
| country | Supplier country |
| supplier_category | Supplier type |
| performance_rating | Supplier score |

---

# DIM_EMPLOYEE

## Purpose

Supports workforce analytics.

## Attributes

| Column | Description |
|---|---|
| employee_key | Surrogate key |
| employee_id | Source identifier |
| department | Department |
| job_title | Role |
| location | Work location |
| hire_date | Hiring date |
| employment_status | Active/Inactive |

---

# DIM_LOCATION

## Purpose

Provides geographic analysis.

## Attributes

| Column | Description |
|---|---|
| location_key | Surrogate key |
| facility_name | Facility |
| city | City |
| country | Country |
| region | Region |

---

# DIM_MACHINE

## Purpose

Supports operational and maintenance analytics.

## Attributes

| Column | Description |
|---|---|
| machine_key | Surrogate key |
| machine_id | Source identifier |
| machine_type | Equipment type |
| facility | Location |
| installation_date | Installed date |

---

# Fact Model Design

---

# FACT_SALES

## Business Process

Customer sales transactions.

## Grain

One row per product transaction.

## Measures

| Column | Description |
|---|---|
| quantity_sold | Units sold |
| unit_price | Selling price |
| discount_amount | Discount |
| sales_amount | Revenue |

## Foreign Keys

- date_key
- customer_key
- product_key
- location_key

---

## Business Questions

Answers:

- What products generate the most revenue?
- Which customers are most valuable?
- How is revenue trending?

---

# FACT_FINANCE

## Business Process

Financial transactions.

## Grain

One financial transaction.

## Measures

- Revenue
- Expense
- Profit
- Budget Amount

## Foreign Keys

- date_key
- location_key

---

# FACT_INVENTORY

## Business Process

Inventory movement.

## Grain

One inventory snapshot per product/location/date.

## Measures

- Quantity Available
- Stock Value
- Inventory Movement

---

# FACT_PRODUCTION

## Business Process

Manufacturing activity.

## Grain

One production event.

## Measures

- Units Produced
- Production Time
- Defect Count

## Foreign Keys

- date_key
- product_key
- machine_key
- location_key

---

# FACT_MAINTENANCE

## Business Process

Equipment maintenance events.

## Grain

One maintenance event.

## Measures

- Repair Cost
- Downtime Hours
- Failure Count

---

# FACT_ENERGY_CONSUMPTION

## Business Process

Environmental monitoring.

## Grain

One energy measurement per facility/date.

## Measures

- Energy Usage
- Carbon Emissions
- Waste Generated

---

# Enterprise Data Model Relationship Overview
                 dim_customer
                      |
                      |
dim_date ---- fact_sales ---- dim_product
                      |
                      |
                 dim_location

dim_date ---- fact_inventory ---- dim_product

dim_date ---- fact_production ---- dim_machine

dim_date ---- fact_maintenance ---- dim_machine

dim_date ---- fact_energy_consumption ---- dim_location

---

# Data Warehouse Benefits

The enterprise model provides:

- Consistent KPI calculations
- Faster analytical queries
- Historical tracking
- Scalable reporting
- Department-level analytics

---

# Future Extensions

Additional analytical domains can be added:

- Marketing Analytics
- Risk Analytics
- Product Analytics
- Healthcare Analytics
- Financial Services Analytics

---

# Document Status

Phase:

Phase 1 - Enterprise Data Architecture

Status:

Draft