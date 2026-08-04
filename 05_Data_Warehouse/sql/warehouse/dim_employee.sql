TRUNCATE TABLE warehouse.dim_employee;


INSERT INTO warehouse.dim_employee
(
    employee_key,
    employee_id,
    employee_name,
    department,
    job_title,
    location_id,
    hire_date,
    employment_status,
    effective_date
)

SELECT

ROW_NUMBER() OVER(),

employee_id,

employee_name,

department,

job_title,

location_id,

hire_date,

employment_status,

CURRENT_TIMESTAMP


FROM staging.employees_clean;