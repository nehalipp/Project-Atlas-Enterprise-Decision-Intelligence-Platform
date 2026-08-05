/*
==========================================================
Project Atlas

Transformation:
customers_clean.sql

Purpose:
Transform raw customer data into standardized staging data.

Business Rules
--------------
1. Remove duplicate customer records
2. Keep latest ingested record
3. Trim text fields
4. Replace missing values
5. Preserve customer history
6. Add ETL metadata
==========================================================
*/

TRUNCATE TABLE staging.customers_clean;

INSERT INTO staging.customers_clean
(
    customer_id,
    customer_name,
    industry,
    customer_segment,
    country,
    region,
    customer_since,
    transformation_timestamp,
    record_source
)

WITH deduplicated_customers AS
(
    SELECT DISTINCT ON (customer_id)

        customer_id,
        customer_name,
        industry,
        customer_segment,
        country,
        region,
        customer_since,
        ingestion_timestamp

    FROM raw.customers

    WHERE customer_id IS NOT NULL

    ORDER BY
        customer_id,
        ingestion_timestamp DESC
),

clean_customers AS
(
    SELECT

        customer_id,

        TRIM(customer_name) AS customer_name,

        COALESCE(NULLIF(TRIM(industry),''),'Unknown')
            AS industry,

        COALESCE(NULLIF(TRIM(customer_segment),''),'Unknown')
            AS customer_segment,

        COALESCE(NULLIF(TRIM(country),''),'Unknown')
            AS country,

        COALESCE(NULLIF(TRIM(region),''),'Unknown')
            AS region,

        customer_since

    FROM deduplicated_customers
)

SELECT

    customer_id,
    customer_name,
    industry,
    customer_segment,
    country,
    region,
    customer_since,
    CURRENT_TIMESTAMP,
    'Project Atlas Staging'

FROM clean_customers;