TRUNCATE TABLE warehouse.dim_location;


INSERT INTO warehouse.dim_location
(
location_key,
location_id,
facility_name,
location_type,
city,
country,
region,
operating_status,
effective_date
)


SELECT

ROW_NUMBER() OVER(),

location_id,

facility_name,

location_type,

city,

country,

region,

operating_status,

CURRENT_TIMESTAMP

FROM staging.locations_clean;