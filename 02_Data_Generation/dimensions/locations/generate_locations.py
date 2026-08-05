"""
Project Atlas: Enterprise Decision Intelligence Platform

Location Master Data Generator

Dataset:
dim_location

Purpose:
Generates realistic enterprise location master data.

Includes:
- Manufacturing Plants
- Warehouses
- Distribution Centers
- Corporate Offices
- Research Facilities

Geography:
Country -> Region -> State -> City -> Coordinates
"""


import pandas as pd
import numpy as np

from faker import Faker

import os
import sys



# =====================================================
# Import Configuration
# =====================================================


sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../../config"

        )

    )

)


import generation_config as config



# =====================================================
# Initialization
# =====================================================


np.random.seed(
    config.RANDOM_SEED
)


Faker.seed(
    config.RANDOM_SEED
)


fake = Faker()



# =====================================================
# Generate Locations
# =====================================================


def generate_locations():


    locations = []



    for i in range(config.LOCATION_COUNT):


        # -----------------------------
        # Select Country
        # -----------------------------


        country = np.random.choice(

            config.COUNTRIES

        )


        country_details = (

            config.COUNTRY_LOCATION_MAP[country]

        )



        # -----------------------------
        # Select Geography
        # -----------------------------


        city = np.random.choice(

            country_details["cities"]

        )


        state = np.random.choice(

            country_details["states"]

        )


        region = country_details["region"]



        # -----------------------------
        # Validate Coordinates
        # -----------------------------


        if city not in config.CITY_COORDINATES:

            raise ValueError(

                f"Missing coordinates for city: {city}"

            )



        coordinates = (

            config.CITY_COORDINATES[city]

        )



        # -----------------------------
        # Create Facility
        # -----------------------------


        location_type = np.random.choice(

            config.LOCATION_TYPES

        )


        locations.append(

            {


                "location_id":

                    f"LOC_{str(i+1).zfill(5)}",



                "facility_name":

                    f"{city} {location_type}",



                "location_type":

                    location_type,



                "city":

                    city,



                "state":

                    state,



                "country":

                    country,



                "region":

                    region,



                "latitude":

                    coordinates["latitude"],



                "longitude":

                    coordinates["longitude"],



                "operating_status":

                    np.random.choice(

                        config.OPERATING_STATUS,

                        p=[

                            0.85,

                            0.05,

                            0.10

                        ]

                    ),



                "opening_date":

                    fake.date_between(

                        start_date=config.START_DATE,

                        end_date=config.END_DATE

                    )


            }

        )



    return pd.DataFrame(locations)





# =====================================================
# Introduce Data Quality Issues
# =====================================================


def introduce_quality_issues(df):


    # Missing values

    missing_count = int(

        len(df)

        *

        config.MISSING_VALUE_RATE

    )



    missing_indexes = np.random.choice(

        df.index,

        missing_count,

        replace=False

    )



    df.loc[

        missing_indexes,

        "region"

    ] = None



    # Duplicate locations

    duplicate_count = int(

        len(df)

        *

        config.DUPLICATE_RECORD_RATE

    )



    duplicates = df.sample(

        duplicate_count,

        random_state=config.RANDOM_SEED

    )



    df = pd.concat(

        [

            df,

            duplicates

        ],

        ignore_index=True

    )



    return df





# =====================================================
# Save Output
# =====================================================


def save_locations(df):


    output_folder = os.path.join(

        os.path.dirname(__file__),

        "output"

    )



    os.makedirs(

        output_folder,

        exist_ok=True

    )



    output_file = os.path.join(

        output_folder,

        "raw_locations.csv"

    )



    df.to_csv(

        output_file,

        index=False

    )



    print(

        f"Location file created: {output_file}"

    )


    print(

        f"Records: {len(df)}"

    )





# =====================================================
# Main Execution
# =====================================================


if __name__ == "__main__":


    print(

        "Generating locations..."

    )



    locations = generate_locations()



    locations = introduce_quality_issues(

        locations

    )



    save_locations(

        locations

    )