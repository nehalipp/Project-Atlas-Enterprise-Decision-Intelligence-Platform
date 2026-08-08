/*
==========================================================
Project Atlas
Enterprise Decision Intelligence Platform

Warehouse Dimension Tables
Source: staging schema
Target: warehouse schema
==========================================================
*/

-- ======================================================
-- DIM ACCOUNT
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_account CASCADE;

CREATE TABLE warehouse.dim_account (
    account_key BIGSERIAL PRIMARY KEY,
    account_id VARCHAR(50) NOT NULL,
    account_name VARCHAR(255),
    account_type VARCHAR(100),
    account_category VARCHAR(100),
    department VARCHAR(100),
    active_status VARCHAR(50)
);


-- ======================================================
-- DIM CUSTOMER
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_customer CASCADE;

CREATE TABLE warehouse.dim_customer (
    customer_key BIGSERIAL PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(255),
    industry VARCHAR(100),
    customer_segment VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    customer_since DATE
);


-- ======================================================
-- DIM PRODUCT
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_product CASCADE;

CREATE TABLE warehouse.dim_product (
    product_key BIGSERIAL PRIMARY KEY,
    product_id VARCHAR(50) NOT NULL,
    product_name VARCHAR(255),
    category VARCHAR(100),
    unit_cost NUMERIC(18,2),
    unit_price NUMERIC(18,2),
    product_status VARCHAR(50)
);


-- ======================================================
-- DIM SUPPLIER
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_supplier CASCADE;

CREATE TABLE warehouse.dim_supplier (
    supplier_key BIGSERIAL PRIMARY KEY,
    supplier_id VARCHAR(50) NOT NULL,
    supplier_name VARCHAR(255),
    supplier_category VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    performance_rating NUMERIC(5,2),
    supplier_status VARCHAR(50)
);


-- ======================================================
-- DIM LOCATION
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_location CASCADE;

CREATE TABLE warehouse.dim_location (
    location_key BIGSERIAL PRIMARY KEY,
    location_id VARCHAR(50) NOT NULL,
    facility_name VARCHAR(255),
    location_type VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    latitude NUMERIC(10,6),
    longitude NUMERIC(10,6),
    operating_status VARCHAR(50),
    opening_date DATE
);


-- ======================================================
-- DIM EMPLOYEE
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_employee CASCADE;

CREATE TABLE warehouse.dim_employee (
    employee_key BIGSERIAL PRIMARY KEY,
    employee_id VARCHAR(50) NOT NULL,
    employee_name VARCHAR(255),
    department VARCHAR(100),
    job_title VARCHAR(150),
    location_id VARCHAR(50),
    manager_id VARCHAR(50),
    hire_date DATE,
    salary NUMERIC(18,2),
    employment_status VARCHAR(50),
    performance_rating NUMERIC(5,2)
);


-- ======================================================
-- DIM MACHINE
-- ======================================================

DROP TABLE IF EXISTS warehouse.dim_machine CASCADE;

CREATE TABLE warehouse.dim_machine (
    machine_key BIGSERIAL PRIMARY KEY,
    machine_id VARCHAR(50) NOT NULL,
    machine_name VARCHAR(255),
    machine_type VARCHAR(100),
    manufacturer VARCHAR(150),
    location_id VARCHAR(50),
    purchase_date DATE,
    warranty_expiry DATE,
    expected_life_years NUMERIC(10,2),
    machine_status VARCHAR(50)
);