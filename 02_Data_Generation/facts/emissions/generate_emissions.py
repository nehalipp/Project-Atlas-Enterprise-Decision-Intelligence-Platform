"""
Project Atlas: Enterprise Decision Intelligence Platform

Emission Fact Generator

Purpose:
Generates carbon emission measurements.

Dataset:
fact_emissions
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



def generate_emissions():


    records=[]



    for i in range(

        config.EMISSION_RECORD_COUNT

    ):


        carbon=np.random.uniform(

            100,

            100000

        )



        records.append(

            {


            "emission_id":

                f"EMISSION_{str(i+1).zfill(7)}",



            "measurement_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",



            "emission_type":

                np.random.choice(

                    config.EMISSION_TYPES

                ),



            "scope":

                np.random.choice(

                    config.EMISSION_SCOPES

                ),



            "carbon_emission_tons":

                round(

                    carbon,

                    2

                )

            }

        )


    return pd.DataFrame(records)



def save_emissions(df):


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

        "raw_emissions.csv"

    )


    df.to_csv(

        file,

        index=False

    )


    print(

        f"Emission file created: {file}"

    )


    print(

        f"Records: {len(df)}"

    )



if __name__=="__main__":


    print(
        "Generating emissions..."
    )


    df=generate_emissions()


    save_emissions(df)