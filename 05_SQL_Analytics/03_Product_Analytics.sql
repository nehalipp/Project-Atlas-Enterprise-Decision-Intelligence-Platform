-- ============================================
-- Product Analytics
-- ============================================

-- OUTPUT: top_selling_products.csv

SELECT
    p.product_name,
    SUM(f.quantity) AS units_sold,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_product p
ON f.product_key = p.product_key
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;


-- OUTPUT: revenue_by_category.csv

SELECT
    p.category,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_product p
ON f.product_key = p.product_key
GROUP BY p.category
ORDER BY revenue DESC;


-- OUTPUT: average_selling_price.csv

SELECT
    ROUND(AVG(unit_price),2) AS avg_price
FROM warehouse.fact_sales;