# Project Atlas: Enterprise Decision Intelligence Platform

# Data Dictionary

## Document Purpose

This document defines the metadata standards for Project Atlas analytical datasets.

The purpose of this document is to provide a centralized reference for:

- Table definitions
- Column descriptions
- Business meanings
- Data types
- Source systems
- Transformation rules

The data dictionary ensures consistency between business stakeholders, analysts, engineers, and reporting teams.

---

# Metadata Standards

Each dataset definition includes:

| Attribute | Description |
|---|---|
| Table Name | Physical database table |
| Business Purpose | Why the table exists |
| Grain | Level of detail represented |
| Source System | Origin of data |
| Column Name | Field name |
| Data Type | Storage format |
| Business Definition | Meaning of field |
| Transformation Rule | Processing logic |

---

# Dimension Tables

---

# dim_date

## Business Purpose

Provides standardized calendar information for all analytical reporting.

## Grain

One record per calendar date.

## Source System

Generated internally.

---

| Column | Data Type | Description |
|---|---|---|
| date_key | Integer | Surrogate date identifier |
| full_date | Date | Calendar date |
| day_number | Integer | Day of month |
| month_number | Integer | Month number |
| month_name | Varchar | Month description |
| quarter | Varchar | Calendar quarter |
| year | Integer | Calendar year |
| fiscal_period | Varchar | Financial reporting period |

---

# dim_customer

## Business Purpose

Stores customer master information for customer analytics.

## Grain

One record per customer version.

## Source System

CRM System.

---

| Column | Data Type | Description |
|---|---|---|
| customer_key | Integer | Warehouse surrogate key |
| customer_id | Varchar | Source customer identifier |
| customer_name | Varchar | Customer organization name |
| industry | Varchar | Customer industry classification |
| segment | Varchar | Customer business segment |
| country | Varchar | Customer country |
| region | Varchar | Geographic region |
| effective_date | Date | Start date of record validity |
| expiration_date | Date | End date of record validity |
| active_flag | Boolean | Current record indicator |

---

# dim_product

## Business Purpose

Stores product master information.

## Grain

One record per product.

## Source System

ERP System.

---

| Column | Data Type | Description |
|---|---|---|
| product_key | Integer | Warehouse surrogate key |
| product_id | Varchar | Source product identifier |
| product_name | Varchar | Product description |
| category | Varchar | Product category |
| supplier_key | Integer | Related supplier |
| unit_cost | Decimal | Product cost |
| unit_price | Decimal | Selling price |

---

# dim_supplier

## Business Purpose

Stores supplier information.

## Source System

ERP / Procurement System.

---

| Column | Data Type | Description |
|---|---|---|
| supplier_key | Integer | Warehouse key |
| supplier_id | Varchar | Source supplier identifier |
| supplier_name | Varchar | Supplier name |
| country | Varchar | Supplier location |
| supplier_category | Varchar | Supplier classification |
| performance_rating | Decimal | Supplier quality score |

---

# dim_employee

## Business Purpose

Supports workforce analytics.

## Source System

HR Information System.

---

| Column | Data Type | Description |
|---|---|---|
| employee_key | Integer | Warehouse key |
| employee_id | Varchar | Employee identifier |
| department | Varchar | Organizational department |
| job_title | Varchar | Employee role |
| location | Varchar | Work location |
| hire_date | Date | Employment start date |
| employment_status | Varchar | Active/inactive status |

---

# dim_location

## Business Purpose

Supports geographic analysis.

## Source System

ERP / Operations System.

---

| Column | Data Type | Description |
|---|---|---|
| location_key | Integer | Warehouse key |
| facility_name | Varchar | Facility name |
| city | Varchar | City |
| country | Varchar | Country |
| region | Varchar | Geographic region |

---

# dim_machine

## Business Purpose

Supports equipment analytics.

## Source System

Manufacturing System.

---

