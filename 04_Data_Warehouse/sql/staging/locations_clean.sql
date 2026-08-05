TRUNCATE TABLE staging.locations_clean;

INSERT INTO staging.locations_clean
(
location_id,
facility_name,
location_type,
city,
country,
region,
operating_status,
opening_date,
transformation_timestamp,
record_source
)

WITH deduplicated AS
(
SELECT DISTINCT ON(location_id)
*
FROM raw.locations
WHERE location_id IS NOT NULL
ORDER BY location_id,ingestion_timestamp DESC
)

SELECT

location_id,

TRIM(facility_name),

COALESCE(NULLIF(TRIM(location_type),''),'Unknown'),

COALESCE(NULLIF(TRIM(city),''),'Unknown'),

COALESCE(NULLIF(TRIM(country),''),'Unknown'),

COALESCE(NULLIF(TRIM(region),''),'Unknown'),

COALESCE(NULLIF(TRIM(operating_status),''),'Unknown'),

opening_date,

CURRENT_TIMESTAMP,

'Project Atlas Staging'

FROM deduplicated;