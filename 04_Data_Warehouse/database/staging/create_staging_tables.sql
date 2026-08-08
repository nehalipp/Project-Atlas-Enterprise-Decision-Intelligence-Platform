/*
==========================================================
Project Atlas
Enterprise Decision Intelligence Platform

Staging Layer Table Creation

Schema:
    staging

Purpose:
    Temporary landing area after extraction
    before warehouse transformation

==========================================================
*/


CREATE SCHEMA IF NOT EXISTS staging;


-- ========================================================
-- DIMENSION TABLES
-- ========================================================


-- 1. Accounts
CREATE TABLE IF NOT EXISTS staging.stg_accounts (
    account_id VARCHAR(50),
    account_name TEXT,
    account_type TEXT,
    account_category TEXT,
    department TEXT,
    active_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 2. Customers
CREATE TABLE IF NOT EXISTS staging.stg_customers (
    customer_id VARCHAR(50),
    customer_name TEXT,
    industry TEXT,
    customer_segment TEXT,
    country TEXT,
    region TEXT,
    customer_since DATE,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 3. Products
CREATE TABLE IF NOT EXISTS staging.stg_products (
    product_id VARCHAR(50),
    product_name TEXT,
    category TEXT,
    unit_cost NUMERIC(12,2),
    unit_price NUMERIC(12,2),
    product_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 4. Suppliers
CREATE TABLE IF NOT EXISTS staging.stg_suppliers (
    supplier_id VARCHAR(50),
    supplier_name TEXT,
    supplier_category TEXT,
    country TEXT,
    region TEXT,
    performance_rating NUMERIC(5,2),
    supplier_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 5. Locations
CREATE TABLE IF NOT EXISTS staging.stg_locations (
    location_id VARCHAR(50),
    facility_name TEXT,
    location_type TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    region TEXT,
    latitude NUMERIC(10,6),
    longitude NUMERIC(10,6),
    operating_status TEXT,
    opening_date DATE,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 6. Employees
CREATE TABLE IF NOT EXISTS staging.stg_employees (
    employee_id VARCHAR(50),
    employee_name TEXT,
    department TEXT,
    job_title TEXT,
    location_id VARCHAR(50),
    manager_id VARCHAR(50),
    hire_date DATE,
    salary NUMERIC(12,2),
    employment_status TEXT,
    performance_rating NUMERIC(5,2),

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 7. Machines
CREATE TABLE IF NOT EXISTS staging.stg_machines (
    machine_id VARCHAR(50),
    machine_name TEXT,
    machine_type TEXT,
    manufacturer TEXT,
    location_id VARCHAR(50),
    purchase_date DATE,
    warranty_expiry DATE,
    expected_life_years INTEGER,
    machine_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- ========================================================
-- FACT TABLES
-- ========================================================


-- 1. Sales Transactions
CREATE TABLE IF NOT EXISTS staging.stg_sales_transactions (
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    location_id VARCHAR(50),
    transaction_date DATE,
    quantity INTEGER,
    unit_price NUMERIC(12,2),
    discount_percentage NUMERIC(5,2),
    revenue NUMERIC(14,2),
    sales_channel TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 2. Production
CREATE TABLE IF NOT EXISTS staging.stg_production (
    production_id VARCHAR(50),
    production_date DATE,
    machine_id VARCHAR(50),
    product_id VARCHAR(50),
    location_id VARCHAR(50),
    shift TEXT,
    units_produced INTEGER,
    defect_count INTEGER,
    defect_rate NUMERIC(8,4),
    production_hours NUMERIC(10,2),
    production_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 3. Maintenance
CREATE TABLE IF NOT EXISTS staging.stg_maintenance (
    maintenance_id VARCHAR(50),
    maintenance_date DATE,
    machine_id VARCHAR(50),
    maintenance_type TEXT,
    technician TEXT,
    downtime_hours NUMERIC(10,2),
    repair_cost NUMERIC(12,2),
    maintenance_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 4. Financial Transactions
CREATE TABLE IF NOT EXISTS staging.stg_financial_transactions (
    transaction_id VARCHAR(50),
    transaction_date DATE,
    account_id VARCHAR(50),
    department TEXT,
    transaction_type TEXT,
    amount NUMERIC(14,2),
    currency VARCHAR(10),
    vendor TEXT,
    payment_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 5. Budget
CREATE TABLE IF NOT EXISTS staging.stg_budget (
    budget_id VARCHAR(50),
    fiscal_year INTEGER,
    department TEXT,
    account_type TEXT,
    budget_amount NUMERIC(14,2),
    approved_by TEXT,
    budget_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 6. Energy Consumption
CREATE TABLE IF NOT EXISTS staging.stg_energy_consumption (
    energy_id VARCHAR(50),
    measurement_date DATE,
    location_id VARCHAR(50),
    energy_source TEXT,
    consumption_kwh NUMERIC(14,2),
    energy_cost NUMERIC(12,2),

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 7. Emissions
CREATE TABLE IF NOT EXISTS staging.stg_emissions (
    emission_id VARCHAR(50),
    measurement_date DATE,
    location_id VARCHAR(50),
    emission_type TEXT,
    scope TEXT,
    carbon_emission_tons NUMERIC(14,4),

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 8. Waste
CREATE TABLE IF NOT EXISTS staging.stg_waste (
    waste_id VARCHAR(50),
    measurement_date DATE,
    location_id VARCHAR(50),
    waste_type TEXT,
    quantity_tons NUMERIC(14,4),
    disposal_method TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- 9. Inventory
CREATE TABLE IF NOT EXISTS staging.stg_inventory (
    inventory_id VARCHAR(50),
    date DATE,
    product_id VARCHAR(50),
    location_id VARCHAR(50),
    inventory_quantity INTEGER,
    unit_cost NUMERIC(12,2),
    inventory_value NUMERIC(14,2),
    stock_status TEXT,

    etl_batch_id UUID,
    etl_loaded_timestamp TIMESTAMP,
    source_file TEXT
);



-- ========================================================
-- Verification
-- ========================================================

SELECT table_name
FROM information_schema.tables
WHERE table_schema='staging'
ORDER BY table_name;