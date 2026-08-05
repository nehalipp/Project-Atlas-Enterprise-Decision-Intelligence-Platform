"""
Project Atlas: Enterprise Decision Intelligence Platform

Waste Management Fact Generator

Purpose:
Generates operational waste data.

Dataset:
fact_waste
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



def generate_waste():


    records=[]


    for i in range(

        config.WASTE_RECORD_COUNT

    ):


        records.append(

            {


            "waste_id":

                f"WASTE_{str(i+1).zfill(7)}",



            "measurement_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",



            "waste_type":

                np.random.choice(

                    config.WASTE_TYPES

                ),



            "quantity_tons":

                round(

                    np.random.uniform(

                        0.1,

                        500

                    ),

                    2

                ),



            "disposal_method":

                np.random.choice(

                    config.DISPOSAL_METHODS

                )

            }

        )


    return pd.DataFrame(records)



def save_waste(df):


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

        "raw_waste.csv"

    )


    df.to_csv(

        file,

        index=False

    )


    print(

        f"Waste file created: {file}"

    )


    print(

        f"Records: {len(df)}"

    )



if __name__=="__main__":


    print(
        "Generating waste data..."
    )


    df=generate_waste()


    save_waste(df)