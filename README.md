# Project Atlas: Enterprise Decision Intelligence Platform

## Overview

Project Atlas is an end-to-end analytics engineering project designed to transform raw operational sales data into trusted business insights.

The project simulates a real-world enterprise analytics environment where transactional data is generated, cleaned, validated, modeled into a dimensional data warehouse, and analyzed through business intelligence dashboards.

The primary goal is to demonstrate practical skills in:

- Data Engineering
- SQL Development
- Data Warehousing
- Data Quality Management
- Business Intelligence
- Analytics

---

# Business Problem

Organizations often struggle to make timely decisions because business data is distributed across multiple systems, contains quality issues, and requires significant manual preparation before analysis.

Project Atlas addresses this challenge by creating a centralized analytics platform that:

- Consolidates operational sales data
- Improves data reliability through validation
- Creates reusable analytical data models
- Provides business insights through dashboards

---

# Project Objectives

The project focuses on:

## 1. Data Generation

Create realistic synthetic enterprise datasets representing:

- Customers
- Products
- Suppliers
- Locations
- Employees
- Sales Transactions

Technology:

- Python
- Faker
- Pandas

---

## 2. Data Quality Management

Implement automated data quality checks including:

- Missing value detection
- Duplicate identification
- Referential integrity validation
- Business rule validation

Examples:

- Revenue cannot be negative
- Transactions must have valid customers
- Products must map to valid dimensions

---

## 3. Data Warehouse Development

Design and implement a PostgreSQL dimensional data warehouse using a star schema.

Warehouse includes:

### Dimension Tables

- dim_customer
- dim_product
- dim_supplier
- dim_location
- dim_employee
- dim_date

### Fact Tables

- fact_sales

---

## 4. Business Intelligence

Develop analytical dashboards using:

- Power BI
- Tableau

Dashboard areas include:

- Revenue Performance
- Customer Analysis
- Product Performance
- Sales Trends

---

# Architecture

The overall data flow:
Python Faker
(Synthetic Data Generation)

    |

    v

CSV Source Files

    |

    v

PostgreSQL Raw Layer

    |

    v

Staging Layer

(Data Cleaning + Standardization)

    |

    v

Enterprise Data Warehouse

(Star Schema)

    |

    v

Power BI / Tableau

(Business Insights)

---

# Technology Stack

## Data Generation

- Python
- Faker
- Pandas

## Database

- PostgreSQL

## Data Engineering

- SQL
- ETL Pipelines
- Dimensional Modeling

## Data Quality

- Python Validation Scripts
- SQL Validation Rules

## Visualization

- Power BI
- Tableau

## Development Tools

- Git
- GitHub
- VS Code

---

# Dataset Overview

The project uses synthetic enterprise data.

Generated datasets include:

| Dataset | Records |
|---|---:|
| Customers | 50,000+ |
| Products | 5,000+ |
| Suppliers | 1,000+ |
| Locations | 250+ |
| Employees | 10,000+ |
| Sales Transactions | 500,000+ |

---

# Data Warehouse Design

Project Atlas follows dimensional modeling principles.

## Star Schema
                  dim_date
                     |
                     |
dim_customer --- fact_sales --- dim_product
                     |
                     |
                dim_location
                     |
                     |
                dim_supplier
                     |
                     |
                dim_employee

---

# ETL Pipeline

The pipeline follows these steps:

## Step 1: Generate Data

Synthetic enterprise data is created using Python Faker.

---

## Step 2: Load Raw Data

Raw datasets are loaded into PostgreSQL without modification.

Purpose:

- Preserve source data
- Maintain traceability

---

## Step 3: Transform Data

Staging processes perform:

- Data cleaning
- Standardization
- Validation
- Transformation logic

---

## Step 4: Load Warehouse

Cleaned data is loaded into:

- Dimension tables
- Fact tables

---

## Step 5: Validate Warehouse

Automated checks validate:

- Record counts
- Duplicate records
- Missing values
- Referential integrity
- Business rules

---

# Data Quality Results

Validation framework confirms:

- Fact table contains expected transaction volumes
- No duplicate transaction records
- No missing revenue values
- Referential integrity checks passed
- Warehouse revenue reconciles with staging data

---

# Project Structure
Project-Atlas
│
├── data_generation
│
├── data_quality
│
├── data_warehouse
│
├── analytics
│
├── dashboards
│
└── documentation


---

# Key Skills Demonstrated

This project demonstrates:

## Data Engineering

- ETL pipeline development
- Data ingestion
- Data transformation
- Warehouse loading

## SQL Development

- Complex SQL transformations
- Data validation queries
- Dimensional modeling

## Analytics Engineering

- Star schema design
- Fact and dimension modeling
- Data quality frameworks

## Business Intelligence

- KPI development
- Dashboard design
- Business insights

---

# Future Enhancements

Potential future improvements:

- Add additional business domains
- Implement dbt transformations
- Add cloud deployment using Azure
- Introduce automated orchestration
- Add machine learning forecasting models

---

# Project Status

Current Phase:

Completed Core Analytics Platform

Completed:

✅ Synthetic data generation  
✅ Data quality framework  
✅ PostgreSQL warehouse  
✅ Star schema implementation  
✅ ETL pipeline  
✅ Validation framework  
✅ BI dashboards  

---

# Author

Nehali Parulekar

Data Analyst | Business Intelligence | Analytics Engineering