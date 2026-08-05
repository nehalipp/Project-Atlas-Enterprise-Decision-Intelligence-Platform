TRUNCATE TABLE staging.sales_transactions_clean;

INSERT INTO staging.sales_transactions_clean
(
transaction_id,
transaction_date,
customer_id,
product_id,
location_id,
quantity,
unit_price,
discount_percentage,
revenue,
sales_channel,
transformation_timestamp,
record_source
)

WITH deduplicated AS
(
SELECT DISTINCT ON(transaction_id)

transaction_id,
transaction_date,
customer_id,
product_id,
location_id,
quantity,
unit_price,
discount_percentage,
revenue,
sales_channel,
ingestion_timestamp

FROM raw.sales_transactions

WHERE transaction_id IS NOT NULL

ORDER BY transaction_id,ingestion_timestamp DESC
),

cleaned AS
(
SELECT

transaction_id,

transaction_date,

customer_id,

product_id,

location_id,

CASE
WHEN quantity<0 THEN 0
ELSE quantity
END quantity,

CASE
WHEN unit_price<0 THEN 0
ELSE unit_price
END unit_price,

CASE
WHEN discount_percentage<0 THEN 0
WHEN discount_percentage>100 THEN 100
ELSE discount_percentage
END discount_percentage,

CASE
WHEN revenue<0 THEN 0
ELSE revenue
END revenue,

COALESCE(NULLIF(TRIM(sales_channel),''),'Unknown') sales_channel

FROM deduplicated
)

SELECT

*,

CURRENT_TIMESTAMP,

'Project Atlas Staging'

FROM cleaned;