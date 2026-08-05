TRUNCATE TABLE warehouse.fact_sales;


INSERT INTO warehouse.fact_sales
(
sales_key,
transaction_id,
date_key,
customer_key,
product_key,
location_key,
quantity,
unit_price,
discount_percentage,
revenue,
sales_channel,
load_timestamp
)


SELECT

ROW_NUMBER() OVER(),

s.transaction_id,


d.date_key,


c.customer_key,


p.product_key,


l.location_key,


s.quantity,

s.unit_price,

s.discount_percentage,

s.revenue,

s.sales_channel,

CURRENT_TIMESTAMP


FROM staging.sales_transactions_clean s


LEFT JOIN warehouse.dim_date d

ON s.transaction_date=d.full_date


LEFT JOIN warehouse.dim_customer c

ON s.customer_id=c.customer_id


LEFT JOIN warehouse.dim_product p

ON s.product_id=p.product_id


LEFT JOIN warehouse.dim_location l

ON s.location_id=l.location_id;