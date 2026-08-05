-- =====================================================
-- Project Atlas
-- Sales Analytics
-- =====================================================


-- OUTPUT: total_revenue.csv

SELECT
    ROUND(SUM(revenue),2) AS total_revenue
FROM warehouse.fact_sales;



-- OUTPUT: monthly_revenue_trend.csv

SELECT
    d.year,
    d.month_name,
    ROUND(SUM(f.revenue),2) AS monthly_revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_date d
ON f.date_key = d.date_key
GROUP BY
    d.year,
    d.month,
    d.month_name
ORDER BY
    d.year,
    d.month;



-- OUTPUT: revenue_by_sales_channel.csv

SELECT
    sales_channel,
    ROUND(SUM(revenue),2) AS revenue
FROM warehouse.fact_sales
GROUP BY sales_channel
ORDER BY revenue DESC;



-- OUTPUT: average_order_value.csv

SELECT
    ROUND(AVG(revenue),2) AS average_order_value
FROM warehouse.fact_sales;



-- OUTPUT: top_transactions.csv

SELECT
    transaction_id,
    revenue
FROM warehouse.fact_sales
ORDER BY revenue DESC
LIMIT 10;