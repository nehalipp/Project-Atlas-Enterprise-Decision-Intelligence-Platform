/*
==========================================================
Project Atlas

Duplicate Record Validation

Checks all 16 staging tables

Output:
    validation_type
    table_name
    rule_name
    failed_records
    status

==========================================================
*/


SELECT
    'DUPLICATE_VALIDATION' AS validation_type,
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
    'duplicate_account_id' AS rule_name,
    COUNT(*) AS failed_records
FROM (
    SELECT
        account_id,
        COUNT(*) cnt
    FROM staging.stg_accounts
    GROUP BY account_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'customers',
    'duplicate_customer_id',
    COUNT(*)
FROM (
    SELECT
        customer_id
    FROM staging.stg_customers
    GROUP BY customer_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'products',
    'duplicate_product_id',
    COUNT(*)
FROM (
    SELECT
        product_id
    FROM staging.stg_products
    GROUP BY product_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'suppliers',
    'duplicate_supplier_id',
    COUNT(*)
FROM (
    SELECT
        supplier_id
    FROM staging.stg_suppliers
    GROUP BY supplier_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'locations',
    'duplicate_location_id',
    COUNT(*)
FROM (
    SELECT
        location_id
    FROM staging.stg_locations
    GROUP BY location_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'employees',
    'duplicate_employee_id',
    COUNT(*)
FROM (
    SELECT
        employee_id
    FROM staging.stg_employees
    GROUP BY employee_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'machines',
    'duplicate_machine_id',
    COUNT(*)
FROM (
    SELECT
        machine_id
    FROM staging.stg_machines
    GROUP BY machine_id
    HAVING COUNT(*) > 1
) x



----------------------------------------------------------
-- FACT TABLES
----------------------------------------------------------


UNION ALL


SELECT
    'sales_transactions',
    'duplicate_transaction_id',
    COUNT(*)
FROM (
    SELECT
        transaction_id
    FROM staging.stg_sales_transactions
    GROUP BY transaction_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'production',
    'duplicate_production_id',
    COUNT(*)
FROM (
    SELECT
        production_id
    FROM staging.stg_production
    GROUP BY production_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'maintenance',
    'duplicate_maintenance_id',
    COUNT(*)
FROM (
    SELECT
        maintenance_id
    FROM staging.stg_maintenance
    GROUP BY maintenance_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'financial_transactions',
    'duplicate_transaction_id',
    COUNT(*)
FROM (
    SELECT
        transaction_id
    FROM staging.stg_financial_transactions
    GROUP BY transaction_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'budget',
    'duplicate_budget_id',
    COUNT(*)
FROM (
    SELECT
        budget_id
    FROM staging.stg_budget
    GROUP BY budget_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'energy_consumption',
    'duplicate_energy_id',
    COUNT(*)
FROM (
    SELECT
        energy_id
    FROM staging.stg_energy_consumption
    GROUP BY energy_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'emissions',
    'duplicate_emission_id',
    COUNT(*)
FROM (
    SELECT
        emission_id
    FROM staging.stg_emissions
    GROUP BY emission_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'waste',
    'duplicate_waste_id',
    COUNT(*)
FROM (
    SELECT
        waste_id
    FROM staging.stg_waste
    GROUP BY waste_id
    HAVING COUNT(*) > 1
) x


UNION ALL


SELECT
    'inventory',
    'duplicate_inventory_id',
    COUNT(*)
FROM (
    SELECT
        inventory_id
    FROM staging.stg_inventory
    GROUP BY inventory_id
    HAVING COUNT(*) > 1
) x


) validation

ORDER BY
    table_name,
    rule_name;