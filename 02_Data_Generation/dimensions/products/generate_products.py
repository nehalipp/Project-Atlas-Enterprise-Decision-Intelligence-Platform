"""
Project Atlas

Product Master Data Generator
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



fake = Faker()

np.random.seed(config.RANDOM_SEED)

Faker.seed(config.RANDOM_SEED)




def generate_products():


    products=[]


    for i in range(config.PRODUCT_COUNT):


        products.append({

            "product_id":
                f"PROD_{str(i+1).zfill(5)}",

            "product_name":
                fake.catch_phrase(),

            "category":
                np.random.choice(
                    config.PRODUCT_CATEGORIES
                ),

            "unit_cost":
                round(
                    np.random.uniform(
                        50,
                        5000
                    ),
                    2
                ),

            "unit_price":
                round(
                    np.random.uniform(
                        100,
                        8000
                    ),
                    2
                ),

            "product_status":
                np.random.choice(
                    config.PRODUCT_STATUS
                )

        })


    return pd.DataFrame(products)




def save_output(df):


    path=os.path.join(

        os.path.dirname(__file__),
        "output/raw_products.csv"

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
        f"Products created: {path}"
    )





if __name__=="__main__":


    print(
        "Generating products..."
    )


    df=generate_products()

    save_output(df)