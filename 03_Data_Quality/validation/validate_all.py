"""
Project Atlas

Master Data Validation Runner
"""


import os
import sys
import json


CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


QUALITY_ROOT = os.path.abspath(
    os.path.join(
        CURRENT_DIR,
        ".."
    )
)


sys.path.append(
    QUALITY_ROOT
)


from config import quality_config as config


from validation.validators.dimension_validator import (
    validate_dimension
)


from validation.validators.fact_validator import (
    validate_fact
)


DIMENSIONS=[

"accounts",

"customers",

"employees",

"locations",

"machines",

"products",

"suppliers"

]



FACTS=[

"sales",

"inventory",

"production",

"maintenance",

"finance",

"budget",

"energy",

"emissions",

"waste"

]



results=[]



def run_validation():


    print(
        "STARTING VALIDATION"
    )


    for dataset,path in config.DATASETS.items():


        if dataset in DIMENSIONS:


            result=validate_dimension(
                dataset,
                path
            )


        else:


            result=validate_fact(
                dataset,
                path
            )


        results.append(result)


        print(
            dataset,
            "completed"
        )



    output=os.path.join(

        "validation",

        "output",

        "validation_results.json"

    )


    os.makedirs(

        os.path.dirname(output),

        exist_ok=True

    )


    with open(
        output,
        "w"
    ) as f:


        json.dump(

            results,

            f,

            indent=4

        )



if __name__=="__main__":

    run_validation()