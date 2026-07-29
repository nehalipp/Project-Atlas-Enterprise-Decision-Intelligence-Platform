"""
Project Atlas

Automated Data Quality Report Generator

Purpose:
Creates enterprise-style data quality documentation
from profiling results.
"""


from datetime import datetime



def determine_status(dataset, report):

    """
    Determines overall dataset health.
    """


    if dataset == "Customers":

        if report["duplicate_records"] > 0:
            return "WARNING"

        return "PASS"



    elif dataset == "Products":

        if (
            report["negative_cost_records"] > 0
            or
            report["unknown_categories"] > 0
        ):
            return "WARNING"

        return "PASS"



    elif dataset == "Sales":

        if (
            report["revenue_mismatch_records"] > 0
            or
            report["negative_quantity_records"] > 0
        ):
            return "CRITICAL"

        return "PASS"




def generate_report():

    """
    Generates markdown quality report.
    """


    # Import profiling modules

    import sys

    sys.path.append("../profiling")


    from profile_customers import (
        load_customer_data,
        profile_customers
    )


    from profile_products import (
        load_product_data,
        profile_products
    )


    from profile_sales import (
        load_sales_data,
        profile_sales
    )



    # Run profiling


    customer_report = profile_customers(
        load_customer_data()
    )


    product_report = profile_products(
        load_product_data()
    )


    sales_report = profile_sales(
        load_sales_data()
    )



    # Determine statuses


    customer_status = determine_status(
        "Customers",
        customer_report
    )


    product_status = determine_status(
        "Products",
        product_report
    )


    sales_status = determine_status(
        "Sales",
        sales_report
    )



    report_content = f"""
# Project Atlas
## Enterprise Data Quality Report


Generated:

{datetime.now().strftime("%Y-%m-%d")}


---


# Dataset Summary


| Dataset | Status |
|---|---|
| Customers | {customer_status} |
| Products | {product_status} |
| Sales | {sales_status} |


---


# Customer Data Quality Findings


Total Records:

{customer_report['total_records']}


Duplicate Records:

{customer_report['duplicate_records']}


Missing Values:

{customer_report['missing_values']}



---


# Product Data Quality Findings


Total Records:

{product_report['total_records']}


Duplicate Records:

{product_report['duplicate_records']}


Negative Costs:

{product_report['negative_cost_records']}


Unknown Categories:

{product_report['unknown_categories']}



---


# Sales Data Quality Findings


Total Records:

{sales_report['total_records']}


Duplicate Transactions:

{sales_report['duplicate_records']}


Missing Product References:

{sales_report['missing_values']['product_id']}


Negative Quantity Records:

{sales_report['negative_quantity_records']}


Revenue Mismatch Records:

{sales_report['revenue_mismatch_records']}



---


# Recommendation


Data cleansing should be completed before loading
datasets into the analytical warehouse.
"""



    output_file = (
        "data_quality_report.md"
    )


    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            report_content
        )


    print(
        "Data quality report generated successfully."
    )




if __name__ == "__main__":

    generate_report()