# Project Atlas: Enterprise Decision Intelligence Platform

# Data Warehouse Design Document

## Document Purpose

This document defines the physical data warehouse architecture for Project Atlas.

The purpose of the warehouse is to provide a scalable, reliable, and optimized analytical environment that integrates data from multiple enterprise source systems.

The warehouse follows a layered architecture separating raw data ingestion, transformation processes, analytical modeling, and business reporting.

---

# Data Warehouse Architecture Overview

Project Atlas uses a multi-layer warehouse architecture:
Source Systems
  |

  ↓
Raw Data Layer
  |

  ↓
Staging Layer
  |

  ↓
Enterprise Warehouse Layer
  |

  ↓
Business Data Marts
  |

  ↓
BI & Analytics Applications


---

# Database Platform

## Primary Database

PostgreSQL

Reason:

- Open-source enterprise database
- Strong analytical capabilities
- Excellent SQL support
- Supports dimensional modeling
- Widely used in modern data platforms

---

# Database Schema Architecture

Project Atlas will use separate schemas to organize data.

Database:
atlas_enterprise_dw

---

# Schema 1: RAW

## Purpose

Stores source data exactly as received.

No business transformations are applied.

Purpose:

- Preserve source information
- Enable data lineage
- Support auditing
- Allow reprocessing

---

## RAW Tables

Examples:
raw.customers

raw.products

raw.sales_transactions

raw.inventory

raw.employees

raw.sensor_measurements

---

## Raw Layer Characteristics

Includes metadata columns:

| Column | Purpose |
|---|---|
| source_system | Origin system |
| ingestion_timestamp | Load time |
| file_name | Source file |
| batch_id | Processing batch |

---

# Schema 2: STAGING

## Purpose

Provides temporary processing space where data is cleaned and standardized.

---

## Transformation Activities

Includes:

- Data type conversion
- Null handling
- Duplicate removal
- Standardization
- Validation

---

## Staging Tables

Examples:
stg.customers_clean

stg.products_clean

stg.sales_clean

stg.inventory_clean

---

# Schema 3: WAREHOUSE

## Purpose

Stores enterprise analytical models.

This is the primary reporting layer.

---

# Warehouse Modeling Approach

Project Atlas follows:

## Star Schema

Benefits:

- Faster reporting queries
- Simple business understanding
- Optimized BI performance

---

# Dimension Tables

Stored in:
warehouse.dimensions

---

## Dimension Tables
dim_date

dim_customer

dim_product

dim_supplier

dim_employee

dim_location

dim_machine

---

# Dimension Design Standards

All dimensions follow:

## Surrogate Keys

Example:
customer_key

instead of:
customer_id

Purpose:

- Better historical tracking
- Improved joins
- Source system independence

---

## Audit Columns

Each dimension includes:
created_date

updated_date

record_status


---

# Slowly Changing Dimensions

Project Atlas uses:

## SCD Type 2

Purpose:

Maintain historical changes.

Example:

Customer changes region:

Previous:
Customer:
ABC Corporation

Region:
North America

Valid Until:
2026-06-30

New record:
Customer:
ABC Corporation

Region:
Europe

Effective Date:
2026-07-01

Both records remain available for historical reporting.

---

# Fact Tables

Stored in:
warehouse.facts

---

# FACT_SALES

## Purpose

Stores customer purchase transactions.

## Grain

One row per product sale transaction.

---

## Measures
quantity_sold

unit_price

discount_amount

sales_amount

---

## Foreign Keys
date_key

customer_key

product_key

location_key

---

# FACT_FINANCE

## Purpose

Stores financial transactions.

## Grain

One financial transaction.

---

## Measures
revenue_amount

expense_amount

profit_amount

budget_amount

---

# FACT_INVENTORY

## Purpose

Tracks inventory levels.

## Grain

One product-location-date snapshot.

---

## Measures
quantity_available

inventory_value

stock_movement

---

# FACT_PRODUCTION

## Purpose

Tracks manufacturing activities.

## Grain

One production event.

---

## Measures
units_produced

production_hours

defect_count

---

# FACT_MAINTENANCE

## Purpose

Tracks equipment maintenance.

## Grain

One maintenance event.

---

## Measures
repair_cost

downtime_hours

failure_count

---

# FACT_ENERGY

## Purpose

Supports ESG analytics.

## Grain

One facility-date measurement.

---

## Measures
energy_consumption

carbon_emissions

waste_generated

---

# Schema 4: MARTS

## Purpose

Provides business-specific analytical datasets.

These datasets are optimized for reporting.

---

# Sales Data Mart

Schema:
mart_sales

Includes:

- Customer performance
- Revenue analysis
- Product analytics

---

# Finance Data Mart

Schema:
mart_finance

Includes:

- Revenue
- Expenses
- Profitability

---

# Supply Chain Data Mart

Schema:
mart_supply_chain

Includes:

- Inventory
- Suppliers
- Logistics

---

# Operations Data Mart

Schema:
mart_operations

Includes:

- Production
- Quality
- Maintenance

---

# Data Warehouse Naming Standards

## Tables

Use:
snake_case

Example:
fact_sales_transaction

---

## Columns

Use descriptive names:

Good:
customer_segment

Avoid:
cust_seg

---

## Primary Keys

Format:
<table>_key ```

Examples:
customer_key

product_key

## Foreign Keys

Follow dimension naming:

Example:

customer_key

## Indexing Strategy

Indexes will be created on:
# Primary Keys

Example:

customer_key

# Foreign Keys

Example:

product_key

# Frequently Filtered Columns

Examples:

transaction_date

region

category

# Data Partitioning Strategy

Large fact tables will use partitioning.

Example:

FACT_SALES:

Partition by:

year

Reason:

- Faster historical queries
- Improved maintenance
- Better scalability

## Data Quality Integration

The warehouse will include:
# Validation Tables
Examples:

data_quality_results

etl_error_log

pipeline_execution_log

# Security Design
Security controls:
- Role-based access
- Schema permissions
- Data masking
- Audit logging

---

# Backup Strategy
The platform should maintain:
- Database backups
- Version-controlled scripts
- Recovery procedures

---

# Future Cloud Migration
The architecture supports migration to:
- Azure SQL Database
- Azure Synapse Analytics
- Snowflake
- Databricks Lakehouse

---

# Document Status

Phase:

Phase 1 - Enterprise Data Architecture

Status:

Draft