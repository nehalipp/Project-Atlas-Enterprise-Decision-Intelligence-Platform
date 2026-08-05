"""
Project Atlas: Enterprise Decision Intelligence Platform

Data Quality Report Generator

Combines:

1. Profiling Results
2. Validation Results

Creates:

- quality_summary.csv
- data_quality_report.md
"""


import os
import json
import pandas as pd



# --------------------------------------------------
# Paths
# --------------------------------------------------


CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


QUALITY_ROOT = os.path.abspath(
    os.path.join(
        CURRENT_DIR,
        ".."
    )
)



PROFILE_PATH = os.path.join(

    QUALITY_ROOT,

    "profiling",

    "output",

    "profiles"

)



VALIDATION_FILE = os.path.join(

    QUALITY_ROOT,

    "validation",

    "output",

    "validation_results.json"

)



OUTPUT_PATH = os.path.join(

    CURRENT_DIR,

    "output"

)



os.makedirs(

    OUTPUT_PATH,

    exist_ok=True

)



# --------------------------------------------------
# Load Profiles
# --------------------------------------------------


def load_profiles():

    profiles=[]


    for file in os.listdir(PROFILE_PATH):

        if file.endswith(".json"):


            with open(
                os.path.join(
                    PROFILE_PATH,
                    file
                )
            ) as f:


                profiles.append(
                    json.load(f)
                )


    return profiles



# --------------------------------------------------
# Load Validation Results
# --------------------------------------------------


def load_validation():


    if not os.path.exists(
        VALIDATION_FILE
    ):

        return []


    with open(
        VALIDATION_FILE
    ) as f:


        return json.load(f)



# --------------------------------------------------
# Create Summary
# --------------------------------------------------


def generate_summary():


    profiles = load_profiles()

    validations = load_validation()



    validation_lookup = {


        item["dataset"]:
            item

        for item in validations

    }



    summary=[]



    for profile in profiles:


        dataset = profile["dataset"]


        validation = (

            validation_lookup
            .get(
                dataset,
                {}
            )

        )


        issues = validation.get(
            "issues",
            []
        )



        status = (

            "PASS"

            if len(issues)==0

            else

            "WARNING"

        )



        summary.append(

            {

            "Dataset":
                dataset,


            "Rows":
                profile["rows"],


            "Columns":
                profile["columns"],


            "Missing %":
                profile["missing_percentage"],


            "Duplicate %":
                profile["duplicate_percentage"],


            "Quality Score":
                profile["quality_score"],


            "Validation Status":
                status,


            "Issues":
                len(issues)

            }

        )


    return pd.DataFrame(summary)



# --------------------------------------------------
# Save CSV
# --------------------------------------------------


def save_csv(df):


    output=os.path.join(

        OUTPUT_PATH,

        "quality_summary.csv"

    )


    df.to_csv(

        output,

        index=False

    )


    print(
        f"Created: {output}"
    )



# --------------------------------------------------
# Save Markdown Report
# --------------------------------------------------


def save_markdown(df):


    output=os.path.join(

        OUTPUT_PATH,

        "data_quality_report.md"

    )



    with open(
        output,
        "w"
    ) as f:


        f.write(

            "# Project Atlas - Data Quality Report\n\n"

        )


        f.write(

            "## Dataset Health Summary\n\n"

        )


        f.write(

            df.to_markdown(
                index=False
            )

        )


        f.write(

            "\n\n## Overall Statistics\n\n"

        )


        f.write(

            f"- Total datasets analyzed: {len(df)}\n"

        )


        f.write(

            f"- Average quality score: {round(df['Quality Score'].mean(),2)}%\n"

        )


        f.write(

            f"- Datasets requiring attention: {(df['Validation Status']=='WARNING').sum()}\n"

        )



    print(
        f"Created: {output}"
    )



# --------------------------------------------------
# Main
# --------------------------------------------------


if __name__=="__main__":


    print(
        "Generating Data Quality Report..."
    )


    df = generate_summary()


    save_csv(df)


    save_markdown(df)


    print(
        "Report generation completed"
    )