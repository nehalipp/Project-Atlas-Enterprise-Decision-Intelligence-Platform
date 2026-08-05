/*
Project Atlas

Completeness Validation Rules

Purpose:
Identify missing mandatory attributes
before warehouse loading.
*/


-- Customer completeness checks

SELECT
    'customers' AS dataset,
    COUNT(*) AS missing_customer_name
FROM raw.customers
WHERE customer_name IS NULL;



SELECT
    'customers' AS dataset,
    COUNT(*) AS missing_country
FROM raw.customers
WHERE country IS NULL;



-- Product completeness checks


SELECT
    'products' AS dataset,
    COUNT(*) AS missing_supplier
FROM raw.products
WHERE supplier_id IS NULL;



SELECT
    'products' AS dataset,
    COUNT(*) AS missing_category
FROM raw.products
WHERE category IS NULL;



-- Sales completeness checks


SELECT
    'sales_transactions' AS dataset,
    COUNT(*) AS missing_product_reference
FROM raw.sales_transactions
WHERE product_id IS NULL;