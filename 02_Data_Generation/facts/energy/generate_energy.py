"""
Project Atlas: Enterprise Decision Intelligence Platform

Energy Consumption Fact Generator

Purpose:
Generates facility energy consumption data.

Dataset:
fact_energy_consumption
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



def generate_energy():


    records=[]


    for i in range(

        config.ENERGY_RECORD_COUNT

    ):


        consumption=np.random.uniform(

            500,

            50000

        )


        records.append(

            {


            "energy_id":

                f"ENERGY_{str(i+1).zfill(7)}",



            "measurement_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",



            "energy_source":

                np.random.choice(

                    config.ENERGY_SOURCES

                ),



            "consumption_kwh":

                round(

                    consumption,

                    2

                ),



            "energy_cost":

                round(

                    consumption *

                    np.random.uniform(
                        0.05,
                        0.25
                    ),

                    2

                )

            }

        )


    return pd.DataFrame(records)



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

        "energy_source"

    ]=None


    return df



def save_energy(df):


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

        "raw_energy_consumption.csv"

    )


    df.to_csv(

        file,

        index=False

    )


    print(

        f"Energy file created: {file}"

    )


    print(

        f"Records: {len(df)}"

    )



if __name__=="__main__":


    print(
        "Generating energy consumption..."
    )


    df=generate_energy()


    df=introduce_quality_issues(df)


    save_energy(df)