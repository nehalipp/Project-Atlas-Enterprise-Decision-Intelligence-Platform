/*
==========================================================
Project Atlas
Enterprise Decision Intelligence Platform

Database Creation Script
==========================================================
*/

SELECT 'CREATE DATABASE project_atlas_dw'
WHERE NOT EXISTS (
    SELECT FROM pg_database 
    WHERE datname = 'project_atlas_dw'
)
\gexec