# Project Atlas - Synthetic Enterprise Data Generation Framework

## Overview

This module generates realistic enterprise-scale synthetic datasets used throughout the Project Atlas Enterprise Decision Intelligence Platform.

The objective is to simulate a real-world organization's data ecosystem across multiple business domains including:

- Customer Management
- Product Management
- Sales Operations
- Supplier Management
- Workforce Management
- Manufacturing Operations
- Finance
- ESG / Sustainability


The generated data intentionally contains realistic data quality issues such as:

- Missing values
- Duplicate records
- Invalid categories
- Outliers
- Data inconsistencies

These issues simulate challenges commonly found in enterprise data environments.


---

# Architecture
02_Data_Generation

├── config
│ └── generation_config.py

├── common
│ ├── faker_utils.py
│ ├── file_utils.py
│ ├── id_generator.py
│ ├── quality.py
│ └── random_utils.py

├── dimensions
│
└── facts



---

# Generated Data Domains


## Dimension Data

Master data entities describing business objects:

| Domain | Dataset |
|---|---|
| Customer | Customer master |
| Product | Product catalog |
| Supplier | Supplier master |
| Location | Enterprise facilities |
| Employee | Workforce master |
| Machine | Manufacturing assets |



## Fact Data

Business transactions and operational events:

| Domain | Dataset |
|---|---|
| Sales | Customer transactions |
| Production | Manufacturing output |
| Maintenance | Asset maintenance history |
| Finance | Financial transactions |
| Budget | Budget planning |
| Energy | Energy consumption |
| Emissions | Carbon emissions |
| Waste | Waste management |


---

# Data Generation Technology

Tools used:

- Python
- Pandas
- NumPy
- Faker
- Randomized synthetic generation


---

# Running the Pipeline

From this directory:
```bash
python3 run_all_generators.py

---

The pipeline generates all datasets and stores outputs inside:

dimensions/<dataset>/output/

facts/<dataset>/output/