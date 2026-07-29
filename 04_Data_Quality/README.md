# Project Atlas — Data Quality Framework


## Purpose

This module evaluates the quality of enterprise datasets before
loading data into the analytical warehouse.


## Objectives

The framework identifies:

- Missing values
- Duplicate records
- Invalid categories
- Referential integrity issues
- Business rule violations


## Data Quality Dimensions

### Completeness

Measures whether required fields contain values.

Example:

Customer without country information.


---

### Accuracy

Determines whether values are realistic.

Example:

Negative product cost.


---

### Consistency

Ensures standardized values.

Example:

USA, US, United States.


---

### Uniqueness

Identifies duplicate records.

Example:

Duplicate customer IDs.


---

### Validity

Checks whether values follow business rules.

Example:

Quantity cannot be negative.


## Workflow
Raw Data

|

Data Profiling

|

Validation Rules

|

Data Quality Report

|

Clean Data Pipeline


## Tools

Python

- Pandas
- NumPy


SQL

- PostgreSQL validation queries