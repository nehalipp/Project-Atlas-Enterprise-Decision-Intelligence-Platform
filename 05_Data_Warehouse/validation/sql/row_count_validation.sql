/*
==========================================================
Project Atlas

Validation:
Row Count Checks

Purpose:
Validate record movement across layers
==========================================================
*/


SELECT
'RAW_CUSTOMERS' AS table_name,
COUNT(*) AS record_count
FROM raw.customers

UNION ALL

SELECT
'STAGING_CUSTOMERS',
COUNT(*)
FROM staging.customers_clean

UNION ALL

SELECT
'DIM_CUSTOMER',
COUNT(*)
FROM warehouse.dim_customer;



SELECT
'RAW_PRODUCTS' AS table_name,
COUNT(*) AS record_count
FROM raw.products

UNION ALL

SELECT
'STAGING_PRODUCTS',
COUNT(*)
FROM staging.products_clean

UNION ALL

SELECT
'DIM_PRODUCT',
COUNT(*)
FROM warehouse.dim_product;



SELECT
'RAW_SALES',
COUNT(*)
FROM raw.sales_transactions

UNION ALL

SELECT
'STAGING_SALES',
COUNT(*)
FROM staging.sales_transactions_clean

UNION ALL

SELECT
'FACT_SALES',
COUNT(*)
FROM warehouse.fact_sales;