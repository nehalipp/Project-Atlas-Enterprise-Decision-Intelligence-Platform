"""
Project Atlas: Enterprise Decision Intelligence Platform

Customer Master Data Generator

Purpose:
Generates realistic CRM customer data with intentional
data quality issues.
"""

import pandas as pd
import numpy as np

from faker import Faker
from datetime import datetime

import sys
import os


# Allow importing configuration file
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../config"
        )
    )
)

import generation_config as config


# Initialize Faker
fake = Faker()

# Reproducibility
np.random.seed(42)
Faker.seed(42)


def generate_customers():

    customers = []

    for i in range(config.CUSTOMER_COUNT):

        customer_id = f"CUST_{str(i+1).zfill(6)}"

        customer_name = fake.company()

        industry = np.random.choice(
            config.INDUSTRIES
        )

        segment = np.random.choice(
            config.CUSTOMER_SEGMENTS,
            p=[0.25,0.35,0.25,0.15]
        )

        country = np.random.choice(
            config.COUNTRIES
        )

        region = np.random.choice(
            config.REGIONS
        )

        customer_since = fake.date_between(
            start_date=config.START_DATE,
            end_date=config.END_DATE
        )


        customers.append({

            "customer_id": customer_id,

            "customer_name": customer_name,

            "industry": industry,

            "customer_segment": segment,

            "country": country,

            "region": region,

            "customer_since": customer_since

        })


    df = pd.DataFrame(customers)


    return df



def introduce_data_quality_issues(df):

    """
    Introduces realistic CRM data problems.
    """


    # ----------------------------------
    # Missing Values
    # ----------------------------------

    missing_rows = int(
        len(df) *
        config.MISSING_VALUE_RATE
    )


    for column in [
        "industry",
        "customer_segment",
        "country"
    ]:

        indexes = np.random.choice(
            df.index,
            missing_rows,
            replace=False
        )

        df.loc[indexes, column] = None



    # ----------------------------------
    # Country Inconsistency
    # ----------------------------------

    country_mapping = {

        "United States": [
            "USA",
            "US",
            "U.S.A.",
            "United States"
        ],

        "United Kingdom": [
            "UK",
            "U.K.",
            "United Kingdom"
        ]

    }


    for standard, variations in country_mapping.items():

        mask = df["country"] == standard

        df.loc[
            mask,
            "country"
        ] = np.random.choice(
            variations,
            size=mask.sum()
        )



    # ----------------------------------
    # Duplicate Customers
    # ----------------------------------

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


    # ----------------------------------
    # Invalid Categories
    # ----------------------------------

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
        "customer_segment"
    ] = "Unknown"



    return df



def save_customer_data(df):

    output_file = os.path.join(
        os.path.dirname(__file__),
        "../output/raw_customers.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        f"Customer dataset created: {output_file}"
    )

    print(
        f"Total records: {len(df)}"
    )



if __name__ == "__main__":


    print(
        "Generating customer master data..."
    )


    customers = generate_customers()


    customers = introduce_data_quality_issues(
        customers
    )


    save_customer_data(
        customers
    )