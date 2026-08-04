/*
==========================================================
Project Atlas

Dimension:
dim_date

Purpose:
Create enterprise date dimension
==========================================================
*/


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

    TO_CHAR(d,'YYYYMMDD')::INTEGER AS date_key,

    d::DATE AS full_date,

    EXTRACT(YEAR FROM d)::INTEGER AS year,

    EXTRACT(QUARTER FROM d)::INTEGER AS quarter,

    EXTRACT(MONTH FROM d)::INTEGER AS month,

    TRIM(TO_CHAR(d,'Month')) AS month_name,

    EXTRACT(DAY FROM d)::INTEGER AS day,

    TRIM(TO_CHAR(d,'Day')) AS day_name


FROM generate_series
(
    '2020-01-01'::DATE,
    '2030-12-31'::DATE,
    INTERVAL '1 day'
) AS d;