| Column | Data Type | Description |
|---|---|---|
| machine_key | Integer | Warehouse key |
| machine_id | Varchar | Source machine identifier |
| machine_type | Varchar | Equipment category |
| facility | Varchar | Operating location |
| installation_date | Date | Installation date |

---

# Fact Tables

---

# fact_sales

## Business Purpose

Stores customer sales transactions.

## Grain

One row per product transaction.

## Source System

ERP / Sales System.

---

| Column | Data Type | Description |
|---|---|---|
| sales_key | Integer | Transaction identifier |
| date_key | Integer | Transaction date |
| customer_key | Integer | Customer reference |
| product_key | Integer | Product reference |
| location_key | Integer | Sales location |
| quantity_sold | Integer | Number of units sold |
| unit_price | Decimal | Selling price |
| discount_amount | Decimal | Applied discount |
| sales_amount | Decimal | Total revenue |

---

# fact_finance

## Business Purpose

Stores financial transactions.

## Grain

One financial transaction.

---

| Column | Data Type | Description |
|---|---|---|
| finance_key | Integer | Transaction identifier |
| date_key | Integer | Transaction date |
| location_key | Integer | Business location |
| revenue_amount | Decimal | Revenue value |
| expense_amount | Decimal | Expense value |
| profit_amount | Decimal | Calculated profit |
| budget_amount | Decimal | Planned budget |

---

# fact_inventory

## Business Purpose

Tracks inventory levels and movement.

## Grain

One product-location-date snapshot.

---

| Column | Data Type | Description |
|---|---|---|
| inventory_key | Integer | Inventory identifier |
| date_key | Integer | Snapshot date |
| product_key | Integer | Product reference |
| location_key | Integer | Warehouse location |
| quantity_available | Integer | Available stock |
| inventory_value | Decimal | Inventory financial value |

---

# fact_production

## Business Purpose

Tracks manufacturing performance.

## Grain

One production event.

---

| Column | Data Type | Description |
|---|---|---|
| production_key | Integer | Production event identifier |
| date_key | Integer | Production date |
| machine_key | Integer | Equipment reference |
| product_key | Integer | Manufactured product |
| units_produced | Integer | Production quantity |
| production_hours | Decimal | Production duration |
| defect_count | Integer | Number of defects |

---

# fact_maintenance

## Business Purpose

Tracks equipment maintenance events.

## Grain

One maintenance event.

---

| Column | Data Type | Description |
|---|---|---|
| maintenance_key | Integer | Maintenance identifier |
| date_key | Integer | Maintenance date |
| machine_key | Integer | Equipment reference |
| repair_cost | Decimal | Repair expense |
| downtime_hours | Decimal | Equipment downtime |
| failure_count | Integer | Failure occurrence |

---

# fact_energy_consumption

## Business Purpose

Supports ESG and sustainability analytics.

## Grain

One facility-date measurement.

---

| Column | Data Type | Description |
|---|---|---|
| energy_key | Integer | Measurement identifier |
| date_key | Integer | Measurement date |
| location_key | Integer | Facility reference |
| energy_consumption | Decimal | Energy usage |
| carbon_emissions | Decimal | Carbon output |
| waste_generated | Decimal | Waste quantity |

---

# Data Quality Rules

## Customer Data

Rules:

- Customer ID cannot be null
- Customer name cannot be empty
- Country must use standardized values


---

## Sales Data

Rules:

- Quantity sold must be greater than zero
- Revenue cannot be negative
- Product must exist in product dimension


---

## Inventory Data

Rules:

- Inventory quantity cannot be negative
- Product must have valid reference


---

## Employee Data

Rules:

- Employee ID required
- Department must be populated


---

# Data Governance Ownership

| Data Domain | Owner |
|---|---|
| Customer | CRM Team |
| Finance | Finance Department |
| Products | Product Management |
| Suppliers | Procurement |
| Employees | HR |
| Operations | Operations Team |
| ESG | Sustainability Team |

---

# Document Status

Phase:

Phase 1 - Enterprise Data Architecture

Status:

Draft