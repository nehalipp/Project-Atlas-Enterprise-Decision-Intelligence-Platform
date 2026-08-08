/*
==========================================================
Project Atlas
RAW Layer Table Creation

Purpose:
Create raw ingestion tables matching source CSV files

Schema:
raw
==========================================================
*/


CREATE SCHEMA IF NOT EXISTS raw;


-- ==========================================================
-- ACCOUNTS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.accounts
(
    account_id VARCHAR(50),
    account_name VARCHAR(255),
    account_type VARCHAR(100),
    account_category VARCHAR(100),
    department VARCHAR(100),
    active_status VARCHAR(50)
);


-- ==========================================================
-- CUSTOMERS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.customers
(
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    industry VARCHAR(100),
    customer_segment VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    customer_since DATE
);


-- ==========================================================
-- PRODUCTS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.products
(
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(100),
    unit_cost NUMERIC(12,2),
    unit_price NUMERIC(12,2),
    product_status VARCHAR(50)
);


-- ==========================================================
-- SUPPLIERS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.suppliers
(
    supplier_id VARCHAR(50),
    supplier_name VARCHAR(255),
    supplier_category VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    performance_rating NUMERIC(5,2),
    supplier_status VARCHAR(50)
);


-- ==========================================================
-- LOCATIONS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.locations
(
    location_id VARCHAR(50),
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


-- ==========================================================
-- EMPLOYEES
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.employees
(
    employee_id VARCHAR(50),
    employee_name VARCHAR(255),
    department VARCHAR(100),
    job_title VARCHAR(100),
    location_id VARCHAR(50),
    manager_id VARCHAR(50),
    hire_date DATE,
    salary NUMERIC(12,2),
    employment_status VARCHAR(50),
    performance_rating NUMERIC(5,2)
);


-- ==========================================================
-- MACHINES
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.machines
(
    machine_id VARCHAR(50),
    machine_name VARCHAR(255),
    machine_type VARCHAR(100),
    manufacturer VARCHAR(100),
    location_id VARCHAR(50),
    purchase_date DATE,
    warranty_expiry DATE,
    expected_life_years NUMERIC(5,2),
    machine_status VARCHAR(50)
);

-- ==========================================================
-- FACT TABLES
-- ==========================================================


-- ==========================================================
-- SALES TRANSACTIONS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.sales_transactions
(
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    location_id VARCHAR(50),
    transaction_date DATE,
    quantity INTEGER,
    unit_price NUMERIC(12,2),
    discount_percentage NUMERIC(5,2),
    revenue NUMERIC(14,2),
    sales_channel VARCHAR(100)
);


-- ==========================================================
-- PRODUCTION
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.production
(
    production_id VARCHAR(50),
    production_date DATE,
    machine_id VARCHAR(50),
    product_id VARCHAR(50),
    location_id VARCHAR(50),
    shift VARCHAR(50),
    units_produced INTEGER,
    defect_count INTEGER,
    defect_rate NUMERIC(8,4),
    production_hours NUMERIC(8,2),
    production_status VARCHAR(50)
);


-- ==========================================================
-- MAINTENANCE
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.maintenance
(
    maintenance_id VARCHAR(50),
    maintenance_date DATE,
    machine_id VARCHAR(50),
    maintenance_type VARCHAR(100),
    technician VARCHAR(255),
    downtime_hours NUMERIC(8,2),
    repair_cost NUMERIC(12,2),
    maintenance_status VARCHAR(50)
);


-- ==========================================================
-- FINANCIAL TRANSACTIONS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.financial_transactions
(
    transaction_id VARCHAR(50),
    transaction_date DATE,
    account_id VARCHAR(50),
    department VARCHAR(100),
    transaction_type VARCHAR(100),
    amount NUMERIC(14,2),
    currency VARCHAR(10),
    vendor VARCHAR(255),
    payment_status VARCHAR(50)
);


-- ==========================================================
-- BUDGET
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.budget
(
    budget_id VARCHAR(50),
    fiscal_year INTEGER,
    department VARCHAR(100),
    account_type VARCHAR(100),
    budget_amount NUMERIC(14,2),
    approved_by VARCHAR(255),
    budget_status VARCHAR(50)
);


-- ==========================================================
-- ENERGY CONSUMPTION
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.energy_consumption
(
    energy_id VARCHAR(50),
    measurement_date DATE,
    location_id VARCHAR(50),
    energy_source VARCHAR(100),
    consumption_kwh NUMERIC(14,2),
    energy_cost NUMERIC(12,2)
);


-- ==========================================================
-- EMISSIONS
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.emissions
(
    emission_id VARCHAR(50),
    measurement_date DATE,
    location_id VARCHAR(50),
    emission_type VARCHAR(100),
    scope VARCHAR(50),
    carbon_emission_tons NUMERIC(14,2)
);


-- ==========================================================
-- WASTE
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.waste
(
    waste_id VARCHAR(50),
    measurement_date DATE,
    location_id VARCHAR(50),
    waste_type VARCHAR(100),
    quantity_tons NUMERIC(14,2),
    disposal_method VARCHAR(100)
);


-- ==========================================================
-- INVENTORY
-- ==========================================================

CREATE TABLE IF NOT EXISTS raw.inventory
(
    inventory_id VARCHAR(50),
    date DATE,
    product_id VARCHAR(50),
    location_id VARCHAR(50),
    inventory_quantity INTEGER,
    unit_cost NUMERIC(12,2),
    inventory_value NUMERIC(14,2),
    stock_status VARCHAR(50)
);