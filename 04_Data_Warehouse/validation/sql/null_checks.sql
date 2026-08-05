/*
Mandatory Field Validation
*/


SELECT
'CUSTOMER_ID NULLS' AS check_name,
COUNT(*)
FROM warehouse.dim_customer
WHERE customer_id IS NULL;



SELECT
'PRODUCT_ID NULLS',
COUNT(*)
FROM warehouse.dim_product
WHERE product_id IS NULL;



SELECT
'SALES_TRANSACTION_ID NULLS',
COUNT(*)
FROM warehouse.fact_sales
WHERE transaction_id IS NULL;



SELECT
'REVENUE NULLS',
COUNT(*)
FROM warehouse.fact_sales
WHERE revenue IS NULL;