"""
==========================================================
Project Atlas

Dimension Loader

Loads:

    dim_date
    dim_customer
    dim_supplier
    dim_product
    dim_location
    dim_employee

==========================================================
"""


from pathlib import Path

from sqlalchemy import text

from etl.database import engine



# ---------------------------------------------------------
# SQL Location
# ---------------------------------------------------------

SQL_PATH = (
    Path(__file__)
    .resolve()
    .parents[2]
    /
    "sql"
    /
    "warehouse"
)



DIMENSION_FILES = [

    "dim_date.sql",

    "dim_customer.sql",

    "dim_supplier.sql",

    "dim_product.sql",

    "dim_location.sql",

    "dim_employee.sql"

]



# ---------------------------------------------------------
# Dimension Loader
# ---------------------------------------------------------

def load_dimensions():

    print("\n")
    print("-" * 60)
    print("LOADING DIMENSION TABLES")
    print("-" * 60)



    with engine.begin() as connection:


        for file in DIMENSION_FILES:


            print(
                f"\nExecuting {file}"
            )


            sql_file = SQL_PATH / file


            if not sql_file.exists():

                raise FileNotFoundError(
                    f"Missing SQL file: {sql_file}"
                )



            sql = sql_file.read_text(
                encoding="utf-8"
            )


            connection.execute(
                text(sql)
            )


            print(
                f"SUCCESS: {file}"
            )



    print("\nDIMENSION LOAD COMPLETED")
