"""
Dimension Dataset Validation
"""


import pandas as pd



def validate_dimension(
        dataset_name,
        file_path
):


    results = {

        "dataset":
            dataset_name,

        "checks": [],

        "issues":[]

    }



    df=pd.read_csv(
        file_path
    )


    # -------------------------
    # Missing primary keys
    # -------------------------


    primary_keys={

        "customers":"customer_id",

        "products":"product_id",

        "suppliers":"supplier_id",

        "employees":"employee_id",

        "locations":"location_id",

        "machines":"machine_id",

        "accounts":"account_id"

    }



    if dataset_name in primary_keys:


        key=primary_keys[dataset_name]


        if key in df.columns:


            missing=(

                df[key]
                .isna()
                .sum()

            )


            results["checks"].append(
                f"{key} completeness"
            )


            if missing > 0:

                results["issues"].append(
                    f"Missing {key}: {missing}"
                )



            duplicates=(

                df[key]
                .duplicated()
                .sum()

            )


            if duplicates > 0:

                results["issues"].append(
                    f"Duplicate {key}: {duplicates}"
                )


    return results