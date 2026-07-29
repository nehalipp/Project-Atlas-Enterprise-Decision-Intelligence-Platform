
# Project Atlas
## Enterprise Data Quality Report


Generated:

2026-07-29


---


# Dataset Summary


| Dataset | Status |
|---|---|
| Customers | WARNING |
| Products | WARNING |
| Sales | CRITICAL |


---


# Customer Data Quality Findings


Total Records:

51000


Duplicate Records:

986


Missing Values:

{'customer_id': 0, 'customer_name': 0, 'industry': 2540, 'customer_segment': 2535, 'country': 2547, 'region': 0, 'customer_since': 0}



---


# Product Data Quality Findings


Total Records:

5100


Duplicate Records:

94


Negative Costs:

51


Unknown Categories:

51



---


# Sales Data Quality Findings


Total Records:

510000


Duplicate Transactions:

10000


Missing Product References:

25476


Negative Quantity Records:

5096


Revenue Mismatch Records:

10137



---


# Recommendation


Data cleansing should be completed before loading
datasets into the analytical warehouse.
