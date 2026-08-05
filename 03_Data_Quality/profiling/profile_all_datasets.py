"""
Project Atlas

Enterprise Data Quality Profiling Orchestrator

Purpose:
Execute all dataset profiling modules from a single script.
"""


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



def run_all_profiles():


    print("\n================================")
    print("PROJECT ATLAS DATA QUALITY RUN")
    print("================================\n")


    # Customer profiling

    customers = load_customer_data()

    customer_report = profile_customers(
        customers
    )


    print("\nCUSTOMER DATASET")
    print("----------------")
    print(customer_report)



    # Product profiling

    products = load_product_data()

    product_report = profile_products(
        products
    )


    print("\nPRODUCT DATASET")
    print("----------------")
    print(product_report)



    # Sales profiling

    sales = load_sales_data()

    sales_report = profile_sales(
        sales
    )


    print("\nSALES DATASET")
    print("----------------")
    print(sales_report)



if __name__ == "__main__":

    run_all_profiles()