# Project Atlas
# Enterprise Data Quality Assessment Report


Generated:

July 2026


---

# Executive Summary


Project Atlas evaluated enterprise datasets across customer,
product, and sales domains before analytical warehouse ingestion.


The objective of this assessment was to identify data quality
issues impacting analytical reliability across the following
dimensions:

- Completeness
- Uniqueness
- Referential Integrity
- Validity
- Accuracy


Overall Data Quality Status:

⚠ Requires Data Cleansing Before Warehouse Loading


Datasets Assessed:


| Dataset | Records | Status |
|---|---:|---|
| Customers | 51,000 | Warning |
| Products | 5,100 | Warning |
| Sales Transactions | 510,000 | Critical |



---

# Customer Dataset Assessment


Status:

⚠ Requires Data Cleaning


## Findings


1. Dataset contains 51,000 records.
2. 50,000 unique customer IDs identified.
3. 986 exact duplicate customer records detected.
4. Approximately 5% missing values found in:
   - Industry
   - Customer Segment
   - Country


## Data Quality Issues


### Completeness

Missing customer attributes may impact segmentation,
customer profiling, and geographic analysis.


### Uniqueness

Duplicate customer records may result in:

- Incorrect customer counts
- Duplicate reporting
- Inaccurate customer-level metrics



## Business Impact


Customer segmentation and geographic reporting may produce
inaccurate results without remediation.


Recommended actions:

- Apply missing value treatment rules.
- Standardize customer attributes.
- Deduplicate records using customer business keys.



---

# Product Dataset Assessment


Status:

⚠ Requires Cleaning Before Warehouse Load


## Findings


1. Dataset contains 5,100 records.
2. 5,000 unique products identified.
3. 94 exact duplicate product records detected based on full-row duplication checks.
4. Approximately 5% missing values found in:
   - Product Category
   - Supplier Mapping


## Business Rule Violations


- 51 products contain negative costs.
- 51 products contain invalid categories.
- 18 products contain extreme price values.


## Data Quality Issues


### Completeness

Missing supplier mappings impact supplier analysis
and procurement reporting.


### Validity

Negative costs and invalid categories violate product
master data rules.


### Accuracy

Extreme pricing values may indicate:

- Data entry issues
- Currency conversion errors
- Incorrect source system updates



## Business Impact


Product analytics, profitability reporting, and supplier
analysis may produce inaccurate results without remediation.


Recommended actions:

- Validate supplier relationships.
- Standardize product categories.
- Review abnormal pricing records.
- Correct invalid cost values.



---

# Sales Transaction Dataset Assessment


Status:

🔴 Critical - Requires Remediation Before Warehouse Load


## Findings


1. Dataset contains 510,000 transaction records.
2. 500,000 unique transaction IDs identified.
3. 10,000 duplicate transaction records detected.
4. 25,476 transactions contain missing product references.
5. 5,096 transactions contain invalid negative quantities.
6. 10,137 transactions contain revenue calculation mismatches.


## Business Rule Violations


### Quantity Validation


Requirement:
quantity > 0


Finding:

5,096 transactions contain invalid quantity values.



---

### Revenue Validation


Requirement:
revenue =
quantity × unit_price × (1 - discount_percentage)


Finding:

10,137 transactions contain revenue calculation mismatches.



---

### Referential Integrity Validation


Requirement:

Every sales transaction must reference
a valid product.


Finding:

25,476 transactions contain missing product references.



## Business Impact


Sales analytics, revenue reporting, and executive dashboards
may produce inaccurate results without remediation.


Potential impacts:

- Incorrect revenue calculations
- Inaccurate product performance analysis
- Incorrect business forecasting
- Misleading executive KPIs



Recommended actions:

- Remove duplicate transactions.
- Validate product references against product master data.
- Separate sales and return transactions.
- Recalculate revenue using validated business rules.



---

# Dataset Summary


| Dataset | Status | Issues |
|---|---|---|
| Customers | Warning | Missing attributes, duplicates |
| Products | Warning | Missing suppliers, invalid categories |
| Sales Transactions | Critical | Revenue mismatches, missing products |



---

# Critical Findings


1. 25,476 sales transactions are missing product references.

2. 5,096 transactions contain invalid quantity values.

3. 10,137 transactions contain revenue calculation mismatches.

4. Customer and product master datasets contain missing attributes
   requiring cleansing before warehouse ingestion.

5. Duplicate records may impact analytical accuracy.



---

# Data Quality Dimension Assessment


| Dimension | Description | Status |
|---|---|---|
| Completeness | Missing value detection across datasets | ⚠ Requires Improvement |
| Uniqueness | Duplicate record identification | ⚠ Requires Improvement |
| Referential Integrity | Relationship validation between datasets | 🔴 Critical |
| Validity | Business rule compliance | ⚠ Requires Improvement |
| Accuracy | Revenue and metric validation | 🔴 Critical |



Overall Assessment:


Data cleansing, validation, and transformation processes
should be completed before datasets are promoted into the
analytical warehouse layer.



---

# Recommended Remediation Strategy


## Customer Data


Actions:

- Standardize customer attributes.
- Handle missing values using defined business rules.
- Remove duplicate records using customer identifiers.



## Product Data


Actions:

- Validate supplier mappings.
- Standardize product categories.
- Correct invalid cost and pricing values.



## Sales Data


Actions:

- Remove duplicate transactions.
- Validate foreign key relationships.
- Correct invalid quantities.
- Recalculate revenue metrics.
- Implement automated validation checks.



---

# Conclusion


The Project Atlas data quality assessment identified multiple
issues across enterprise datasets that could impact downstream
analytics and reporting.


Before warehouse loading, datasets should pass defined quality
checks to ensure reliable reporting, accurate decision-making,
and trusted business intelligence.