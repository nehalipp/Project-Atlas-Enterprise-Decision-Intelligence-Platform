"""
Project Atlas

Product Data Profiling

Purpose:
Analyze product master data quality before
warehouse ingestion.
"""


import pandas as pd



def load_product_data():

    file_path = (
        "../../03_Data_Generation/output/raw_products.csv"
    )

    return pd.read_csv(file_path)




def profile_products(df):


    report = {}


    # Dataset size

    report["total_records"] = len(df)



    # Unique products

    report["unique_product_ids"] = (
        df["product_id"]
        .nunique()
    )



    # Duplicate records

    report["duplicate_records"] = int(
        df.duplicated()
        .sum()
    )



    # Missing values

    report["missing_values"] = (
        df.isnull()
        .sum()
        .to_dict()
    )



    # Missing percentage

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


    # Negative cost validation

    report["negative_cost_records"] = (
        df[
            df["unit_cost"] < 0
        ]
        .shape[0]
    )



    # Invalid categories

    report["unknown_categories"] = (
        df[
            df["category"]
            ==
            "Unknown Category"
        ]
        .shape[0]
    )



    # Price outliers

    average_price = (
        df["unit_price"]
        .mean()
    )


    report["price_outliers"] = (
        df[
            df["unit_price"]
            >
            average_price * 5
        ]
        .shape[0]
    )



    return report




def print_report(report):


    print(
        "\n===== PRODUCT DATA QUALITY REPORT =====\n"
    )


    print(
        f"Total Records: {report['total_records']}"
    )


    print(
        f"Unique Product IDs: {report['unique_product_ids']}"
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
        f"Negative Costs: {report['negative_cost_records']}"
    )


    print(
        f"Unknown Categories: {report['unknown_categories']}"
    )


    print(
        f"Price Outliers: {report['price_outliers']}"
    )




if __name__ == "__main__":


    products = load_product_data()


    report = profile_products(
        products
    )


    print_report(
        report
    )