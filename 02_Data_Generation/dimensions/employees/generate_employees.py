"""
Project Atlas: Enterprise Decision Intelligence Platform

Employee Master Data Generator

Purpose:
Generates workforce data for HR analytics.
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

fake = Faker()



def generate_employees():

    employees=[]


    for i in range(config.EMPLOYEE_COUNT):


        employees.append(

            {


            "employee_id":

                f"EMP_{str(i+1).zfill(6)}",


            "employee_name":

                fake.name(),


            "department":

                np.random.choice(
                    config.DEPARTMENTS
                ),


            "job_title":

                np.random.choice(
                    config.JOB_TITLES
                ),


            "location_id":

                f"LOC_{np.random.randint(1,config.LOCATION_COUNT+1):05d}",


            "manager_id":

                f"EMP_{np.random.randint(1,config.EMPLOYEE_COUNT+1):06d}",


            "hire_date":

                fake.date_between(
                    start_date=config.START_DATE,
                    end_date=config.END_DATE
                ),


            "salary":

                round(
                    np.random.uniform(
                        45000,
                        180000
                    ),
                    2
                ),


            "employment_status":

                np.random.choice(
                    config.EMPLOYMENT_STATUS
                ),


            "performance_rating":

                round(
                    np.random.uniform(
                        1,
                        5
                    ),
                    2
                )


            }

        )


    return pd.DataFrame(employees)



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
        "department"
    ] = None



    return df



def save_employees(df):


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
        "raw_employees.csv"
    )


    df.to_csv(
        file,
        index=False
    )


    print(
        f"Employee file created: {file}"
    )


    print(
        f"Records: {len(df)}"
    )



if __name__=="__main__":


    print(
        "Generating employees..."
    )


    df=generate_employees()


    df=introduce_quality_issues(df)


    save_employees(df)