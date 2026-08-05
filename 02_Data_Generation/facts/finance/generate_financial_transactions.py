"""
Project Atlas: Enterprise Decision Intelligence Platform

Financial Transaction Fact Generator

Purpose:
Generates enterprise financial transactions.

Dataset:
fact_financial_transactions

Used for:
- Finance dashboards
- Expense analysis
- Revenue analytics
- Profitability reporting
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
# Initialization
# --------------------------------------------------

np.random.seed(
    config.RANDOM_SEED
)

Faker.seed(
    config.RANDOM_SEED
)

fake = Faker()



# --------------------------------------------------
# Generate Financial Transactions
# --------------------------------------------------

def generate_financial_transactions():


    transactions=[]



    for i in range(

        config.FINANCIAL_TRANSACTION_COUNT

    ):



        transaction_type=np.random.choice(

            config.TRANSACTION_TYPES,

            p=[
                0.35,
                0.25,
                0.15,
                0.20,
                0.05
            ]

        )


        if transaction_type=="Revenue":

            amount=np.random.uniform(
                500,
                100000
            )

        else:

            amount=np.random.uniform(
                100,
                50000
            )



        transactions.append(

            {


            "transaction_id":

                f"FIN_{str(i+1).zfill(7)}",



            "transaction_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "account_id":

                f"ACC_{np.random.randint(1,config.ACCOUNT_COUNT+1):05d}",



            "department":

                np.random.choice(

                    config.DEPARTMENTS

                ),



            "transaction_type":

                transaction_type,



            "amount":

                round(

                    amount,

                    2

                ),



            "currency":

                np.random.choice(

                    [
                        "USD",
                        "EUR",
                        "SEK",
                        "INR"
                    ]

                ),



            "vendor":

                fake.company(),



            "payment_status":

                np.random.choice(

                    [
                        "Completed",
                        "Pending",
                        "Failed"
                    ],

                    p=[
                        0.90,
                        0.08,
                        0.02
                    ]

                )

            }

        )


    return pd.DataFrame(
        transactions
    )



# --------------------------------------------------
# Data Quality Issues
# --------------------------------------------------

def introduce_quality_issues(df):


    missing_count=int(

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

        "vendor"

    ]=None



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

def save_transactions(df):


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

        "raw_financial_transactions.csv"

    )



    df.to_csv(

        file_path,

        index=False

    )



    print(

        f"Financial transactions created: {file_path}"

    )


    print(

        f"Records: {len(df)}"

    )



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__=="__main__":


    print(

        "Generating financial transactions..."

    )


    df=generate_financial_transactions()


    df=introduce_quality_issues(

        df

    )


    save_transactions(

        df

    )