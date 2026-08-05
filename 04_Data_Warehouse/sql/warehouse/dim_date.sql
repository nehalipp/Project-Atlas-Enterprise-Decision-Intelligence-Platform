TRUNCATE TABLE warehouse.dim_date;


INSERT INTO warehouse.dim_date
(
date_key,
full_date,
year,
quarter,
month,
month_name,
day,
day_name
)


SELECT

TO_CHAR(d,'YYYYMMDD')::INTEGER,

d,

EXTRACT(YEAR FROM d),

EXTRACT(QUARTER FROM d),

EXTRACT(MONTH FROM d),

TO_CHAR(d,'Month'),

EXTRACT(DAY FROM d),

TO_CHAR(d,'Day')


FROM generate_series
(
'2020-01-01'::DATE,
'2030-12-31'::DATE,
interval '1 day'
)d;