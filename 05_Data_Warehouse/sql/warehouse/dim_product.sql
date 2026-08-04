TRUNCATE TABLE warehouse.dim_product;


INSERT INTO warehouse.dim_product
(
    product_key,
    product_id,
    product_name,
    category,
    supplier_key,
    unit_cost,
    unit_price,
    product_status,
    effective_date
)

SELECT

ROW_NUMBER() OVER(),

p.product_id,

p.product_name,

p.category,

s.supplier_key,

p.unit_cost,

p.unit_price,

p.product_status,

CURRENT_TIMESTAMP


FROM staging.products_clean p


LEFT JOIN warehouse.dim_supplier s

ON p.supplier_id = s.supplier_id;