"""
Project Atlas
End-to-End ETL Pipeline Runner
"""

import subprocess
import sys
import time


PIPELINE_STEPS = [

    (
        "Raw Data Ingestion",
        "etl.raw.load_raw_data"
    ),

    (
        "Staging Transformation",
        "etl.staging.transform_staging"
    ),

    (
        "Warehouse Load",
        "etl.warehouse.load_warehouse"
    ),

    (
        "Warehouse Validation",
        "validation.warehouse_validation"
    )

]


def run_step(name, module):

    print("\n")
    print("=" * 70)
    print(f"RUNNING: {name}")
    print("=" * 70)


    start=time.time()


    result=subprocess.run(
        [
            sys.executable,
            "-m",
            module
        ]
    )


    duration=round(
        time.time()-start,
        2
    )


    if result.returncode !=0:

        raise Exception(
            f"{name} FAILED"
        )


    print(
        f"{name} COMPLETED ({duration}s)"
    )



def main():

    print("""
============================================================
PROJECT ATLAS ENTERPRISE DATA PIPELINE
============================================================
""")


    for name,module in PIPELINE_STEPS:

        run_step(
            name,
            module
        )


    print("""
============================================================
PIPELINE COMPLETED SUCCESSFULLY
============================================================
""")


if __name__=="__main__":

    main()