"""
Project Atlas: Enterprise Decision Intelligence Platform

Budget Planning Fact Generator

Purpose:
Generates departmental budget planning data.

Dataset:
fact_budget

Used for:
- Budget vs actual analysis
- Department spending dashboard
- Financial planning analytics
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



np.random.seed(
    config.RANDOM_SEED
)

Faker.seed(
    config.RANDOM_SEED
)


fake=Faker()



# --------------------------------------------------
# Generate Budget Data
# --------------------------------------------------

def generate_budget():


    budgets=[]



    for i in range(

        config.BUDGET_COUNT

    ):



        budget_amount=np.random.uniform(

            50000,

            5000000

        )


        budgets.append(

            {


            "budget_id":

                f"BUD_{str(i+1).zfill(6)}",



            "fiscal_year":

                np.random.choice(

                    [
                        2023,
                        2024,
                        2025,
                        2026
                    ]

                ),



            "department":

                np.random.choice(

                    config.DEPARTMENTS

                ),



            "account_type":

                np.random.choice(

                    config.ACCOUNT_TYPES

                ),



            "budget_amount":

                round(

                    budget_amount,

                    2

                ),



            "approved_by":

                fake.name(),



            "budget_status":

                np.random.choice(

                    [
                        "Approved",
                        "Draft",
                        "Rejected"
                    ],

                    p=[
                        0.85,
                        0.10,
                        0.05
                    ]

                )

            }

        )



    return pd.DataFrame(
        budgets
    )



# --------------------------------------------------
# Save
# --------------------------------------------------

def save_budget(df):


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

        "raw_budget.csv"

    )



    df.to_csv(

        file_path,

        index=False

    )



    print(

        f"Budget file created: {file_path}"

    )


    print(

        f"Records: {len(df)}"

    )



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__=="__main__":


    print(

        "Generating budget data..."

    )


    df=generate_budget()


    save_budget(

        df

    )