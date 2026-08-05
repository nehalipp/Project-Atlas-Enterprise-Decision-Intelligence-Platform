"""
Project Atlas

Customer Master Data Generator

Generates synthetic CRM customer data
with intentional enterprise data quality issues.
"""


import pandas as pd
import numpy as np

from faker import Faker
from datetime import datetime

import os
import sys



# -----------------------------------------
# Import configuration
# -----------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../config"
        )
    )
)

import generation_config as config



fake = Faker()

np.random.seed(config.RANDOM_SEED)

Faker.seed(config.RANDOM_SEED)



def generate_customers():

    customers = []


    for i in range(config.CUSTOMER_COUNT):

        customers.append({

            "customer_id":
                f"CUST_{str(i+1).zfill(6)}",

            "customer_name":
                fake.company(),

            "industry":
                np.random.choice(
                    config.INDUSTRIES
                ),

            "customer_segment":
                np.random.choice(
                    config.CUSTOMER_SEGMENTS
                ),

            "country":
                np.random.choice(
                    config.COUNTRIES
                ),

            "region":
                np.random.choice(
                    config.REGIONS
                ),

            "customer_since":
                fake.date_between(
                    start_date=config.START_DATE,
                    end_date=config.END_DATE
                )

        })


    return pd.DataFrame(customers)




def introduce_quality_issues(df):


    missing_count = int(
        len(df)
        *
        config.MISSING_VALUE_RATE
    )


    for col in [

        "industry",
        "customer_segment",
        "country"

    ]:

        indexes = np.random.choice(
            df.index,
            missing_count,
            replace=False
        )

        df.loc[indexes,col] = None



    duplicate_count = int(

        len(df)
        *
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




def save_output(df):


    output_path = os.path.join(

        os.path.dirname(__file__),
        "output/raw_customers.csv"

    )


    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )


    df.to_csv(
        output_path,
        index=False
    )


    print(
        f"Customer file created: {output_path}"
    )

    print(
        f"Records: {len(df)}"
    )




if __name__ == "__main__":


    print(
        "Generating customers..."
    )


    df = generate_customers()


    df = introduce_quality_issues(
        df
    )


    save_output(df)