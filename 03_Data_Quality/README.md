# Project Atlas: Enterprise Decision Intelligence Platform

# 03_Data_Quality - Data Quality Framework

## Overview

The **Data Quality Framework** is the third layer of the Project Atlas Enterprise Decision Intelligence Platform.

This module validates and measures the quality of synthetic enterprise datasets generated in the `02_Data_Generation` layer.

The objective is to simulate a real-world enterprise data governance process where raw operational data is evaluated before being loaded into a data warehouse.

The framework performs:

* Dataset profiling
* Data completeness checks
* Duplicate detection
* Data consistency validation
* Business rule validation
* Data quality scoring
* Automated quality reporting

---

# Data Quality Architecture

The overall Project Atlas data flow:

```
02_Data_Generation
        |
        |
        v
03_Data_Quality
        |
        |
        +----------------+
        |                |
        v                v
   Profiling        Validation
        |                |
        +----------------+
                 |
                 v
          Quality Reporting
                 |
                 |
                 v
        04_Data_Warehouse
```

---

# Folder Structure

```
03_Data_Quality
│
├── config
│   └── quality_config.py
│
├── profiling
│   │
│   ├── profiler.py
│   ├── profile_all_datasets.py
│   │
│   └── output
│       └── profiles
│
├── validation
│   │
│   ├── validate_all.py
│   │
│   ├── validators
│   │   ├── dimension_validator.py
│   │   ├── fact_validator.py
│   │   └── business_rules.py
│   │
│   └── output
│       └── validation_results.json
│
├── reports
│   │
│   ├── generate_quality_report.py
│   ├── generate_quality_scorecard.py
│   │
│   └── output
│       ├── quality_summary.csv
│       ├── data_quality_report.md
│       └── data_quality_scorecard.xlsx
│
├── run_quality_pipeline.py
│
└── README.md
```

---

# Input Data Sources

The framework validates datasets generated from:

```
02_Data_Generation
```

The following datasets are analyzed.

---

# Dimension Datasets

| Dataset   | Source File       |
| --------- | ----------------- |
| Accounts  | raw_accounts.csv  |
| Customers | raw_customers.csv |
| Employees | raw_employees.csv |
| Locations | raw_locations.csv |
| Machines  | raw_machines.csv  |
| Products  | raw_products.csv  |
| Suppliers | raw_suppliers.csv |

---

# Fact Datasets

| Dataset                | Source File                    |
| ---------------------- | ------------------------------ |
| Sales                  | raw_sales_transactions.csv     |
| Inventory              | raw_inventory.csv              |
| Production             | raw_production.csv             |
| Maintenance            | raw_maintenance.csv            |
| Financial Transactions | raw_financial_transactions.csv |
| Budget                 | raw_budget.csv                 |
| Energy Consumption     | raw_energy_consumption.csv     |
| Emissions              | raw_emissions.csv              |
| Waste Management       | raw_waste.csv                  |

---

# Data Quality Framework Components

## 1. Dataset Profiling

Location:

```
profiling/
```

The profiling engine analyzes every dataset and generates metadata.

Metrics captured:

* Dataset row count
* Column count
* Data types
* Missing values
* Missing percentage
* Duplicate records
* Unique values
* Quality score

Example:

```
Dataset:
customers

Rows:
51000

Columns:
7

Missing Percentage:
5%

Duplicate Percentage:
2%

Quality Score:
93%
```

---

# 2. Validation Framework

Location:

```
validation/
```

The validation framework performs automated checks.

---

## Dimension Validation

Checks include:

### Primary Key Completeness

Example:

```
customer_id cannot contain NULL values
```

### Duplicate Key Detection

Example:

```
Duplicate customer_id records detected
```

### Reference Integrity

Example:

```
product_id must be unique
```

---

## Fact Validation

Checks include:

### Sales Validation

Examples:

```
Quantity cannot be negative

Revenue = Quantity × Unit Price
```

---

### Inventory Validation

Examples:

```
Inventory quantity cannot be negative
```

---

### Manufacturing Validation

Examples:

