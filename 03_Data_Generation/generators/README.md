# Data Generator Documentation

## Product Generator

File:

generate_products.py


## Purpose

Creates synthetic ERP product master data.


## Output

raw_products.csv


## Dataset Size

Initial:

5,000 products

After quality issues:

~5,100 records


## Data Quality Issues Introduced

- Missing supplier mappings
- Missing categories
- Duplicate products
- Invalid categories
- Negative costs
- Price outliers


## Business Use Cases

Supports:

- Product analytics
- Sales reporting
- Inventory analysis
- Profitability analysis