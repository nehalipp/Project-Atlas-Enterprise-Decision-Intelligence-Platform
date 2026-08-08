/*
==========================================================
Project Atlas

Business Rule Validation

All 16 staging tables

Output:
    validation_type
    table_name
    rule_name
    failed_records
    status

==========================================================
*/


SELECT
    'BUSINESS_RULE' AS validation_type,
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
-- DIMENSIONS
----------------------------------------------------------

SELECT
    'accounts' AS table_name,
    'missing_account_id' AS rule_name,
    COUNT(*) AS failed_records
FROM staging.stg_accounts
WHERE account_id IS NULL


UNION ALL


SELECT
    'customers',
    'missing_customer_id',
    COUNT(*)
FROM staging.stg_customers
WHERE customer_id IS NULL


UNION ALL


SELECT
    'products',
    'negative_unit_price',
    COUNT(*)
FROM staging.stg_products
WHERE unit_price < 0


UNION ALL


SELECT
    'suppliers',
    'missing_supplier_id',
    COUNT(*)
FROM staging.stg_suppliers
WHERE supplier_id IS NULL


UNION ALL


SELECT
    'locations',
    'missing_location_id',
    COUNT(*)
FROM staging.stg_locations
WHERE location_id IS NULL


UNION ALL


SELECT
    'employees',
    'missing_employee_id',
    COUNT(*)
FROM staging.stg_employees
WHERE employee_id IS NULL


UNION ALL


SELECT
    'machines',
    'missing_machine_id',
    COUNT(*)
FROM staging.stg_machines
WHERE machine_id IS NULL



----------------------------------------------------------
-- FACT TABLES
----------------------------------------------------------


UNION ALL


SELECT
    'sales_transactions',
    'negative_quantity',
    COUNT(*)
FROM staging.stg_sales_transactions
WHERE quantity < 0


UNION ALL


SELECT
    'sales_transactions',
    'negative_revenue',
    COUNT(*)
FROM staging.stg_sales_transactions
WHERE revenue < 0


UNION ALL


SELECT
    'production',
    'negative_units_produced',
    COUNT(*)
FROM staging.stg_production
WHERE units_produced < 0


UNION ALL


SELECT
    'maintenance',
    'negative_repair_cost',
    COUNT(*)
FROM staging.stg_maintenance
WHERE repair_cost < 0


UNION ALL


SELECT
    'financial_transactions',
    'negative_amount',
    COUNT(*)
FROM staging.stg_financial_transactions
WHERE amount < 0


UNION ALL


SELECT
    'budget',
    'negative_budget_amount',
    COUNT(*)
FROM staging.stg_budget
WHERE budget_amount < 0


UNION ALL


SELECT
    'energy_consumption',
    'negative_consumption',
    COUNT(*)
FROM staging.stg_energy_consumption
WHERE consumption_kwh < 0


UNION ALL


SELECT
    'emissions',
    'negative_carbon_emission',
    COUNT(*)
FROM staging.stg_emissions
WHERE carbon_emission_tons < 0


UNION ALL


SELECT
    'waste',
    'negative_quantity',
    COUNT(*)
FROM staging.stg_waste
WHERE quantity_tons < 0


UNION ALL


SELECT
    'inventory',
    'negative_inventory_quantity',
    COUNT(*)
FROM staging.stg_inventory
WHERE inventory_quantity < 0


) validation

ORDER BY
    table_name,
    rule_name;