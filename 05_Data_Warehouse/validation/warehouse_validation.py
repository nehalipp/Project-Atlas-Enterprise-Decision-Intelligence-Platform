"""
==========================================================
Project Atlas

Warehouse Data Quality Validation Framework

Validations:
    - Row Counts
    - Duplicate Records
    - Null Checks
    - Referential Integrity
    - Business Reconciliation

==========================================================
"""


from pathlib import Path

from sqlalchemy import text

from etl.database import engine



# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

SQL_FOLDER = (
    Path(__file__)
    .resolve()
    .parent
    /
    "sql"
)



VALIDATION_FILES = [

    "row_count_validation.sql",

    "duplicate_checks.sql",

    "null_checks.sql",

    "referential_integrity.sql",

    "business_validation.sql"

]



# ---------------------------------------------------------
# Execute Validation SQL
# ---------------------------------------------------------

def execute_validation(file_name):


    print("\n" + "-" * 60)

    print(f"Running {file_name}")

    print("-" * 60)



    sql_file = SQL_FOLDER / file_name


    sql = sql_file.read_text(
        encoding="utf-8"
    )


    with engine.begin() as connection:


        result = connection.execute(
            text(sql)
        )


        rows = result.fetchall()



    if rows:


        print("\nRESULTS:")


        for row in rows:

            print(row)



    else:

        print(
            "PASS - No issues found"
        )



# ---------------------------------------------------------
# Runner
# ---------------------------------------------------------

def run():


    print("=" * 60)

    print(
        "PROJECT ATLAS DATA QUALITY VALIDATION"
    )

    print("=" * 60)



    for validation_file in VALIDATION_FILES:

        execute_validation(
            validation_file
        )



    print("\n")

    print("=" * 60)

    print(
        "VALIDATION COMPLETED"
    )

    print("=" * 60)



if __name__ == "__main__":

    run()