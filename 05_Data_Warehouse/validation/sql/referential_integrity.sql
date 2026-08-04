/*
Fact-Dimension Relationship Validation
*/


-- Missing Customers

SELECT COUNT(*) AS missing_customers

FROM warehouse.fact_sales f

LEFT JOIN warehouse.dim_customer c

ON f.customer_key = c.customer_key

WHERE c.customer_key IS NULL;



-- Missing Products

SELECT COUNT(*) AS missing_products

FROM warehouse.fact_sales f

LEFT JOIN warehouse.dim_product p

ON f.product_key = p.product_key

WHERE p.product_key IS NULL;



-- Missing Locations

SELECT COUNT(*) AS missing_locations

FROM warehouse.fact_sales f

LEFT JOIN warehouse.dim_location l

ON f.location_key = l.location_key

WHERE l.location_key IS NULL;