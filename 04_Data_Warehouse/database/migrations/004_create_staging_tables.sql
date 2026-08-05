/*
==========================================================
Project Atlas

Migration:
004_create_staging_tables.sql

Purpose:
Create cleaned staging layer tables.

The staging layer contains standardized,
validated data before warehouse loading.
==========================================================
*/


CREATE TABLE IF NOT EXISTS staging.customers_clean
(
    customer_id VARCHAR(20),
    customer_name VARCHAR(200),
    industry VARCHAR(100),
    customer_segment VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    customer_since DATE,
    transformation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    record_source VARCHAR(50) DEFAULT 'Project Atlas Staging'
);



CREATE TABLE IF NOT EXISTS staging.products_clean
(
    product_id VARCHAR(20),
    product_name VARCHAR(200),
    category VARCHAR(100),
    supplier_id VARCHAR(20),
    unit_cost NUMERIC(12,2),
    unit_price NUMERIC(12,2),
    product_status VARCHAR(50),
    launch_date DATE,
    transformation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    record_source VARCHAR(50) DEFAULT 'Project Atlas Staging'
);



CREATE TABLE IF NOT EXISTS staging.suppliers_clean
(
    supplier_id VARCHAR(50),
    supplier_name VARCHAR(200),
    supplier_category VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    performance_rating NUMERIC(5,2),
    contract_status VARCHAR(50),
    supplier_since DATE,
    transformation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    record_source VARCHAR(50) DEFAULT 'Project Atlas Staging'
);



CREATE TABLE IF NOT EXISTS staging.locations_clean
(
    location_id VARCHAR(50),
    facility_name VARCHAR(200),
    location_type VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    operating_status VARCHAR(50),
    opening_date DATE,
    transformation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    record_source VARCHAR(50) DEFAULT 'Project Atlas Staging'
);



CREATE TABLE IF NOT EXISTS staging.employees_clean
(
    employee_id VARCHAR(50),
    employee_name VARCHAR(200),
    department VARCHAR(100),
    job_title VARCHAR(150),
    location_id VARCHAR(50),
    hire_date DATE,
    employment_status VARCHAR(50),
    salary_band VARCHAR(50),
    manager_id VARCHAR(50),
    transformation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    record_source VARCHAR(50) DEFAULT 'Project Atlas Staging'
);



CREATE TABLE IF NOT EXISTS staging.sales_transactions_clean
(
    transaction_id VARCHAR(30),
    transaction_date DATE,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    location_id VARCHAR(20),
    quantity INTEGER,
    unit_price NUMERIC(12,2),
    discount_percentage NUMERIC(5,2),
    revenue NUMERIC(14,2),
    sales_channel VARCHAR(50),
    transformation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    record_source VARCHAR(50) DEFAULT 'Project Atlas Staging'
);