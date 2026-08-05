"""
Project Atlas: Enterprise Decision Intelligence Platform

Manufacturing Production Fact Generator

Purpose:
Generates manufacturing production transactions.

Dataset:
fact_production

Used for:
- Production dashboards
- Plant analytics
- Machine performance
- Quality analytics
"""


import pandas as pd
import numpy as np

from faker import Faker

import os
import sys



# --------------------------------------------------
# Import Configuration
# --------------------------------------------------

sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../../config"

        )

    )

)


import generation_config as config



# --------------------------------------------------
# Initialize
# --------------------------------------------------

np.random.seed(
    config.RANDOM_SEED
)

Faker.seed(
    config.RANDOM_SEED
)


fake = Faker()



# --------------------------------------------------
# Generate Production Data
# --------------------------------------------------

def generate_production():


    production_records = []


    for i in range(
        config.PRODUCTION_EVENT_COUNT
    ):


        units_produced = np.random.randint(
            50,
            500
        )


        production_hours = round(

            np.random.uniform(
                2,
                12
            ),

            2

        )


        defect_count = np.random.randint(
            0,
            int(units_produced * 0.05)
        )



        production_records.append(

            {


            "production_id":

                f"PROD_{str(i+1).zfill(7)}",



            "production_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "machine_id":

                f"MACH_{np.random.randint(1,config.MACHINE_COUNT+1):06d}",



            "product_id":

                f"PROD_{np.random.randint(1,config.PRODUCT_COUNT+1):05d}",



            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",



            "shift":

                np.random.choice(

                    [
                        "Morning",
                        "Evening",
                        "Night"
                    ]

                ),



            "units_produced":

                units_produced,



            "defect_count":

                defect_count,



            "defect_rate":

                round(

                    defect_count /
                    units_produced,

                    4

                ),



            "production_hours":

                production_hours,



            "production_status":

                np.random.choice(

                    config.PRODUCTION_STATUS,

                    p=[
                        0.90,
                        0.03,
                        0.07
                    ]

                )

            }

        )


    return pd.DataFrame(
        production_records
    )



# --------------------------------------------------
# Introduce Data Quality Issues
# --------------------------------------------------

def introduce_quality_issues(df):


    missing_count = int(

        len(df)
        *
        config.MISSING_VALUE_RATE

    )


    indexes=np.random.choice(

        df.index,

        missing_count,

        replace=False

    )


    df.loc[

        indexes,

        "production_status"

    ] = None



    duplicate_count=int(

        len(df)
        *
        config.DUPLICATE_RECORD_RATE

    )


    duplicates=df.sample(

        duplicate_count,

        random_state=42

    )


    df=pd.concat(

        [
            df,
            duplicates
        ],

        ignore_index=True

    )


    return df



# --------------------------------------------------
# Save
# --------------------------------------------------

def save_production(df):


    output_path=os.path.join(

        os.path.dirname(__file__),

        "output"

    )


    os.makedirs(

        output_path,

        exist_ok=True

    )



    file_path=os.path.join(

        output_path,

        "raw_production.csv"

    )



    df.to_csv(

        file_path,

        index=False

    )


    print(

        f"Production file created: {file_path}"

    )


    print(

        f"Records: {len(df)}"

    )



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__=="__main__":


    print(
        "Generating production data..."
    )


    df=generate_production()


    df=introduce_quality_issues(
        df
    )


    save_production(
        df
    )