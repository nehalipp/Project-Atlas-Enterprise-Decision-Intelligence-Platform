"""
==========================================================
Project Atlas

Enterprise Decision Intelligence Platform

Master ETL Pipeline Orchestrator

Pipeline Flow:

CSV Files
    |
    v
Extract
    |
    v
RAW Schema
    |
    v
Transform
    |
    v
STAGING Schema
    |
    v
Warehouse Load
    |
    v
Validation

==========================================================
"""


import subprocess
import time
from datetime import datetime



# ==========================================================
# PIPELINE CONFIGURATION
# ==========================================================


DATABASE_NAME = "project_atlas_dw"

VALIDATION_SCRIPT = (
    "sql/validation/pipeline_validation.sql"
)



# ==========================================================
# RUN COMMAND
# ==========================================================


def run_step(step_name, command):

    print("\n")
    print("=" * 70)
    print(f"RUNNING: {step_name}")
    print("=" * 70)


    start_time = time.time()


    result = subprocess.run(
        command,
        shell=True
    )


    duration = (
        time.time() - start_time
    )


    if result.returncode != 0:

        raise Exception(
            f"{step_name} FAILED"
        )


    print(
        f"""
Completed: {step_name}
Duration : {duration:.2f} seconds
"""
    )



# ==========================================================
# PIPELINE STEPS
# ==========================================================


def run_extract():

    run_step(
        "Raw Data Extraction",
        "python3 -m etl.extract.run_extract"
    )



def run_transform():

    run_step(
        "Raw To Staging Transformation",
        "python3 -m etl.transform.run_transform"
    )



def run_warehouse_load():

    run_step(
        "Staging To Warehouse Load",
        "python3 -m etl.load.staging_to_warehouse"
    )



def run_validation():

    run_step(
        "Pipeline Data Quality Validation",
        (
            f"psql -d {DATABASE_NAME} "
            f"-f {VALIDATION_SCRIPT}"
        )
    )



# ==========================================================
# MAIN PIPELINE
# ==========================================================


def main():


    pipeline_start = datetime.now()


    print(
        """
============================================================
PROJECT ATLAS ENTERPRISE DATA PIPELINE
============================================================
"""
    )


    try:


        # ------------------------------------------
        # STEP 1
        # ------------------------------------------

        run_extract()



        # ------------------------------------------
        # STEP 2
        # ------------------------------------------

        run_transform()



        # ------------------------------------------
        # STEP 3
        # ------------------------------------------

        run_warehouse_load()



        # ------------------------------------------
        # STEP 4
        # ------------------------------------------

        run_validation()



        pipeline_end = datetime.now()


        duration = (
            pipeline_end - pipeline_start
        )


        print(
            """
============================================================
PROJECT ATLAS PIPELINE COMPLETED
============================================================

Status   : SUCCESS
Started  : {}
Finished : {}
Duration : {}

============================================================
""".format(
                pipeline_start,
                pipeline_end,
                duration
            )
        )



    except Exception as e:


        print(
            """
============================================================
PROJECT ATLAS PIPELINE FAILED
============================================================
"""
        )


        print(
            f"Error: {e}"
        )


        raise



# ==========================================================
# ENTRY POINT
# ==========================================================


if __name__ == "__main__":

    main()