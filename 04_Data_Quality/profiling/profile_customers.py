"""
Project Atlas

Customer Data Profiling

Purpose:
Analyze customer dataset quality before transformation.
"""


import pandas as pd
import os



def load_customer_data():

    file_path = (
        "../../03_Data_Generation/output/raw_customers.csv"
    )

    return pd.read_csv(file_path)




def profile_customers(df):


    report = {}


    # Dataset size

    report["total_records"] = len(df)



    # Column information

    report["columns"] = list(
        df.columns
    )



    # Missing values

    report["missing_values"] = (
        df.isnull()
        .sum()
        .to_dict()
    )



    # Duplicate records

    report["duplicate_records"] = (
        df.duplicated()
        .sum()
    )



    # Unique customers

    report["unique_customer_ids"] = (
        df["customer_id"]
        .nunique()
    )



    return report




def print_report(report):


    print(
        "\n===== CUSTOMER DATA QUALITY REPORT =====\n"
    )


    print(
        f"Total Records: {report['total_records']}"
    )


    print(
        f"Unique Customer IDs: {report['unique_customer_ids']}"
    )


    print(
        f"Duplicate Records: {report['duplicate_records']}"
    )


    print(
        "\nMissing Values:"
    )


    for column,value in report["missing_values"].items():

        print(
            f"{column}: {value}"
        )




if __name__ == "__main__":


    customers = load_customer_data()


    report = profile_customers(
        customers
    )


    print_report(
        report
    )