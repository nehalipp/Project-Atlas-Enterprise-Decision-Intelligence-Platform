"""
Project Atlas: Enterprise Decision Intelligence Platform

Product Master Data Generator

Purpose:
Generates realistic ERP product master data with
intentional enterprise data quality problems.
"""


import pandas as pd
import numpy as np

from faker import Faker

import sys
import os


# Import configuration

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../config"
        )
    )
)

import generation_config as config


fake = Faker()

np.random.seed(42)
Faker.seed(42)



def generate_products():

    products = []


    for i in range(config.PRODUCT_COUNT):

        product_id = (
            f"PROD_{str(i+1).zfill(6)}"
        )


        product_name = (
            fake.catch_phrase()
        )


        category = np.random.choice(
            config.PRODUCT_CATEGORIES
        )


        supplier_id = (
            f"SUP_{str(np.random.randint(1, config.SUPPLIER_COUNT+1)).zfill(5)}"
        )


        unit_cost = round(
            np.random.uniform(
                50,
                5000
            ),
            2
        )


        markup_percentage = np.random.uniform(
            1.15,
            2.5
        )


        unit_price = round(
            unit_cost *
            markup_percentage,
            2
        )


        product_status = np.random.choice(
            [
                "Active",
                "Inactive",
                "Discontinued"
            ],
            p=[
                0.75,
                0.15,
                0.10
            ]
        )


        launch_date = fake.date_between(
            start_date=config.START_DATE,
            end_date=config.END_DATE
        )


        products.append({

            "product_id": product_id,

            "product_name": product_name,

            "category": category,

            "supplier_id": supplier_id,

            "unit_cost": unit_cost,

            "unit_price": unit_price,

            "product_status": product_status,

            "launch_date": launch_date

        })


    return pd.DataFrame(products)



def introduce_product_quality_issues(df):


    """
    Introduces realistic ERP master data problems.
    """


    # -------------------------------
    # Missing Values
    # -------------------------------


    missing_count = int(
        len(df) *
        config.MISSING_VALUE_RATE
    )


    for column in [
        "category",
        "supplier_id"
    ]:

        indexes = np.random.choice(
            df.index,
            missing_count,
            replace=False
        )


        df.loc[
            indexes,
            column
        ] = None



    # -------------------------------
    # Duplicate Products
    # -------------------------------


    duplicate_count = int(
        len(df) *
        config.DUPLICATE_RECORD_RATE
    )


    duplicates = df.sample(
        duplicate_count,
        random_state=42
    )


    df = pd.concat(
        [
            df,
            duplicates
        ],
        ignore_index=True
    )



    # -------------------------------
    # Invalid Categories
    # -------------------------------


    invalid_count = int(
        len(df) *
        config.INVALID_CATEGORY_RATE
    )


    invalid_indexes = np.random.choice(
        df.index,
        invalid_count,
        replace=False
    )


    df.loc[
        invalid_indexes,
        "category"
    ] = "Unknown Category"



    # -------------------------------
    # Price Anomalies
    # -------------------------------


    outlier_count = int(
        len(df) *
        config.OUTLIER_RATE
    )


    outlier_indexes = np.random.choice(
        df.index,
        outlier_count,
        replace=False
    )


    df.loc[
        outlier_indexes,
        "unit_price"
    ] *= 10



    # -------------------------------
    # Negative Cost Errors
    # -------------------------------


    error_count = int(
        len(df) *
        config.INVALID_CATEGORY_RATE
    )


    error_indexes = np.random.choice(
        df.index,
        error_count,
        replace=False
    )


    df.loc[
        error_indexes,
        "unit_cost"
    ] = -100


    return df



def save_products(df):


    output_file = os.path.join(
        os.path.dirname(__file__),
        "../output/raw_products.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Product dataset created"
    )

    print(
        f"Total records: {len(df)}"
    )



if __name__ == "__main__":


    print(
        "Generating product master data..."
    )


    products = generate_products()


    products = introduce_product_quality_issues(
        products
    )


    save_products(
        products
    )