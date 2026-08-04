/*
==========================================================
Project Atlas
Transformation: suppliers_clean.sql
==========================================================
*/

TRUNCATE TABLE staging.suppliers_clean;

INSERT INTO staging.suppliers_clean
(
    supplier_id,
    supplier_name,
    supplier_category,
    country,
    region,
    performance_rating,
    contract_status,
    supplier_since,
    transformation_timestamp,
    record_source
)

WITH deduplicated AS
(
SELECT DISTINCT ON (supplier_id)
    supplier_id,
    supplier_name,
    supplier_category,
    country,
    region,
    performance_rating,
    contract_status,
    supplier_since,
    ingestion_timestamp
FROM raw.suppliers
WHERE supplier_id IS NOT NULL
ORDER BY supplier_id, ingestion_timestamp DESC
),

cleaned AS
(
SELECT

supplier_id,

TRIM(supplier_name) supplier_name,

COALESCE(NULLIF(TRIM(supplier_category),''),'Unknown') supplier_category,

COALESCE(NULLIF(TRIM(country),''),'Unknown') country,

COALESCE(NULLIF(TRIM(region),''),'Unknown') region,

LEAST(GREATEST(performance_rating,0),100) performance_rating,

COALESCE(NULLIF(TRIM(contract_status),''),'Unknown') contract_status,

supplier_since

FROM deduplicated
)

SELECT

*,

CURRENT_TIMESTAMP,

'Project Atlas Staging'

FROM cleaned;