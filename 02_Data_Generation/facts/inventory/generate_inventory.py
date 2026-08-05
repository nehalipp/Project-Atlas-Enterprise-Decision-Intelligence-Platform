"""
Project Atlas: Enterprise Decision Intelligence Platform

Inventory Fact Generator

Dataset:
fact_inventory

Purpose:
Generates warehouse inventory snapshots.
"""


import pandas as pd
import numpy as np

from faker import Faker

import os
import sys



sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../../config"

        )

    )

)


import generation_config as config



np.random.seed(
    config.RANDOM_SEED
)


Faker.seed(
    config.RANDOM_SEED
)


fake=Faker()



def generate_inventory():


    records=[]


    for i in range(

        config.INVENTORY_RECORD_COUNT

    ):


        quantity=np.random.randint(

            0,

            5000

        )


        unit_cost=np.random.uniform(

            10,

            5000

        )


        records.append(

            {


            "inventory_id":

                f"INV_{str(i+1).zfill(7)}",



            "date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "product_id":

                f"PROD_{np.random.randint(1,config.PRODUCT_COUNT+1):05d}",



            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",



            "inventory_quantity":

                quantity,



            "unit_cost":

                round(

                    unit_cost,

                    2

                ),



            "inventory_value":

                round(

                    quantity*unit_cost,

                    2

                ),



            "stock_status":

                np.random.choice(

                    [

                        "In Stock",

                        "Low Stock",

                        "Out of Stock"

                    ],

                    p=[

                        .75,

                        .20,

                        .05

                    ]

                )

            }

        )


    return pd.DataFrame(records)




def save_inventory(df):


    output=os.path.join(

        os.path.dirname(__file__),

        "output"

    )


    os.makedirs(

        output,

        exist_ok=True

    )


    file=os.path.join(

        output,

        "raw_inventory.csv"

    )


    df.to_csv(

        file,

        index=False

    )


    print(

        f"Inventory created: {file}"

    )


    print(

        f"Records: {len(df)}"

    )





if __name__=="__main__":


    print(

        "Generating inventory..."

    )


    df=generate_inventory()


    save_inventory(df)