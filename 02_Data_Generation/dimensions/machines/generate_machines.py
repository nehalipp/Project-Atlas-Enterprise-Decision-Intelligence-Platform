"""
Project Atlas: Enterprise Decision Intelligence Platform

Machine Master Data Generator

Purpose:
Generates manufacturing equipment master data.
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



np.random.seed(config.RANDOM_SEED)

Faker.seed(config.RANDOM_SEED)

fake=Faker()



def generate_machines():


    machines=[]


    for i in range(config.MACHINE_COUNT):


        purchase_date=fake.date_between(

            start_date=config.START_DATE,

            end_date=config.END_DATE

        )


        machines.append(

            {


            "machine_id":

                f"MACH_{str(i+1).zfill(6)}",


            "machine_name":

                f"{np.random.choice(config.MACHINE_TYPES)}-{i+1}",


            "machine_type":

                np.random.choice(
                    config.MACHINE_TYPES
                ),


            "manufacturer":

                np.random.choice(
                    config.MACHINE_MANUFACTURERS
                ),


            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",


            "purchase_date":

                purchase_date,


            "warranty_expiry":

                purchase_date,


            "expected_life_years":

                np.random.randint(
                    5,
                    25
                ),


            "machine_status":

                np.random.choice(
                    config.MACHINE_STATUS
                )

            }

        )


    return pd.DataFrame(machines)



def save_machines(df):


    output_path=os.path.join(

        os.path.dirname(__file__),

        "output"

    )


    os.makedirs(
        output_path,
        exist_ok=True
    )


    file=os.path.join(

        output_path,

        "raw_machines.csv"

    )


    df.to_csv(
        file,
        index=False
    )


    print(
        f"Machine file created: {file}"
    )


    print(
        f"Records: {len(df)}"
    )



if __name__=="__main__":


    print(
        "Generating machines..."
    )


    df=generate_machines()


    save_machines(df)