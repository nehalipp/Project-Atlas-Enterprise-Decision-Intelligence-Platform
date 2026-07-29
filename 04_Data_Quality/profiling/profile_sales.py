"""
Project Atlas

Sales Transaction Data Profiling

Purpose:
Validate sales fact data before loading
into analytical warehouse.
"""


import pandas as pd
import numpy as np



def load_sales_data():

    file_path = (
        "../../03_Data_Generation/output/raw_sales_transactions.csv"
    )

    return pd.read_csv(file_path)




def profile_sales(df):


    report = {}



    # -----------------------------
    # Dataset Statistics
    # -----------------------------

    report["total_records"] = len(df)



    report["unique_transactions"] = (
        df["transaction_id"]
        .nunique()
    )



    report["duplicate_records"] = int (
        df.duplicated()
        .sum()
    )



    # -----------------------------
    # Missing Values
    # -----------------------------

    report["missing_values"] = (
        df.isnull()
        .sum()
        .to_dict()
    )



    report["missing_percentage"] = (
        (
            df.isnull()
            .sum()
            /
            len(df)
        )
        *
        100
    ).round(2).to_dict()



    # -----------------------------
    # Quantity Validation
    # -----------------------------

    report["negative_quantity_records"] = (
        df[
            df["quantity"] <= 0
        ]
        .shape[0]
    )



    # -----------------------------
    # Discount Validation
    # -----------------------------

    report["invalid_discount_records"] = (
        df[
            (
                df["discount_percentage"] < 0
            )
            |
            (
                df["discount_percentage"] > 100
            )
        ]
        .shape[0]
    )



    # -----------------------------
    # Revenue Accuracy Check
    # -----------------------------

    expected_revenue = (
        df["quantity"]
        *
        df["unit_price"]
        *
        (
            1 -
            df["discount_percentage"] / 100
        )
    )


    revenue_difference = (
        abs(
            df["revenue"]
            -
            expected_revenue
        )
    )


    report["revenue_mismatch_records"] = int(
        (
            revenue_difference
            >
            0.01
        )
        .sum()
    )



    return report




def print_report(report):


    print(
        "\n===== SALES DATA QUALITY REPORT =====\n"
    )


    print(
        f"Total Records: {report['total_records']}"
    )


    print(
        f"Unique Transactions: {report['unique_transactions']}"
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



    print(
        "\nMissing Percentage:"
    )


    for column,value in report["missing_percentage"].items():

        print(
            f"{column}: {value}%"
        )



    print(
        "\nBusiness Rule Violations:"
    )


    print(
        f"Negative Quantity Records: "
        f"{report['negative_quantity_records']}"
    )


    print(
        f"Invalid Discount Records: "
        f"{report['invalid_discount_records']}"
    )


    print(
        f"Revenue Mismatch Records: "
        f"{report['revenue_mismatch_records']}"
    )




if __name__ == "__main__":


    sales = load_sales_data()


    report = profile_sales(
        sales
    )


    print_report(
        report
    )