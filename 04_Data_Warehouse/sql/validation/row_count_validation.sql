/*
==========================================================
Project Atlas

Row Count Validation

Validates:

Raw Layer
      |
      ↓
Staging Layer
      |
      ↓
Warehouse Layer


Purpose:
    Confirm ETL record movement and reconciliation.

==========================================================
*/


SELECT

    'ROW_COUNT' AS validation_type,

    table_name,

    raw_count,

    staging_count,

    warehouse_count,

    raw_count - staging_count AS raw_to_staging_difference,

    staging_count - warehouse_count AS staging_to_warehouse_difference,

    CASE
        WHEN staging_count <= raw_count
        AND warehouse_count = staging_count
        THEN 'PASS'
        ELSE 'FAIL'
    END AS status


FROM (

SELECT
    'accounts' AS table_name,
    (SELECT COUNT(*) FROM raw.accounts),
    (SELECT COUNT(*) FROM staging.stg_accounts),
    (SELECT COUNT(*) FROM warehouse.dim_account)


UNION ALL


SELECT
    'customers',
    (SELECT COUNT(*) FROM raw.customers),
    (SELECT COUNT(*) FROM staging.stg_customers),
    (
        SELECT COUNT(*)
        FROM warehouse.dim_customer
        WHERE customer_id <> 'UNKNOWN'
    )


UNION ALL


SELECT
    'products',
    (SELECT COUNT(*) FROM raw.products),
    (SELECT COUNT(*) FROM staging.stg_products),
    (SELECT COUNT(*) FROM warehouse.dim_product)


UNION ALL


SELECT
    'suppliers',
    (SELECT COUNT(*) FROM raw.suppliers),
    (SELECT COUNT(*) FROM staging.stg_suppliers),
    (SELECT COUNT(*) FROM warehouse.dim_supplier)


UNION ALL


SELECT
    'locations',
    (SELECT COUNT(*) FROM raw.locations),
    (SELECT COUNT(*) FROM staging.stg_locations),
    (SELECT COUNT(*) FROM warehouse.dim_location)


UNION ALL


SELECT
    'employees',
    (SELECT COUNT(*) FROM raw.employees),
    (SELECT COUNT(*) FROM staging.stg_employees),
    (SELECT COUNT(*) FROM warehouse.dim_employee)


UNION ALL


SELECT
    'machines',
    (SELECT COUNT(*) FROM raw.machines),
    (SELECT COUNT(*) FROM staging.stg_machines),
    (SELECT COUNT(*) FROM warehouse.dim_machine)


UNION ALL


SELECT
    'sales_transactions',
    (SELECT COUNT(*) FROM raw.sales_transactions),
    (SELECT COUNT(*) FROM staging.stg_sales_transactions),
    (SELECT COUNT(*) FROM warehouse.fact_sales)


UNION ALL


SELECT
    'production',
    (SELECT COUNT(*) FROM raw.production),
    (SELECT COUNT(*) FROM staging.stg_production),
    (SELECT COUNT(*) FROM warehouse.fact_production)


UNION ALL


SELECT
    'maintenance',
    (SELECT COUNT(*) FROM raw.maintenance),
    (SELECT COUNT(*) FROM staging.stg_maintenance),
    (SELECT COUNT(*) FROM warehouse.fact_maintenance)


UNION ALL


SELECT
    'financial_transactions',
    (SELECT COUNT(*) FROM raw.financial_transactions),
    (SELECT COUNT(*) FROM staging.stg_financial_transactions),
    (SELECT COUNT(*) FROM warehouse.fact_financial_transactions)


UNION ALL


SELECT
    'budget',
    (SELECT COUNT(*) FROM raw.budget),
    (SELECT COUNT(*) FROM staging.stg_budget),
    (SELECT COUNT(*) FROM warehouse.fact_budget)


UNION ALL


SELECT
    'energy_consumption',
    (SELECT COUNT(*) FROM raw.energy_consumption),
    (SELECT COUNT(*) FROM staging.stg_energy_consumption),
    (SELECT COUNT(*) FROM warehouse.fact_energy_consumption)


UNION ALL


SELECT
    'emissions',
    (SELECT COUNT(*) FROM raw.emissions),
    (SELECT COUNT(*) FROM staging.stg_emissions),
    (SELECT COUNT(*) FROM warehouse.fact_emissions)


UNION ALL


SELECT
    'waste',
    (SELECT COUNT(*) FROM raw.waste),
    (SELECT COUNT(*) FROM staging.stg_waste),
    (SELECT COUNT(*) FROM warehouse.fact_waste)


UNION ALL


SELECT
    'inventory',
    (SELECT COUNT(*) FROM raw.inventory),
    (SELECT COUNT(*) FROM staging.stg_inventory),
    (SELECT COUNT(*) FROM warehouse.fact_inventory)


) validation

(
    table_name,
    raw_count,
    staging_count,
    warehouse_count
)

ORDER BY
    table_name;