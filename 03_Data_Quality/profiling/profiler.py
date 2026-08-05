"""
Project Atlas: Enterprise Decision Intelligence Platform

Generic Data Profiling Engine

Purpose:
Reusable profiling framework to analyze all
enterprise datasets generated in 02_Data_Generation.

Checks:
- Dataset availability
- Row count
- Column count
- Data types
- Missing values
- Duplicate records
- Unique values
- Numeric statistics
- Data quality score
"""


import os
import json
import pandas as pd
import numpy as np



# -----------------------------------------------------
# Profile Dataset
# -----------------------------------------------------

def profile_dataset(
        dataset_name,
        file_path
):


    print(
        f"Profiling {dataset_name}..."
    )


    if not os.path.exists(file_path):

        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )



    # Load dataset

    df = pd.read_csv(
        file_path
    )


    total_rows = len(df)

    total_columns = len(df.columns)



    # -------------------------------------------------
    # Missing Values
    # -------------------------------------------------

    missing_values = (
        df.isnull()
        .sum()
        .to_dict()
    )


    total_missing = (
        df.isnull()
        .sum()
        .sum()
    )


    missing_percentage = round(
        (
            total_missing /
            (total_rows * total_columns)
        )
        *
        100,
        2
    )



    # -------------------------------------------------
    # Duplicate Records
    # -------------------------------------------------

    duplicate_count = (
        df.duplicated()
        .sum()
    )


    duplicate_percentage = round(
        (
            duplicate_count /
            total_rows
        )
        *
        100,
        2
    )



    # -------------------------------------------------
    # Data Types
    # -------------------------------------------------

    data_types = {

        column:
        str(dtype)

        for column, dtype
        in df.dtypes.items()

    }



    # -------------------------------------------------
    # Unique Values
    # -------------------------------------------------

    unique_values = {

        column:
        int(df[column].nunique())

        for column in df.columns

    }



    # -------------------------------------------------
    # Numeric Statistics
    # -------------------------------------------------

    numeric_statistics = {}


    numeric_columns = (
        df.select_dtypes(
            include=np.number
        )
        .columns
    )


    for column in numeric_columns:

        numeric_statistics[column] = {


            "min":
                float(
                    df[column]
                    .min()
                ),


            "max":
                float(
                    df[column]
                    .max()
                ),


            "mean":
                round(
                    float(
                        df[column]
                        .mean()
                    ),
                    2
                ),


            "median":
                round(
                    float(
                        df[column]
                        .median()
                    ),
                    2
                )

        }



    # -------------------------------------------------
    # Quality Score
    # -------------------------------------------------

    quality_score = 100



    if missing_percentage > 5:

        quality_score -= 10



    if duplicate_percentage > 2:

        quality_score -= 10



    quality_score = max(
        quality_score,
        0
    )



    # -------------------------------------------------
    # Final Report
    # -------------------------------------------------

    profile = {


        "dataset":

            dataset_name,


        "file":

            file_path,


        "rows":

            total_rows,


        "columns":

            total_columns,


        "missing_percentage":

            missing_percentage,


        "duplicate_percentage":

            duplicate_percentage,


        "quality_score":

            quality_score,


        "data_types":

            data_types,


        "missing_values":

            missing_values,


        "unique_values":

            unique_values,


        "numeric_statistics":

            numeric_statistics


    }



    return profile