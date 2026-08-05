"""
Project Atlas: Enterprise Decision Intelligence Platform

Run Complete Data Profiling Pipeline

Profiles every dataset registered
in quality_config.py
"""


import os
import json
import sys


# Add 03_Data_Quality root to Python path

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

from profiling.profiler import profile_dataset


# -----------------------------------------------------
# Run Profiling
# -----------------------------------------------------

def run_profiling():


    print("="*70)

    print(
        "PROJECT ATLAS DATA QUALITY PROFILING PIPELINE"
    )

    print("="*70)



    results = []



    for dataset_name, file_path in config.DATASETS.items():


        try:


            profile = profile_dataset(
                dataset_name,
                file_path
            )


            results.append(profile)



            output_file = os.path.join(

                config.PROFILE_OUTPUT_PATH,

                f"{dataset_name}_profile.json"

            )



            os.makedirs(

                config.PROFILE_OUTPUT_PATH,

                exist_ok=True

            )



            with open(
                output_file,
                "w"
            ) as f:


                json.dump(
                    profile,
                    f,
                    indent=4
                )



            print(
                f"SUCCESS: {dataset_name}"
            )



        except Exception as e:


            print(
                f"FAILED: {dataset_name}"
            )


            print(e)




    return results




# -----------------------------------------------------
# Main
# -----------------------------------------------------

if __name__ == "__main__":


    run_profiling()