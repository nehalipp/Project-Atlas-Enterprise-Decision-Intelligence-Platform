# Project Atlas: Enterprise Decision Intelligence Platform

# Source System Architecture

## Document Purpose

This document defines the source systems that provide data to Project Atlas.

The objective is to simulate a realistic enterprise environment where data originates from multiple operational systems and must be integrated into a centralized analytics platform.

---

# Enterprise Data Landscape

Modern organizations operate across multiple applications:

- Enterprise Resource Planning (ERP)
- Customer Relationship Management (CRM)
- Human Resources Information Systems (HRIS)
- Supply Chain Management Systems
- Manufacturing Systems
- Internet of Things (IoT) Platforms
- Financial Systems

Project Atlas will integrate data across these domains.

---

# Source System Overview

| Source System | Business Domain | Data Provided |
|---|---|---|
| ERP System | Finance & Operations | Orders, products, suppliers, financial transactions |
| CRM System | Sales & Customer | Customers, opportunities, interactions |
| HRIS System | Workforce | Employees, departments, salaries |
| Supply Chain System | Logistics | Inventory, shipments, suppliers |
| Manufacturing System | Operations | Production, quality, maintenance |
| IoT Platform | Asset Monitoring | Sensor readings, equipment metrics |
| Sustainability System | ESG | Energy consumption, emissions |

---

# 1. ERP System

## Purpose

The ERP system manages core business operations.

## Data Entities

### Products

Attributes:

- Product ID
- Product Name
- Category
- Supplier
- Cost
- Price


### Orders

Attributes:

- Order ID
- Customer ID
- Product ID
- Order Date
- Quantity
- Revenue


### Suppliers

Attributes:

- Supplier ID
- Supplier Name
- Location
- Contract Status


### Financial Transactions

Attributes:

- Transaction ID
- Account
- Amount
- Transaction Date
- Cost Center

---

# 2. CRM System

## Purpose

Manages customer relationships and sales activities.

## Data Entities

### Customers

Attributes:

- Customer ID
- Customer Name
- Industry
- Region
- Customer Segment


### Sales Opportunities

Attributes:

- Opportunity ID
- Customer ID
- Opportunity Stage
- Expected Revenue
- Close Date


### Customer Interactions

Attributes:

- Interaction ID
- Customer ID
- Interaction Type
- Date
- Outcome

---

# 3. HR Information System

## Purpose

Provides workforce analytics data.

## Data Entities

### Employees

Attributes:

- Employee ID
- Department
- Job Role
- Location
- Hire Date


### Employee Events

Attributes:

- Employee ID
- Event Type
- Event Date

Examples:

- Promotion
- Transfer
- Leave
- Termination

---

# 4. Supply Chain System

## Purpose

Provides logistics and inventory visibility.

## Data Entities

### Inventory

Attributes:

- Inventory ID
- Product ID
- Warehouse
- Quantity Available


### Shipments

Attributes:

- Shipment ID
- Supplier ID
- Delivery Date
- Status

---

# 5. Manufacturing System

## Purpose

Tracks operational performance.

## Data Entities

### Production Events

Attributes:

- Production ID
- Machine ID
- Product ID
- Production Date
- Quantity Produced


### Quality Records

Attributes:

- Inspection ID
- Product ID
- Defect Type
- Inspection Result

---

# 6. IoT Platform

## Purpose

Captures equipment performance data.

## Data Entities

### Sensor Measurements

Attributes:

- Sensor ID
- Machine ID
- Timestamp
- Temperature
- Vibration
- Energy Usage

---

# 7. Sustainability System

## Purpose

Tracks ESG performance.

## Data Entities

### Environmental Metrics

Attributes:

- Facility ID
- Date
- Energy Consumption
- Carbon Emissions
- Waste Generated

---

# Data Integration Challenges

Project Atlas intentionally includes realistic enterprise challenges:

## Missing Data

Examples:

- Missing customer industry
- Missing supplier location
- Missing employee department


## Duplicate Records

Examples:

- Duplicate customers
- Duplicate suppliers


## Data Inconsistency

Examples:

Different source values:
USA
US
United States
America

Need standardization:
United States

---

# Data Refresh Frequency

| Source | Refresh Frequency |
|---|---|
| ERP | Daily |
| CRM | Daily |
| HRIS | Weekly |
| Supply Chain | Daily |
| Manufacturing | Near Real-Time |
| IoT | Streaming |
| ESG | Monthly |

---

# Architecture Goal

The purpose of integrating these systems is to create a centralized enterprise analytics environment that supports:

- Executive reporting
- Operational analytics
- Predictive insights
- Business intelligence
- Data-driven decisions

---

# Document Status

Phase:

Phase 1 - Enterprise Data Architecture

Status:

Draft