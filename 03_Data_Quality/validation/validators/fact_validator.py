"""
Fact Dataset Validation
"""


import pandas as pd

from .business_rules import (

    validate_sales,

    validate_inventory,

    validate_production,

    validate_esg

)



def validate_fact(
        dataset_name,
        file_path
):


    df=pd.read_csv(
        file_path
    )


    results={

        "dataset":
            dataset_name,

        "issues":[]

    }



    if dataset_name=="sales":

        results["issues"].extend(
            validate_sales(df)
        )



    elif dataset_name=="inventory":

        results["issues"].extend(
            validate_inventory(df)
        )



    elif dataset_name=="production":

        results["issues"].extend(
            validate_production(df)
        )



    elif dataset_name in [

        "energy",

        "emissions",

        "waste"

    ]:

        results["issues"].extend(
            validate_esg(df)
        )


    return results