"""
Project Atlas: Enterprise Decision Intelligence Platform

Data Quality Master Pipeline Runner

Execution:

python3 run_quality_pipeline.py

Pipeline:

1. Dataset Profiling
2. Data Validation
3. Quality Reporting
"""


import os
import sys
import subprocess



CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)



def run_step(
        step_name,
        command
):

    print("\n" + "="*70)

    print(
        f"STARTING: {step_name}"
    )

    print("="*70)



    try:

        subprocess.run(
            command,
            check=True
        )


        print(
            f"\nCOMPLETED: {step_name}"
        )


    except subprocess.CalledProcessError as e:


        print(
            f"\nFAILED: {step_name}"
        )


        print(e)





# ==================================================
# MAIN PIPELINE
# ==================================================


if __name__ == "__main__":


    print(
        "\nPROJECT ATLAS DATA QUALITY PIPELINE"
    )



    # ------------------------------
    # Profiling
    # ------------------------------


    profiling_script = os.path.join(

        CURRENT_DIR,

        "profiling",

        "profile_all_datasets.py"

    )


    run_step(

        "DATASET PROFILING",

        [
            "python3",
            profiling_script
        ]

    )



    # ------------------------------
    # Validation
    # ------------------------------


    validation_script = os.path.join(

        CURRENT_DIR,

        "validation",

        "validate_all.py"

    )


    if os.path.exists(validation_script):


        run_step(

            "DATA VALIDATION",

            [
                "python3",
                validation_script
            ]

        )


    else:

        print(
            "\nValidation framework not created yet. Skipping..."
        )



    print("\n")

    print("="*70)

    print(
        "DATA QUALITY PIPELINE COMPLETED"
    )

    print("="*70)

# ------------------------------
# Excel Scorecard
# ------------------------------

scorecard_script = os.path.join(

    CURRENT_DIR,

    "reports",

    "generate_quality_scorecard.py"

)


run_step(

    "QUALITY SCORECARD GENERATION",

    [

        "python3",

        scorecard_script

    ]

)