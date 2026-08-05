"""
Project Atlas: Enterprise Decision Intelligence Platform

Manufacturing Maintenance Fact Generator

Purpose:
Generates machine maintenance history.

Dataset:
fact_maintenance

Used for:
- Maintenance dashboard
- Machine reliability
- Downtime analysis
- Cost optimization
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
# Generate Maintenance Records
# --------------------------------------------------

def generate_maintenance():


    maintenance_records=[]



    for i in range(

        config.MAINTENANCE_EVENT_COUNT

    ):



        downtime=np.random.uniform(

            0.5,

            48

        )


        repair_cost=np.random.uniform(

            100,

            25000

        )



        maintenance_records.append(

            {


            "maintenance_id":

                f"MAINT_{str(i+1).zfill(7)}",



            "maintenance_date":

                fake.date_between(

                    start_date=config.START_DATE,

                    end_date=config.END_DATE

                ),



            "machine_id":

                f"MACH_{np.random.randint(1,config.MACHINE_COUNT+1):06d}",



            "maintenance_type":

                np.random.choice(

                    config.MAINTENANCE_TYPES

                ),



            "technician":

                fake.name(),



            "downtime_hours":

                round(

                    downtime,

                    2

                ),



            "repair_cost":

                round(

                    repair_cost,

                    2

                ),



            "maintenance_status":

                np.random.choice(

                    [
                        "Completed",
                        "Pending",
                        "Scheduled"
                    ],

                    p=[
                        0.85,
                        0.05,
                        0.10
                    ]

                )

            }

        )



    return pd.DataFrame(

        maintenance_records

    )



# --------------------------------------------------
# Quality Issues
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

        "technician"

    ]=None



    return df



# --------------------------------------------------
# Save
# --------------------------------------------------

def save_maintenance(df):


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

        "raw_maintenance.csv"

    )



    df.to_csv(

        file_path,

        index=False

    )



    print(

        f"Maintenance file created: {file_path}"

    )


    print(

        f"Records: {len(df)}"

    )



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__=="__main__":


    print(

        "Generating maintenance data..."

    )


    df=generate_maintenance()


    df=introduce_quality_issues(

        df

    )


    save_maintenance(

        df

    )