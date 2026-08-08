/*
==========================================================
Project Atlas

Pipeline Validation Controller

Executes all ETL validation checks:

1. Row Count Validation
2. Duplicate Validation
3. Referential Integrity Validation
4. Business Rule Validation

==========================================================
*/


\echo ''
\echo '=========================================='
\echo 'ROW COUNT VALIDATION'
\echo '=========================================='

\i sql/validation/row_count_validation.sql



\echo ''
\echo '=========================================='
\echo 'DUPLICATE VALIDATION'
\echo '=========================================='

\i sql/validation/duplicate_validation.sql



\echo ''
\echo '=========================================='
\echo 'REFERENTIAL INTEGRITY VALIDATION'
\echo '=========================================='

\i sql/validation/referential_integrity.sql



\echo ''
\echo '=========================================='
\echo 'BUSINESS RULE VALIDATION'
\echo '=========================================='

\i sql/validation/business_rule_validation.sql



\echo ''
\echo '=========================================='
\echo 'PIPELINE VALIDATION COMPLETED'
\echo '=========================================='