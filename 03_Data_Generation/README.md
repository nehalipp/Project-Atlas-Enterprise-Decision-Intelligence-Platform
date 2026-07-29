# Project Atlas: Synthetic Data Generation

## Purpose

This module generates realistic enterprise datasets used to simulate an organization's operational environment.

The generated data represents multiple business domains:

- Customer Relationship Management
- Sales
- Supply Chain
- Human Resources
- Manufacturing
- Maintenance
- Sustainability

---

# Objective

The objective is to create realistic analytical datasets containing:

- Valid business records
- Missing values
- Duplicate records
- Data inconsistencies
- Data quality challenges

These datasets will be used for:

- Data cleaning
- Data validation
- ETL development
- Data warehouse loading
- Business intelligence reporting

---

# Technology Stack

## Programming

Python

## Libraries

- Pandas
- NumPy
- Faker

## Output Format

CSV files

## Target Database

PostgreSQL

---

# Generated Domains

## Customer Domain

Dataset:

raw_customers.csv

Contains:

- Customer information
- Industry
- Region
- Segment


## Product Domain

Dataset:

raw_products.csv

Contains:

- Product details
- Categories
- Pricing


## Sales Domain

Dataset:

raw_sales.csv

Contains:

- Transactions
- Revenue
- Discounts


## Supply Chain Domain

Dataset:

raw_inventory.csv

Contains:

- Inventory levels
- Locations


## Workforce Domain

Dataset:

raw_employees.csv

Contains:

- Employees
- Departments
- Roles


## Operations Domain

Dataset:

raw_production.csv

Contains:

- Production events
- Machine performance


## ESG Domain

Dataset:

raw_energy.csv

Contains:

- Energy consumption
- Carbon emissions

---

# Data Quality Challenges

The generated datasets intentionally include:

- NULL values
- Duplicate records
- Invalid categories
- Incorrect formatting
- Outlier values

These issues simulate real-world enterprise data challenges.

---

# Data Generation Workflow
Configuration
|
↓
Python Generators
|
↓
Raw CSV Files
|
↓
Data Quality Issues
|
↓
Raw Enterprise Dataset
