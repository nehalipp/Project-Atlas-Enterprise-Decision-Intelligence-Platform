"""
Project Atlas: Enterprise Decision Intelligence Platform

Sales Transaction Generator

Purpose:
Generates enterprise transactional sales data
connecting customers, products, and locations.
"""


import pandas as pd
import numpy as np

from faker import Faker
from datetime import datetime

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



def generate_sales_transactions():


    sales = []


    sales_channels = [
        "Direct Sales",
        "Online",
        "Partner",
        "Retail"
    ]


    for i in range(
        config.SALES_TRANSACTION_COUNT
    ):


        transaction_id = (
            f"TXN_{str(i+1).zfill(8)}"
        )


        transaction_date = fake.date_between(
            start_date=config.START_DATE,
            end_date=config.END_DATE
        )


        customer_id = (
            f"CUST_{str(np.random.randint(1, config.CUSTOMER_COUNT+1)).zfill(6)}"
        )


        product_id = (
            f"PROD_{str(np.random.randint(1, config.PRODUCT_COUNT+1)).zfill(6)}"
        )


        location_id = (
            f"LOC_{str(np.random.randint(1, config.LOCATION_COUNT+1)).zfill(5)}"
        )


        quantity = np.random.randint(
            1,
            25
        )


        unit_price = round(
            np.random.uniform(
                50,
                5000
            ),
            2
        )


        discount_percentage = round(
            np.random.choice(
                [
                    0,
                    5,
                    10,
                    15,
                    20
                ]
            ),
            2
        )


        revenue = round(
            quantity *
            unit_price *
            (
                1 -
                discount_percentage / 100
            ),
            2
        )


        sales_channel = np.random.choice(
            sales_channels
        )


        sales.append({

            "transaction_id": transaction_id,

            "transaction_date": transaction_date,

            "customer_id": customer_id,

            "product_id": product_id,

            "location_id": location_id,

            "quantity": quantity,

            "unit_price": unit_price,

            "discount_percentage": discount_percentage,

            "revenue": revenue,

            "sales_channel": sales_channel

        })


    return pd.DataFrame(sales)




def introduce_sales_quality_issues(df):


    """
    Introduces transactional data problems.
    """


    # Missing product references

    missing_count = int(
        len(df) *
        config.MISSING_VALUE_RATE
    )


    indexes = np.random.choice(
        df.index,
        missing_count,
        replace=False
    )


    df.loc[
        indexes,
        "product_id"
    ] = None



    # Negative quantities

    error_count = int(
        len(df) *
        config.INVALID_CATEGORY_RATE
    )


    indexes = np.random.choice(
        df.index,
        error_count,
        replace=False
    )


    df.loc[
        indexes,
        "quantity"
    ] = -5



    # Revenue calculation errors

    indexes = np.random.choice(
        df.index,
        error_count,
        replace=False
    )


    df.loc[
        indexes,
        "revenue"
    ] *= 5



    # Duplicate transactions

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


    return df




def save_sales(df):


    output_file = os.path.join(
        os.path.dirname(__file__),
        "../output/raw_sales_transactions.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Sales transaction dataset created"
    )

    print(
        f"Total records: {len(df)}"
    )




if __name__ == "__main__":


    print(
        "Generating sales transactions..."
    )


    sales = generate_sales_transactions()


    sales = introduce_sales_quality_issues(
        sales
    )


    save_sales(
        sales
    )