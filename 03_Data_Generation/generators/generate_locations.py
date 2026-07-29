"""
Project Atlas: Enterprise Decision Intelligence Platform

Location Master Data Generator

Purpose:
Generates enterprise facility and geographic data
for analytics and reporting.
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



def generate_locations():

    locations = []


    location_types = [
        "Headquarters",
        "Manufacturing Plant",
        "Distribution Center",
        "Warehouse",
        "Service Center"
    ]


    for i in range(config.LOCATION_COUNT):


        location_id = (
            f"LOC_{str(i+1).zfill(5)}"
        )


        country = np.random.choice(
            config.COUNTRIES
        )


        region = np.random.choice(
            config.REGIONS
        )


        city = fake.city()


        location_type = np.random.choice(
            location_types,
            p=[
                0.10,
                0.30,
                0.25,
                0.25,
                0.10
            ]
        )


        facility_name = (
            f"{city} {location_type}"
        )


        operating_status = np.random.choice(
            [
                "Active",
                "Inactive"
            ],
            p=[
                0.90,
                0.10
            ]
        )


        opening_date = fake.date_between(
            start_date=config.START_DATE,
            end_date=config.END_DATE
        )


        locations.append({

            "location_id": location_id,

            "facility_name": facility_name,

            "location_type": location_type,

            "city": city,

            "country": country,

            "region": region,

            "operating_status": operating_status,

            "opening_date": opening_date

        })


    return pd.DataFrame(locations)




def introduce_location_quality_issues(df):


    """
    Introduces geographic master data issues.
    """


    # Missing values

    missing_count = int(
        len(df) *
        config.MISSING_VALUE_RATE
    )


    for column in [
        "city",
        "region"
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



    # Duplicate facilities

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


    # Invalid region values

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
        "region"
    ] = "Unknown Region"


    return df




def save_locations(df):


    output_file = os.path.join(
        os.path.dirname(__file__),
        "../output/raw_locations.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Location dataset created"
    )

    print(
        f"Total records: {len(df)}"
    )




if __name__ == "__main__":


    print(
        "Generating location master data..."
    )


    locations = generate_locations()


    locations = introduce_location_quality_issues(
        locations
    )


    save_locations(
        locations
    )