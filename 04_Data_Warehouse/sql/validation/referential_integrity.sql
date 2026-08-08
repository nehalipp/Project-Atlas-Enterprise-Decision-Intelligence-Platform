/*
==========================================================
Project Atlas

Referential Integrity Validation

Checks warehouse dimension key relationships

Output:
    validation_type
    table_name
    rule_name
    failed_records
    status

==========================================================
*/


SELECT
    'REFERENTIAL_INTEGRITY' AS validation_type,
    table_name,
    rule_name,
    failed_records,
    CASE
        WHEN failed_records = 0
        THEN 'PASS'
        ELSE 'FAIL'
    END AS status

FROM (

----------------------------------------------------------
-- FACT SALES
----------------------------------------------------------

SELECT
    'fact_sales' AS table_name,
    'missing_customer_key' AS rule_name,
    COUNT(*) AS failed_records
FROM warehouse.fact_sales
WHERE customer_key IS NULL


UNION ALL


SELECT
    'fact_sales',
    'missing_product_key',
    COUNT(*)
FROM warehouse.fact_sales
WHERE product_key IS NULL


UNION ALL


SELECT
    'fact_sales',
    'missing_location_key',
    COUNT(*)
FROM warehouse.fact_sales
WHERE location_key IS NULL



----------------------------------------------------------
-- FACT PRODUCTION
----------------------------------------------------------


UNION ALL

SELECT
    'fact_production',
    'missing_machine_key',
    COUNT(*)
FROM warehouse.fact_production
WHERE machine_key IS NULL


UNION ALL


SELECT
    'fact_production',
    'missing_product_key',
    COUNT(*)
FROM warehouse.fact_production
WHERE product_key IS NULL



----------------------------------------------------------
-- FACT MAINTENANCE
----------------------------------------------------------


UNION ALL

SELECT
    'fact_maintenance',
    'missing_machine_key',
    COUNT(*)
FROM warehouse.fact_maintenance
WHERE machine_key IS NULL



----------------------------------------------------------
-- FINANCE
----------------------------------------------------------


UNION ALL

SELECT
    'fact_financial_transactions',
    'missing_account_key',
    COUNT(*)
FROM warehouse.fact_financial_transactions
WHERE account_key IS NULL



----------------------------------------------------------
-- ENERGY
----------------------------------------------------------


UNION ALL

SELECT
    'fact_energy_consumption',
    'missing_location_key',
    COUNT(*)
FROM warehouse.fact_energy_consumption
WHERE location_key IS NULL



----------------------------------------------------------
-- EMISSIONS
----------------------------------------------------------


UNION ALL

SELECT
    'fact_emissions',
    'missing_location_key',
    COUNT(*)
FROM warehouse.fact_emissions
WHERE location_key IS NULL



----------------------------------------------------------
-- WASTE
----------------------------------------------------------


UNION ALL

SELECT
    'fact_waste',
    'missing_location_key',
    COUNT(*)
FROM warehouse.fact_waste
WHERE location_key IS NULL



----------------------------------------------------------
-- INVENTORY
----------------------------------------------------------


UNION ALL

SELECT
    'fact_inventory',
    'missing_product_key',
    COUNT(*)
FROM warehouse.fact_inventory
WHERE product_key IS NULL


UNION ALL


SELECT
    'fact_inventory',
    'missing_location_key',
    COUNT(*)
FROM warehouse.fact_inventory
WHERE location_key IS NULL



) validation

ORDER BY
    table_name,
    rule_name;