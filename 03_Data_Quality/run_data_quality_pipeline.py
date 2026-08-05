"""
Project Atlas

Enterprise Data Quality Pipeline

Purpose:
Execute complete data quality workflow:
1. Dataset profiling
2. Validation checks
3. Report generation
"""


import os
import sys
import subprocess
from datetime import datetime



def print_header():

    print("\n")
    print("=" * 45)
    print("PROJECT ATLAS DATA QUALITY PIPELINE")
    print("=" * 45)
    print("\n")



def run_profiling():

    print("Step 1: Running dataset profiling...")
    print("-----------------------------------")


    profiling_path = "../profiling"


    subprocess.run(
        [
            sys.executable,
            os.path.join(
                profiling_path,
                "profile_all_datasets.py"
            )
        ]
    )


    print("\n✓ Profiling completed\n")



def generate_report():

    print("Step 2: Generating quality report...")
    print("-----------------------------------")


    report_path = "../reports"


    subprocess.run(
        [
            sys.executable,
            os.path.join(
                report_path,
                "generate_quality_report.py"
            )
        ]
    )


    print("\n✓ Report generation completed\n")



def pipeline_summary():

    print("=" * 45)

    print(
        "PROJECT ATLAS PIPELINE COMPLETED"
    )

    print("=" * 45)


    print(
        f"""
Execution Date:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


Generated Artifact:

04_Data_Quality/reports/data_quality_report.md


Next Step:

Review quality findings before
warehouse ingestion.
"""
    )



if __name__ == "__main__":


    print_header()


    run_profiling()


    generate_report()


    pipeline_summary()