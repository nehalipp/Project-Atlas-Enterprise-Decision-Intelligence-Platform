/*
==========================================================
Project Atlas
Enterprise Decision Intelligence Platform

Warehouse Fact Tables
Source: staging schema
Target: warehouse schema
==========================================================
*/


-- ======================================================
-- FACT SALES
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_sales CASCADE;

CREATE TABLE warehouse.fact_sales (
    sales_key BIGSERIAL PRIMARY KEY,

    transaction_id VARCHAR(50),
    customer_key BIGINT,
    product_key BIGINT,
    location_key BIGINT,

    transaction_date DATE,
    quantity NUMERIC(18,2),
    unit_price NUMERIC(18,2),
    discount_percentage NUMERIC(10,4),
    revenue NUMERIC(18,2),
    sales_channel VARCHAR(100)
);


-- ======================================================
-- FACT PRODUCTION
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_production CASCADE;

CREATE TABLE warehouse.fact_production (
    production_key BIGSERIAL PRIMARY KEY,

    production_id VARCHAR(50),
    machine_key BIGINT,
    product_key BIGINT,
    location_key BIGINT,

    production_date DATE,
    shift VARCHAR(50),
    units_produced NUMERIC(18,2),
    defect_count NUMERIC(18,2),
    defect_rate NUMERIC(10,6),
    production_hours NUMERIC(18,2),
    production_status VARCHAR(50)
);


-- ======================================================
-- FACT MAINTENANCE
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_maintenance CASCADE;

CREATE TABLE warehouse.fact_maintenance (
    maintenance_key BIGSERIAL PRIMARY KEY,

    maintenance_id VARCHAR(50),
    machine_key BIGINT,

    maintenance_date DATE,
    maintenance_type VARCHAR(100),
    technician VARCHAR(255),
    downtime_hours NUMERIC(18,2),
    repair_cost NUMERIC(18,2),
    maintenance_status VARCHAR(50)
);


-- ======================================================
-- FACT FINANCIAL TRANSACTIONS
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_financial_transactions CASCADE;

CREATE TABLE warehouse.fact_financial_transactions (
    financial_transaction_key BIGSERIAL PRIMARY KEY,

    transaction_id VARCHAR(50),
    account_key BIGINT,

    transaction_date DATE,
    department VARCHAR(100),
    transaction_type VARCHAR(100),
    amount NUMERIC(18,2),
    currency VARCHAR(20),
    vendor VARCHAR(255),
    payment_status VARCHAR(50)
);


-- ======================================================
-- FACT BUDGET
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_budget CASCADE;

CREATE TABLE warehouse.fact_budget (
    budget_key BIGSERIAL PRIMARY KEY,

    budget_id VARCHAR(50),

    fiscal_year INTEGER,
    department VARCHAR(100),
    account_type VARCHAR(100),
    budget_amount NUMERIC(18,2),
    approved_by VARCHAR(255),
    budget_status VARCHAR(50)
);


-- ======================================================
-- FACT ENERGY CONSUMPTION
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_energy_consumption CASCADE;

CREATE TABLE warehouse.fact_energy_consumption (
    energy_key BIGSERIAL PRIMARY KEY,

    energy_id VARCHAR(50),
    location_key BIGINT,

    measurement_date DATE,
    energy_source VARCHAR(100),
    consumption_kwh NUMERIC(18,2),
    energy_cost NUMERIC(18,2)
);


-- ======================================================
-- FACT EMISSIONS
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_emissions CASCADE;

CREATE TABLE warehouse.fact_emissions (
    emission_key BIGSERIAL PRIMARY KEY,

    emission_id VARCHAR(50),
    location_key BIGINT,

    measurement_date DATE,
    emission_type VARCHAR(100),
    scope VARCHAR(50),
    carbon_emission_tons NUMERIC(18,2)
);


-- ======================================================
-- FACT WASTE
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_waste CASCADE;

CREATE TABLE warehouse.fact_waste (
    waste_key BIGSERIAL PRIMARY KEY,

    waste_id VARCHAR(50),
    location_key BIGINT,

    measurement_date DATE,
    waste_type VARCHAR(100),
    quantity_tons NUMERIC(18,2),
    disposal_method VARCHAR(100)
);


-- ======================================================
-- FACT INVENTORY
-- ======================================================

DROP TABLE IF EXISTS warehouse.fact_inventory CASCADE;

CREATE TABLE warehouse.fact_inventory (
    inventory_key BIGSERIAL PRIMARY KEY,

    inventory_id VARCHAR(50),
    product_key BIGINT,
    location_key BIGINT,

    inventory_date DATE,
    inventory_quantity NUMERIC(18,2),
    unit_cost NUMERIC(18,2),
    inventory_value NUMERIC(18,2),
    stock_status VARCHAR(50)
);