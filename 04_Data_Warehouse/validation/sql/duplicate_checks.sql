/*
Duplicate Business Key Checks
*/


-- Customers

SELECT
customer_id,
COUNT(*)
FROM warehouse.dim_customer
GROUP BY customer_id
HAVING COUNT(*) > 1;



-- Products

SELECT
product_id,
COUNT(*)
FROM warehouse.dim_product
GROUP BY product_id
HAVING COUNT(*) > 1;



-- Suppliers

SELECT
supplier_id,
COUNT(*)
FROM warehouse.dim_supplier
GROUP BY supplier_id
HAVING COUNT(*) > 1;



-- Sales Transactions

SELECT
transaction_id,
COUNT(*)
FROM warehouse.fact_sales
GROUP BY transaction_id
HAVING COUNT(*) > 1;