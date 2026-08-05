-- ============================================
-- Location Analytics
-- ============================================

-- OUTPUT: revenue_by_country.csv

SELECT
    l.country,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_location l
ON f.location_key = l.location_key
GROUP BY l.country
ORDER BY revenue DESC;


-- OUTPUT: revenue_by_region.csv

SELECT
    l.region,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_location l
ON f.location_key = l.location_key
GROUP BY l.region
ORDER BY revenue DESC;


-- OUTPUT: top_performing_facilities.csv

SELECT
    l.facility_name,
    ROUND(SUM(f.revenue),2) AS revenue
FROM warehouse.fact_sales f
JOIN warehouse.dim_location l
ON f.location_key = l.location_key
GROUP BY l.facility_name
ORDER BY revenue DESC;