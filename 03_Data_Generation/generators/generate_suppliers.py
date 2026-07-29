"""
Project Atlas: Enterprise Decision Intelligence Platform

Supplier Master Data Generator

Purpose:
Generates realistic ERP supplier data with
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



def generate_suppliers():

    suppliers = []


    supplier_categories = [
        "Raw Materials",
        "Technology Vendor",
        "Equipment Supplier",
        "Logistics Provider",
        "Professional Services",
        "Maintenance Provider"
    ]


    contract_statuses = [
        "Active",
        "Expired",
        "Pending Renewal"
    ]


    for i in range(config.SUPPLIER_COUNT):

        supplier_id = (
            f"SUP_{str(i+1).zfill(5)}"
        )


        supplier_name = fake.company()


        country = np.random.choice(
            config.COUNTRIES
        )


        region = np.random.choice(
            config.REGIONS
        )


        category = np.random.choice(
            supplier_categories
        )


        performance_rating = round(
            np.random.uniform(
                1,
                5
            ),
            2
        )


        contract_status = np.random.choice(
            contract_statuses,
            p=[
                0.75,
                0.15,
                0.10
            ]
        )


        supplier_since = fake.date_between(
            start_date=config.START_DATE,
            end_date=config.END_DATE
        )


        suppliers.append({

            "supplier_id": supplier_id,

            "supplier_name": supplier_name,

            "supplier_category": category,

            "country": country,

            "region": region,

            "performance_rating": performance_rating,

            "contract_status": contract_status,

            "supplier_since": supplier_since

        })


    return pd.DataFrame(suppliers)




def introduce_supplier_quality_issues(df):

    """
    Introduces realistic procurement data problems.
    """


    # ---------------------------------
    # Missing supplier information
    # ---------------------------------

    missing_count = int(
        len(df) *
        config.MISSING_VALUE_RATE
    )


    for column in [
        "country",
        "performance_rating"
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



    # ---------------------------------
    # Country inconsistencies
    # ---------------------------------

    country_mapping = {

        "United States": [
            "USA",
            "US",
            "United States"
        ],

        "United Kingdom": [
            "UK",
            "United Kingdom"
        ]

    }


    for standard, values in country_mapping.items():

        mask = (
            df["country"] == standard
        )


        df.loc[
            mask,
            "country"
        ] = np.random.choice(
            values,
            size=mask.sum()
        )



    # ---------------------------------
    # Duplicate suppliers
    # ---------------------------------

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



    # ---------------------------------
    # Invalid performance ratings
    # ---------------------------------

    invalid_count = int(
        len(df) *
        config.INVALID_CATEGORY_RATE
    )


    indexes = np.random.choice(
        df.index,
        invalid_count,
        replace=False
    )


    df.loc[
        indexes,
        "performance_rating"
    ] = 10



    return df




def save_suppliers(df):


    output_file = os.path.join(
        os.path.dirname(__file__),
        "../output/raw_suppliers.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Supplier dataset created"
    )

    print(
        f"Total records: {len(df)}"
    )




if __name__ == "__main__":


    print(
        "Generating supplier master data..."
    )


    suppliers = generate_suppliers()


    suppliers = introduce_supplier_quality_issues(
        suppliers
    )


    save_suppliers(
        suppliers
    )