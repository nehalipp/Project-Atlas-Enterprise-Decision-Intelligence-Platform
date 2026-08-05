-- ============================================
-- Executive KPI Dashboard
-- ============================================
-- OUTPUT: executive_kpis.csv

SELECT

COUNT(DISTINCT transaction_id) AS total_transactions,

ROUND(SUM(revenue),2) AS total_revenue,

ROUND(AVG(revenue),2) AS average_order_value,

COUNT(DISTINCT customer_key) AS total_customers,

COUNT(DISTINCT product_key) AS total_products,

COUNT(DISTINCT location_key) AS total_locations

FROM warehouse.fact_sales;


-- OUTPUT: top_customer.csv

SELECT
    c.customer_name,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_customer c
ON f.customer_key = c.customer_key
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 1;


-- OUTPUT: top_product.csv

SELECT
    p.product_name,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_product p
ON f.product_key = p.product_key
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 1;


-- OUTPUT: top_country.csv

SELECT
    l.country,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_location l
ON f.location_key = l.location_key
GROUP BY l.country
ORDER BY revenue DESC
LIMIT 1;