# Project Atlas - Dimension Data Generation

## Overview

This folder contains synthetic dimension data generators for the Project Atlas Enterprise Decision Intelligence Platform.

Dimension datasets represent core business entities and master data objects that provide descriptive context for analytical reporting.

These datasets are designed to simulate enterprise master data commonly found in organizations across manufacturing, logistics, finance, technology, and sustainability domains.

The generated dimension data will later be loaded into the enterprise data warehouse as dimension tables using a star schema architecture.


---

# Dimension Data Architecture
dimensions

├── customers
├── employees
├── locations
├── machines
├── products
└── suppliers


---

# Generated Dimension Datasets


## 1. Customer Dimension

Location:
customers/output/raw_customers.csv


Purpose:

Stores enterprise customer master information used for customer analytics, segmentation, and revenue analysis.


Key Attributes:

- customer_id
- customer_name
- industry
- customer_segment
- country
- region
- customer_since


Business Use Cases:

- Customer segmentation
- Revenue by customer group
- Industry analysis
- Customer lifecycle analysis



---

## 2. Product Dimension

Location:
products/output/raw_products.csv


Purpose:

Stores product catalog information used for product performance and profitability analysis.


Key Attributes:

- product_id
- product_name
- category
- supplier_id
- unit_cost
- unit_price
- product_status


Business Use Cases:

- Product profitability
- Category performance
- Pricing analysis
- Product lifecycle management



---

## 3. Supplier Dimension

Location:


suppliers/output/raw_suppliers.csv


Purpose:

Stores supplier master information used for procurement and supply chain analytics.


Key Attributes:

- supplier_id
- supplier_name
- supplier_category
- country
- region
- performance_rating
- supplier_status


Business Use Cases:

- Supplier performance analysis
- Procurement optimization
- Supplier risk assessment
- Vendor segmentation



---

## 4. Location Dimension

Location:


locations/output/raw_locations.csv


Purpose:

Stores enterprise facility and geographic information.


Represents:

- Manufacturing plants
- Warehouses
- Distribution centers
- Corporate offices
- Research facilities


Key Attributes:

- location_id
- facility_name
- location_type
- city
- state
- country
- region
- latitude
- longitude
- operating_status


Business Use Cases:

- Regional performance analysis
- Facility optimization
- Geographic reporting
- Supply chain analytics



---

## 5. Employee Dimension

Location:


employees/output/raw_employees.csv


Purpose:

Stores workforce master data for HR and operational analytics.


Key Attributes:

- employee_id
- employee_name
- department
- job_title
- location_id
- hire_date
- employment_status


Business Use Cases:

- Workforce analytics
- Department analysis
- Employee distribution
- Workforce planning



---

## 6. Machine Dimension

Location:


machines/output/raw_machines.csv


Purpose:

Stores manufacturing equipment master data.


Key Attributes:

- machine_id
- machine_type
- manufacturer
- location_id
- installation_date
- machine_status


Business Use Cases:

- Asset utilization
- Manufacturing performance
- Maintenance planning
- Equipment lifecycle analysis



---

# Data Quality Simulation

Dimension datasets intentionally include realistic enterprise data quality challenges:

| Issue | Purpose |
|---|---|
| Missing values | Simulates incomplete master data |
| Duplicate records | Tests deduplication workflows |
| Invalid categories | Tests validation processes |
| Data inconsistencies | Represents real enterprise issues |


---

# Warehouse Mapping

These datasets become dimension tables in the enterprise data warehouse:


dim_customer

dim_product

dim_supplier

dim_location

dim_employee

dim_machine



---

# Technology Used

- Python
- Pandas
- NumPy
- Faker
- Synthetic data generation techniques


---

# Execution

Generate individual dimension datasets:

Example:

```bash
python3 customers/generate_customers.py

Generate all datasets:

python3 ../run_all_generators.py