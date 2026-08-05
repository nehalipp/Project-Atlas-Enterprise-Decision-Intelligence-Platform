# Project Atlas Data Dictionary


## warehouse.dim_customer

| Column | Type | Description |
|---|---|---|
| customer_key | integer | Surrogate key |
| customer_id | varchar | Business customer identifier |
| customer_name | varchar | Customer name |
| industry | varchar | Customer industry |
| customer_segment | varchar | Customer classification |
| country | varchar | Customer country |
| region | varchar | Geographic region |
| effective_date | timestamp | SCD effective timestamp |


## warehouse.fact_sales

| Column | Type | Description |
|---|---|---|
| sales_key | integer | Fact table surrogate key |
| transaction_id | varchar | Transaction identifier |
| date_key | integer | Date dimension reference |
| customer_key | integer | Customer dimension reference |
| product_key | integer | Product dimension reference |
| revenue | numeric | Sales revenue |