```
Production quantity cannot be negative
```

---

### ESG Validation

Examples:

```
Energy consumption cannot be negative

Carbon emissions cannot be negative

Waste quantity cannot be negative
```

---

# 3. Business Rule Engine

Location:

```
validation/validators/business_rules.py
```

Contains domain-specific validation logic.

Supported domains:

* Sales
* Inventory
* Manufacturing
* ESG

This layer simulates enterprise data governance rules.

---

# 4. Data Quality Reporting

Location:

```
reports/
```

The reporting layer converts technical validation results into business-friendly outputs.

Generated reports:

---

## CSV Quality Summary

File:

```
quality_summary.csv
```

Contains:

* Dataset name
* Row count
* Column count
* Missing percentage
* Duplicate percentage
* Quality score
* Validation status

---

## Markdown Data Quality Report

File:

```
data_quality_report.md
```

Provides:

* Dataset health summary
* Overall quality statistics
* Datasets requiring attention

---

## Excel Data Quality Scorecard

File:

```
data_quality_scorecard.xlsx
```

Contains:

### Sheet 1: Quality Scorecard

Dataset-level quality ranking.

### Sheet 2: Summary

Executive metrics:

* Total datasets analyzed
* Average quality score
* Failed validations
* Passed validations

---

# Running the Pipeline

From:

```
03_Data_Quality
```

execute:

```bash
python3 run_quality_pipeline.py
```

---

# Pipeline Execution Flow

The pipeline executes:

```
START

 |
 |
 v

Dataset Profiling

 |
 |
 v

Data Validation

 |
 |
 v

Quality Report Generation

 |
 |
 v

Excel Scorecard Generation

 |
 |
 v

END
```

---

# Example Pipeline Output

```
PROJECT ATLAS DATA QUALITY PIPELINE


STARTING: DATASET PROFILING

SUCCESS: customers
SUCCESS: products
SUCCESS: sales


COMPLETED: DATASET PROFILING



STARTING: DATA VALIDATION

customers completed
sales completed


COMPLETED: DATA VALIDATION



STARTING: QUALITY REPORT GENERATION

Created data_quality_report.md


STARTING: QUALITY SCORECARD GENERATION

Created data_quality_scorecard.xlsx


DATA QUALITY PIPELINE COMPLETED
```

---

# Technology Stack

| Component              | Technology                |
| ---------------------- | ------------------------- |
| Programming Language   | Python                    |
| Data Processing        | Pandas                    |
| Numerical Processing   | NumPy                     |
| Reporting              | Markdown, Excel           |
| Excel Engine           | OpenPyXL                  |
| Data Generation Source | Synthetic Enterprise Data |
| Version Control        | GitHub                    |

---

# Design Principles

This framework follows enterprise data engineering practices:

## Automation First

All profiling and validation processes are executed through reusable Python pipelines.

---

## Configuration Driven

Dataset rules and quality thresholds are maintained separately from processing logic.

---

## Scalable Architecture

New datasets can be added by:

1. Adding dataset metadata
2. Creating validation rules
3. Registering the dataset

without redesigning the framework.

---

## Data Governance Ready

The framework supports concepts used in enterprise environments:

* Data quality monitoring
* Data stewardship
* Data governance
* Data validation
* Data observability

---

# Future Enhancements

Planned improvements:

* Data quality dashboard using Power BI
* Automated anomaly detection
* Data lineage tracking
* Great Expectations integration
* Data drift monitoring
* Historical quality trend analysis
* Data catalog integration

---

# Project Progress

Current completed layers:

| Layer               | Status    |
| ------------------- | --------- |
| 01_Project Planning | Completed |
| 02_Data Generation  | Completed |
| 03_Data Quality     | Completed |
| 04_Data Warehouse   | Next      |
| 05_Analytics & BI   | Planned   |

---

# Author

Project Atlas: Enterprise Decision Intelligence Platform

Built as an end-to-end analytics engineering portfolio project demonstrating:

* Data Engineering
* Business Intelligence
* Data Quality Management
* Enterprise Analytics Architecture
* Decision Intelligence
