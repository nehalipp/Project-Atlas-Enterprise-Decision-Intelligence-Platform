"""
Project Atlas: Enterprise Decision Intelligence Platform

Account Dimension Generator

Creates financial chart of accounts.

Dataset:
dim_account
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


fake = Faker()



def generate_accounts():


    records=[]


    account_categories = [

        "Corporate",
        "Operations",
        "Manufacturing",
        "Sales",
        "Technology",
        "Human Resources"

    ]


    for i in range(config.ACCOUNT_COUNT):


        records.append(

            {


            "account_id":

                f"ACC_{str(i+1).zfill(5)}",



            "account_name":

                fake.bs().title(),



            "account_type":

                np.random.choice(

                    config.ACCOUNT_TYPES

                ),



            "account_category":

                np.random.choice(

                    account_categories

                ),



            "department":

                np.random.choice(

                    config.DEPARTMENTS

                ),



            "active_status":

                np.random.choice(

                    [

                        "Active",

                        "Inactive"

                    ],

                    p=[0.95,0.05]

                )

            }

        )


    return pd.DataFrame(records)




def save_accounts(df):


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

        "raw_accounts.csv"

    )


    df.to_csv(

        file,

        index=False

    )


    print(

        f"Accounts created: {file}"

    )


    print(

        f"Records: {len(df)}"

    )





if __name__=="__main__":


    print(
        "Generating accounts..."
    )


    df=generate_accounts()


    save_accounts(df)