# Project Atlas
# Enterprise Data Quality Framework


## Overview


The Data Quality layer is a critical component of the Project Atlas Enterprise Intelligence Platform.

The purpose of this layer is to assess, validate, and document the quality of enterprise datasets before loading them into the analytical data warehouse.


The framework identifies and analyzes issues related to:

- Data completeness
- Data uniqueness
- Referential integrity
- Business rule compliance
- Data accuracy


The objective is to ensure trusted, reliable, and analytics-ready data for downstream reporting and decision-making.


---

# Data Quality Architecture


The Project Atlas data quality framework follows an enterprise-style validation workflow:

## Data Quality Architecture

```text
Raw Enterprise Data
        │
        ▼
Data Profiling
        │
        ▼
Validation Rules
        │
        ▼
Quality Assessment
        │
        ▼
Data Quality Report
        │
        ▼
Enterprise Data Warehouse
```

---

# Folder Structure

```text
04_Data_Quality
│
├── pipeline
│   └── run_data_quality_pipeline.py
│
├── profiling
│   ├── profile_customers.py
│   ├── profile_products.py
│   ├── profile_sales.py
│   └── profile_all_datasets.py
│
├── validation_rules
│   ├── completeness_checks.sql
│   ├── integrity_checks.sql
│   └── business_rules.sql
│
└── reports
    ├── generate_quality_report.py
    └── data_quality_report.md
```

---

# Data Quality Workflow


## Step 1 — Dataset Profiling


The profiling layer evaluates raw datasets and identifies:

- Total record counts
- Unique identifiers
- Duplicate records
- Missing values
- Data distribution issues
- Invalid values


Implemented profiling modules:


### Customer Profiling

File:
profiling/profile_customers.py


Validates:

- Customer record completeness
- Duplicate customers
- Missing demographic attributes


---

### Product Profiling

File:
profiling/profile_products.py


Validates:

- Product uniqueness
- Missing categories
- Missing supplier mappings
- Invalid costs
- Pricing anomalies


---

### Sales Profiling

File:
profiling/profile_sales.py


Validates:

- Transaction uniqueness
- Missing product references
- Invalid quantities
- Revenue calculation accuracy


---

# Step 2 — Data Validation Rules


SQL-based validation rules are designed to simulate enterprise data governance checks before warehouse ingestion.


## Completeness Checks


File:
validation_rules/completeness_checks.sql


Purpose:

Identify missing mandatory attributes across datasets.


Examples:

- Missing customer country
- Missing product category
- Missing supplier mappings
- Missing sales product references



---

## Integrity Checks


File:
validation_rules/integrity_checks.sql


Purpose:

Validate relationships between datasets.


Examples:

- Sales transactions referencing invalid customers
- Sales transactions referencing missing products
- Invalid supplier relationships



---

## Business Rule Validation


File:
validation_rules/business_rules.sql


Purpose:

Validate domain-specific business logic.


Examples:


Quantity validation:
quantity > 0


Revenue validation:
revenue =
quantity × unit_price × (1 - discount_percentage)


Discount validation:
0 <= discount_percentage <= 100


---

# Step 3 — Automated Data Quality Pipeline


The pipeline orchestrates the complete data quality workflow.


## Execution

Navigate to the pipeline directory:

```bash
cd 04_Data_Quality/pipeline
```

Run the pipeline:

```bash
python run_data_quality_pipeline.py
```

The pipeline automatically performs the following tasks:

1. Profiles all enterprise datasets
2. Executes data quality validation rules
3. Aggregates profiling results
4. Generates the enterprise data quality report

## Generated Outputs

Successful execution generates:

```text
reports/data_quality_report.md
```

The report includes:

- Executive Summary
- Dataset-Level Assessment
- Missing Value Analysis
- Duplicate Record Analysis
- Business Rule Validation
- Data Quality Dimensions
- Business Impact Assessment
- Recommended Remediation Actions

## Data Quality Dimensions

| Dimension | Description |
|------------|-------------|
| Completeness | Identifies missing mandatory attributes |
| Uniqueness | Detects duplicate records |
| Referential Integrity | Validates relationships between datasets |
| Validity | Ensures records comply with business rules |
| Accuracy | Confirms calculated metrics are correct |

## Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Data Generation | Faker |
| Validation Rules | SQL |
| Documentation | Markdown |
| Version Control | Git & GitHub |

## Future Enhancements

Planned improvements include:

- Automated data quality scoring
- Historical quality trend analysis
- Interactive Power BI data quality dashboard
- Data observability metrics
- Automated alerting for validation failures
- Integration with ETL pipelines and CI/CD workflows

## Summary

The Data Quality Framework ensures that enterprise datasets are validated before they enter the analytical warehouse. By combining automated profiling, SQL-based validation, and standardized reporting, Project Atlas establishes a reliable foundation for business intelligence, analytics, and executive decision-making.