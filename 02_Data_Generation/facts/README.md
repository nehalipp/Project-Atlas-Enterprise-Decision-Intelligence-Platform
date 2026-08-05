
---

# `02_Data_Generation/facts/README.md`

```markdown
# Project Atlas - Fact Data Generation

## Overview

This folder contains synthetic transactional and operational fact data generators for the Project Atlas Enterprise Decision Intelligence Platform.

Fact datasets represent measurable business events and operational activities.

These datasets simulate enterprise processes across:

- Sales
- Manufacturing
- Finance
- Sustainability
- Operations


The generated fact data will be transformed and loaded into analytical fact tables within the enterprise data warehouse.


---

# Fact Data Architecture
facts

├── budgets
├── emissions
├── energy
├── maintenance
├── production
├── sales
└── transactions



---

# Generated Fact Datasets


## 1. Sales Transactions Fact

Location:


sales/output/raw_sales_transactions.csv


Purpose:

Captures customer sales activity and revenue transactions.


Measures:

- Quantity
- Unit price
- Discount
- Revenue


Key Attributes:

- transaction_id
- customer_id
- product_id
- location_id
- sales_channel
- transaction_date


Business Use Cases:

- Revenue analysis
- Sales trends
- Customer profitability
- Product performance



---

## 2. Production Fact

Location:


production/output/raw_production.csv


Purpose:

Captures manufacturing production activities.


Measures:

- Production quantity
- Production time
- Production status


Business Use Cases:

- Manufacturing efficiency
- Production planning
- Operational performance
- Capacity analysis



---

## 3. Maintenance Fact

Location:


maintenance/output/raw_maintenance.csv


Purpose:

Tracks manufacturing equipment maintenance activities.


Measures:

- Maintenance duration
- Downtime
- Maintenance cost


Business Use Cases:

- Asset reliability
- Preventive maintenance analysis
- Downtime reduction
- Equipment optimization



---

## 4. Financial Transactions Fact

Location:


transactions/output/raw_financial_transactions.csv


Purpose:

Captures financial activities across business operations.


Measures:

- Transaction amount
- Account impact
- Financial category


Business Use Cases:

- Financial reporting
- Expense analysis
- Revenue tracking
- Cost management



---

## 5. Budget Fact

Location:


budgets/output/raw_budget.csv


Purpose:

Stores organizational budget planning information.


Measures:

- Planned budget
- Actual spending
- Variance


Business Use Cases:

- Budget vs actual analysis
- Department planning
- Financial forecasting



---

# ESG Fact Datasets


## 6. Energy Consumption Fact

Location:


energy/output/raw_energy_consumption.csv



Purpose:

Tracks enterprise energy usage.


Measures:

- Energy consumption
- Energy source
- Facility usage


Business Use Cases:

- Energy optimization
- Sustainability reporting
- Operational efficiency



---

## 7. Carbon Emissions Fact

Location:


emissions/output/raw_emissions.csv



Purpose:

Tracks greenhouse gas emissions.


Measures:

- Emission quantity
- Emission type
- Emission scope


Business Use Cases:

- ESG reporting
- Carbon footprint analysis
- Sustainability initiatives



---

## 8. Waste Management Fact

Location:


waste/output/raw_waste.csv



Purpose:

Tracks waste generation and disposal activities.


Measures:

- Waste quantity
- Waste category
- Disposal method


Business Use Cases:

- Waste reduction
- Environmental compliance
- ESG reporting



---

# Data Quality Simulation

Fact datasets include realistic enterprise data issues:

| Issue | Purpose |
|---|---|
| Missing values | Simulates incomplete transactions |
| Duplicate records | Tests duplicate detection |
| Outliers | Tests anomaly detection |
| Invalid records | Tests business validation rules |


---

# Warehouse Mapping

Fact datasets become analytical fact tables:


fact_sales

fact_production

fact_maintenance

fact_finance

fact_budget

fact_energy

fact_emissions

fact_waste



---

# Technology Used

- Python
- Pandas
- NumPy
- Faker
- Synthetic enterprise modeling


---

# Execution

Generate individual fact datasets:

Example:

```bash
python3 sales/generate_sales.py
```

Generate all datasets:

```bash
python3 ../run_all_generators.py
```