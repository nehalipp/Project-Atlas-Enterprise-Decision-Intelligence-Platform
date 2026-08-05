TRUNCATE TABLE staging.employees_clean;

INSERT INTO staging.employees_clean
(
employee_id,
employee_name,
department,
job_title,
location_id,
hire_date,
employment_status,
salary_band,
manager_id,
transformation_timestamp,
record_source
)

WITH deduplicated AS
(
SELECT DISTINCT ON(employee_id)
*
FROM raw.employees
WHERE employee_id IS NOT NULL
ORDER BY employee_id,ingestion_timestamp DESC
)

SELECT

employee_id,

TRIM(employee_name),

COALESCE(NULLIF(TRIM(department),''),'Unknown'),

COALESCE(NULLIF(TRIM(job_title),''),'Unknown'),

location_id,

hire_date,

COALESCE(NULLIF(TRIM(employment_status),''),'Unknown'),

salary_band,

manager_id,

CURRENT_TIMESTAMP,

'Project Atlas Staging'

FROM deduplicated;