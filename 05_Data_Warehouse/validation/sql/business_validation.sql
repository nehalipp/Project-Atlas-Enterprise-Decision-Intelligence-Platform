/*
Revenue Reconciliation
*/


SELECT

'RAW' AS layer,

SUM(revenue) AS total_revenue

FROM raw.sales_transactions


UNION ALL


SELECT

'STAGING',

SUM(revenue)

FROM staging.sales_transactions_clean


UNION ALL


SELECT

'WAREHOUSE',

SUM(revenue)

FROM warehouse.fact_sales;