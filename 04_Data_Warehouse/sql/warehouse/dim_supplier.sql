TRUNCATE TABLE warehouse.dim_supplier;


INSERT INTO warehouse.dim_supplier
(
supplier_key,
supplier_id,
supplier_name,
supplier_category,
country,
region,
performance_rating,
effective_date
)


SELECT

ROW_NUMBER() OVER(),

supplier_id,

supplier_name,

supplier_category,

country,

region,

performance_rating,

CURRENT_TIMESTAMP

FROM staging.suppliers_clean;