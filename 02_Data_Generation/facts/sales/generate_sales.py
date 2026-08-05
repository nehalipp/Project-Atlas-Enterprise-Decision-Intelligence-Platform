"""
Project Atlas

Sales Transaction Data Generator

Generates synthetic sales transaction data
for enterprise analytics.
"""


import pandas as pd
import numpy as np

from faker import Faker

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



def generate_sales():


    sales=[]


    for i in range(config.SALES_TRANSACTION_COUNT):


        quantity = np.random.randint(
            1,
            20
        )


        unit_price = round(
            np.random.uniform(
                100,
                10000
            ),
            2
        )


        discount = round(

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

            quantity
            *
            unit_price
            *
            (1 - discount/100),

            2

        )



        sales.append({

            "transaction_id":
                f"TXN_{str(i+1).zfill(8)}",


            "customer_id":
                f"CUST_{np.random.randint(1,config.CUSTOMER_COUNT):06d}",


            "product_id":
                f"PROD_{np.random.randint(1,config.PRODUCT_COUNT):05d}",


            "location_id":
                f"LOC_{np.random.randint(1,config.LOCATION_COUNT):04d}",


            "transaction_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),


            "quantity":

                quantity,


            "unit_price":

                unit_price,


            "discount_percentage":

                discount,


            "revenue":

                revenue,


            "sales_channel":

                np.random.choice(

                    config.SALES_CHANNELS

                )

        })


    return pd.DataFrame(sales)




def introduce_quality_issues(df):


    # Missing values

    missing_count = int(

        len(df)
        *
        config.MISSING_VALUE_RATE

    )


    indexes = np.random.choice(

        df.index,

        missing_count,

        replace=False

    )


    df.loc[
        indexes,
        "customer_id"
    ] = None



    # Negative quantities

    error_count = int(

        len(df)
        *
        config.OUTLIER_RATE

    )


    indexes = np.random.choice(

        df.index,

        error_count,

        replace=False

    )


    df.loc[

        indexes,

        "quantity"

    ] = -1



    # Duplicate transactions


    duplicate_count = int(

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





def save_output(df):


    path=os.path.join(

        os.path.dirname(__file__),

        "output/raw_sales_transactions.csv"

    )


    os.makedirs(

        os.path.dirname(path),

        exist_ok=True

    )


    df.to_csv(

        path,

        index=False

    )


    print(

        f"Sales file created: {path}"

    )


    print(

        f"Records: {len(df)}"

    )





if __name__=="__main__":


    print(
        "Generating sales transactions..."
    )


    df=generate_sales()


    df=introduce_quality_issues(df)


    save_output(df)