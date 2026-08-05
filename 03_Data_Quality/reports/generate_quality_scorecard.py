"""
Project Atlas: Enterprise Decision Intelligence Platform

Data Quality Excel Scorecard Generator

Creates:
data_quality_scorecard.xlsx

Purpose:
Business-friendly data quality dashboard.
"""


import os
import pandas as pd



# --------------------------------------------------
# Paths
# --------------------------------------------------

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


INPUT_FILE = os.path.join(

    CURRENT_DIR,

    "output",

    "quality_summary.csv"

)


OUTPUT_FILE = os.path.join(

    CURRENT_DIR,

    "output",

    "data_quality_scorecard.xlsx"

)



# --------------------------------------------------
# Generate Excel Scorecard
# --------------------------------------------------


def generate_scorecard():


    df = pd.read_csv(
        INPUT_FILE
    )


    # Sort worst quality datasets first

    df = df.sort_values(
        by="Quality Score",
        ascending=True
    )


    with pd.ExcelWriter(
        OUTPUT_FILE,
        engine="openpyxl"
    ) as writer:


        df.to_excel(

            writer,

            sheet_name="Quality Scorecard",

            index=False

        )


        # Summary Sheet

        summary = pd.DataFrame(

            {

            "Metric":[

                "Total Datasets",

                "Average Quality Score",

                "Datasets with Warning",

                "Datasets Passed"

            ],


            "Value":[

                len(df),

                round(
                    df["Quality Score"]
                    .mean(),
                    2
                ),


                (

                    df["Validation Status"]
                    =="WARNING"

                ).sum(),


                (

                    df["Validation Status"]
                    =="PASS"

                ).sum()

            ]

            }

        )


        summary.to_excel(

            writer,

            sheet_name="Summary",

            index=False

        )



    print(
        f"Created: {OUTPUT_FILE}"
    )



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__=="__main__":


    print(
        "Generating Quality Scorecard..."
    )


    generate_scorecard()


    print(
        "Scorecard generation completed"
    )