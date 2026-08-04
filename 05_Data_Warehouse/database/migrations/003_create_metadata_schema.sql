/*
==========================================================
Project Atlas

Migration:
003_create_metadata_schema.sql

Purpose:
Create technical metadata objects
for warehouse operations.
==========================================================
*/


CREATE SCHEMA IF NOT EXISTS metadata;

CREATE TABLE IF NOT EXISTS metadata.migration_history
(
    migration_id SERIAL PRIMARY KEY,
    migration_name VARCHAR(255) UNIQUE,
    execution_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    execution_status VARCHAR(20),
    execution_duration_seconds NUMERIC(10,2)
);