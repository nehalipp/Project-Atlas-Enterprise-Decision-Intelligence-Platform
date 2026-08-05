/*
==========================================================
Project Atlas

Transformation:
products_clean.sql

Purpose:
Transform raw product data into standardized staging data.

Business Rules
--------------
1. Remove duplicate products
2. Keep latest ingested record
3. Trim text fields
4. Replace missing values
5. Prevent negative costs
6. Ensure selling price is not below cost
7. Add ETL metadata
==========================================================
*/

TRUNCATE TABLE staging.products_clean;

INSERT INTO staging.products_clean
(
    product_id,
    product_name,
    category,
    supplier_id,
    unit_cost,
    unit_price,
    product_status,
    launch_date,
    transformation_timestamp,
    record_source
)

WITH deduplicated_products AS
(
    SELECT DISTINCT ON (product_id)

        product_id,
        product_name,
        category,
        supplier_id,
        unit_cost,
        unit_price,
        product_status,
        launch_date,
        ingestion_timestamp

    FROM raw.products

    WHERE product_id IS NOT NULL

    ORDER BY
        product_id,
        ingestion_timestamp DESC
),

clean_products AS
(
    SELECT

        product_id,

        TRIM(product_name) AS product_name,

        COALESCE(NULLIF(TRIM(category), ''), 'Unknown')
            AS category,

        supplier_id,

        CASE
            WHEN unit_cost < 0 THEN 0
            ELSE unit_cost
        END AS unit_cost,

        CASE
            WHEN unit_price <
                CASE
                    WHEN unit_cost < 0 THEN 0
                    ELSE unit_cost
                END
            THEN
                CASE
                    WHEN unit_cost < 0 THEN 0
                    ELSE unit_cost
                END
            ELSE unit_price
        END AS unit_price,

        COALESCE(NULLIF(TRIM(product_status), ''), 'Unknown')
            AS product_status,

        launch_date

    FROM deduplicated_products
)

SELECT

    product_id,
    product_name,
    category,
    supplier_id,
    unit_cost,
    unit_price,
    product_status,
    launch_date,
    CURRENT_TIMESTAMP,
    'Project Atlas Staging'

FROM clean_products;