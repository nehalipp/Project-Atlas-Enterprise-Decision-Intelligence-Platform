/*
Project Atlas

Referential Integrity Validation Rules

Purpose:
Ensure transaction data references
valid master data.
*/


-- Sales should reference existing customers

SELECT
    COUNT(*) AS invalid_customer_reference
FROM raw.sales_transactions s
LEFT JOIN raw.customers c
ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL;



-- Sales should reference existing products

SELECT
    COUNT(*) AS invalid_product_reference
FROM raw.sales_transactions s
LEFT JOIN raw.products p
ON s.product_id = p.product_id
WHERE p.product_id IS NULL;



-- Products should reference valid suppliers

SELECT
    COUNT(*) AS invalid_supplier_reference
FROM raw.products p
LEFT JOIN raw.suppliers s
ON p.supplier_id = s.supplier_id
WHERE p.supplier_id IS NOT NULL
AND s.supplier_id IS NULL;