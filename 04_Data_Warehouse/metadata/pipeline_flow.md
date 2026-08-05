# Project Atlas Pipeline Flow


## Source

Synthetic operational data generated using Python Faker.


## Layers


### RAW Layer

Purpose:
Landing zone.

Characteristics:
- No transformations
- Preserves source data
- Adds ingestion metadata


### STAGING Layer

Purpose:
Data cleansing.

Processes:
- Duplicate removal
- Null handling
- Standardization
- Business rule validation


### WAREHOUSE Layer

Purpose:
Analytics model.

Architecture:
Star Schema


Dimensions:

- dim_customer
- dim_product
- dim_supplier
- dim_location
- dim_employee
- dim_date


Fact:

- fact_sales