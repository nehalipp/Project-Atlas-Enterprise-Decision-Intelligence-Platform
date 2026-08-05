-- ============================================
-- Customer Analytics
-- ============================================

-- OUTPUT: top_customers.csv

SELECT
    c.customer_name,
    ROUND(SUM(f.revenue),2) AS total_revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_customer c
ON f.customer_key = c.customer_key
GROUP BY c.customer_name
ORDER BY total_revenue DESC
LIMIT 10;


-- OUTPUT: revenue_by_customer_segment.csv

SELECT
    c.customer_segment,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_customer c
ON f.customer_key = c.customer_key
GROUP BY c.customer_segment
ORDER BY revenue DESC;


-- OUTPUT: revenue_by_industry.csv

SELECT
    c.industry,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_customer c
ON f.customer_key = c.customer_key
GROUP BY c.industry
ORDER BY revenue DESC;


-- OUTPUT: customers_by_country.csv

SELECT
    country,
    COUNT(*) AS customers
FROM warehouse.dim_customer
GROUP BY country
ORDER BY customers DESC;