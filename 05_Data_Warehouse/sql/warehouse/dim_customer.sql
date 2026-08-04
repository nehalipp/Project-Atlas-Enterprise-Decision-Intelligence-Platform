TRUNCATE TABLE warehouse.dim_customer;


INSERT INTO warehouse.dim_customer
(
    customer_key,
    customer_id,
    customer_name,
    industry,
    customer_segment,
    country,
    region,
    effective_date
)

SELECT

ROW_NUMBER() OVER(),

customer_id,

customer_name,

industry,

customer_segment,

country,

region,

CURRENT_TIMESTAMP


FROM staging.customers_clean;