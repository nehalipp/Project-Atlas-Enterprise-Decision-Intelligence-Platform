/*
==========================================================
Project Atlas

Migration:
006_create_warehouse_tables.sql

Purpose:
Create warehouse star schema.
==========================================================
*/


CREATE TABLE IF NOT EXISTS warehouse.dim_customer
(
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(20),
    customer_name VARCHAR(200),
    industry VARCHAR(100),
    customer_segment VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    effective_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS warehouse.dim_supplier
(
    supplier_key SERIAL PRIMARY KEY,
    supplier_id VARCHAR(50),
    supplier_name VARCHAR(200),
    supplier_category VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    performance_rating NUMERIC(5,2),
    effective_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS warehouse.dim_product
(
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(20),
    product_name VARCHAR(200),
    category VARCHAR(100),
    supplier_key INTEGER,
    unit_cost NUMERIC(12,2),
    unit_price NUMERIC(12,2),
    product_status VARCHAR(50),
    effective_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS warehouse.dim_location
(
    location_key SERIAL PRIMARY KEY,
    location_id VARCHAR(50),
    facility_name VARCHAR(200),
    location_type VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    operating_status VARCHAR(50),
    effective_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS warehouse.dim_employee
(
    employee_key SERIAL PRIMARY KEY,
    employee_id VARCHAR(50),
    employee_name VARCHAR(200),
    department VARCHAR(100),
    job_title VARCHAR(150),
    location_id VARCHAR(50),
    hire_date DATE,
    employment_status VARCHAR(50),
    effective_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS warehouse.dim_date
(
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    day INTEGER,
    day_name VARCHAR(20)
);



CREATE TABLE IF NOT EXISTS warehouse.fact_sales
(
    sales_key SERIAL PRIMARY KEY,
    transaction_id VARCHAR(30),
    date_key INTEGER,
    customer_key INTEGER,
    product_key INTEGER,
    location_key INTEGER,
    quantity INTEGER,
    unit_price NUMERIC(12,2),
    discount_percentage NUMERIC(5,2),
    revenue NUMERIC(14,2),
    sales_channel VARCHAR(50),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);