"""
Project Atlas: Enterprise Decision Intelligence Platform

Employee Master Data Generator

Purpose:
Generates synthetic HR employee data with
realistic enterprise data quality issues.
"""


import pandas as pd
import numpy as np

from faker import Faker
from datetime import datetime

import sys
import os


# Import configuration

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../config"
        )
    )
)

import generation_config as config


fake = Faker()

np.random.seed(42)
Faker.seed(42)



def generate_employees():

    employees = []


    employment_statuses = [
        "Active",
        "Inactive",
        "On Leave",
        "Terminated"
    ]


    salary_bands = [
        "Entry Level",
        "Mid Level",
        "Senior Level",
        "Executive"
    ]


    for i in range(config.EMPLOYEE_COUNT):


        employee_id = (
            f"EMP_{str(i+1).zfill(6)}"
        )


        employee_name = fake.name()


        department = np.random.choice(
            config.DEPARTMENTS
        )


        job_title = np.random.choice(
            config.JOB_TITLES
        )


        location_id = (
            f"LOC_{str(np.random.randint(1, config.LOCATION_COUNT+1)).zfill(5)}"
        )
        hire_date = fake.date_between(
            start_date=datetime(
                2015,
                1,
                1
            ),
            end_date=config.END_DATE
        )

        employment_status = np.random.choice(
            employment_statuses,
            p=[
                0.80,
                0.05,
                0.05,
                0.10
            ]
        )


        salary_band = np.random.choice(
            salary_bands,
            p=[
                0.30,
                0.40,
                0.25,
                0.05
            ]
        )


        manager_id = (
            f"EMP_{str(np.random.randint(1, config.EMPLOYEE_COUNT+1)).zfill(6)}"
        )


        employees.append({

            "employee_id": employee_id,

            "employee_name": employee_name,

            "department": department,

            "job_title": job_title,

            "location_id": location_id,

            "hire_date": hire_date,

            "employment_status": employment_status,

            "salary_band": salary_band,

            "manager_id": manager_id

        })


    return pd.DataFrame(employees)




def introduce_employee_quality_issues(df):


    """
    Introduces HR system data problems.
    """


    # Missing department values

    missing_count = int(
        len(df) *
        config.MISSING_VALUE_RATE
    )


    indexes = np.random.choice(
        df.index,
        missing_count,
        replace=False
    )


    df.loc[
        indexes,
        "department"
    ] = None



    # Missing manager assignments

    indexes = np.random.choice(
        df.index,
        missing_count,
        replace=False
    )


    df.loc[
        indexes,
        "manager_id"
    ] = None



    # Duplicate employee records

    duplicate_count = int(
        len(df) *
        config.DUPLICATE_RECORD_RATE
    )


    duplicates = df.sample(
        duplicate_count,
        random_state=42
    )


    df = pd.concat(
        [
            df,
            duplicates
        ],
        ignore_index=True
    )



    # Invalid job titles

    invalid_count = int(
        len(df) *
        config.INVALID_CATEGORY_RATE
    )


    indexes = np.random.choice(
        df.index,
        invalid_count,
        replace=False
    )


    df.loc[
        indexes,
        "job_title"
    ] = "Unknown Role"



    return df




def save_employees(df):


    output_file = os.path.join(
        os.path.dirname(__file__),
        "../output/raw_employees.csv"
    )


    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Employee dataset created"
    )


    print(
        f"Total records: {len(df)}"
    )




if __name__ == "__main__":


    print(
        "Generating employee master data..."
    )


    employees = generate_employees()


    employees = introduce_employee_quality_issues(
        employees
    )


    save_employees(
        employees
    )
