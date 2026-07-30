/*
==========================================================
Project Atlas
Enterprise Decision Intelligence Platform

Raw Layer Tables
==========================================================

Purpose:
Store source data exactly as received.

No transformations are performed in this layer.
==========================================================
*/

----------------------------------------------------------
-- Customers
----------------------------------------------------------

CREATE TABLE IF NOT EXISTS raw.customers
(
    customer_id         VARCHAR(20),
    customer_name       VARCHAR(200),
    industry            VARCHAR(100),
    customer_segment    VARCHAR(100),
    country             VARCHAR(100),
    region              VARCHAR(100),
    customer_since      DATE,
    source_system       VARCHAR(50) DEFAULT 'Project Atlas',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

----------------------------------------------------------
-- Products
----------------------------------------------------------

CREATE TABLE IF NOT EXISTS raw.products
(
    product_id          VARCHAR(20),
    product_name        VARCHAR(200),
    category            VARCHAR(100),
    supplier_id         VARCHAR(20),
    unit_cost           NUMERIC(12,2),
    unit_price          NUMERIC(12,2),
    product_status      VARCHAR(50),
    launch_date         DATE,
    source_system       VARCHAR(50) DEFAULT 'Project Atlas',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

----------------------------------------------------------
-- Suppliers
----------------------------------------------------------

CREATE TABLE IF NOT EXISTS raw.suppliers
(
    supplier_id         VARCHAR(20),
    supplier_name       VARCHAR(200),
    supplier_country    VARCHAR(100),
    supplier_rating     NUMERIC(3,2),
    source_system       VARCHAR(50) DEFAULT 'Project Atlas',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

----------------------------------------------------------
-- Locations
----------------------------------------------------------

CREATE TABLE IF NOT EXISTS raw.locations
(
    location_id         VARCHAR(20),
    city                VARCHAR(100),
    state               VARCHAR(100),
    country             VARCHAR(100),
    region              VARCHAR(100),
    source_system       VARCHAR(50) DEFAULT 'Project Atlas',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

----------------------------------------------------------
-- Employees
----------------------------------------------------------

CREATE TABLE IF NOT EXISTS raw.employees
(
    employee_id         VARCHAR(20),
    employee_name       VARCHAR(200),
    department          VARCHAR(100),
    designation         VARCHAR(100),
    manager             VARCHAR(200),
    hire_date           DATE,
    source_system       VARCHAR(50) DEFAULT 'Project Atlas',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

----------------------------------------------------------
-- Sales Transactions
----------------------------------------------------------

CREATE TABLE IF NOT EXISTS raw.sales_transactions
(
    transaction_id          VARCHAR(30),
    transaction_date        DATE,

    customer_id             VARCHAR(20),
    product_id              VARCHAR(20),
    location_id             VARCHAR(20),

    quantity                INTEGER,
    unit_price              NUMERIC(12,2),
    discount_percentage     NUMERIC(5,2),
    revenue                 NUMERIC(14,2),

    sales_channel           VARCHAR(50),

    source_system           VARCHAR(50) DEFAULT 'Project Atlas',
    ingestion_timestamp     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);