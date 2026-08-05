/*
Project Atlas

Business Rule Validation Checks

Purpose:
Validate enterprise business rules
before analytical processing.
*/


-- Quantity cannot be zero or negative

SELECT
    COUNT(*) AS invalid_quantity_records
FROM raw.sales_transactions
WHERE quantity <= 0;



-- Discount must be between 0 and 100

SELECT
    COUNT(*) AS invalid_discount_records
FROM raw.sales_transactions
WHERE discount_percentage < 0
OR discount_percentage > 100;



-- Revenue calculation validation

SELECT
    COUNT(*) AS revenue_mismatch_records
FROM raw.sales_transactions
WHERE ABS(
    revenue -
    (
        quantity *
        unit_price *
        (1 - discount_percentage / 100)
    )
) > 0.01;



-- Product cost validation

SELECT
    COUNT(*) AS invalid_product_costs
FROM raw.products
WHERE unit_cost <= 0;