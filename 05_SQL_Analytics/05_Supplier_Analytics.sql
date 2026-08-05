-- ============================================
-- Supplier Analytics
-- ============================================

-- OUTPUT: revenue_by_supplier.csv

SELECT
    s.supplier_name,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_product p
ON f.product_key = p.product_key
JOIN warehouse.dim_supplier s
ON p.supplier_key = s.supplier_key
GROUP BY s.supplier_name
ORDER BY revenue DESC;


-- OUTPUT: revenue_by_supplier_category.csv

SELECT
    s.supplier_category,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_product p
ON f.product_key = p.product_key
JOIN warehouse.dim_supplier s
ON p.supplier_key = s.supplier_key
GROUP BY s.supplier_category
ORDER BY revenue DESC;


-- OUTPUT: average_supplier_rating.csv

SELECT
    ROUND(AVG(performance_rating),2) AS average_rating
FROM warehouse.dim_supplier;