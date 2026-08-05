"""
==========================================================
Project Atlas

Fact Sales Loader

Loads:

    fact_sales

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



FACT_FILE = "fact_sales.sql"



# ---------------------------------------------------------
# Fact Loader
# ---------------------------------------------------------

def load_fact_sales():

    print("\n")
    print("-" * 60)
    print("LOADING FACT SALES")
    print("-" * 60)



    sql_file = SQL_PATH / FACT_FILE



    if not sql_file.exists():

        raise FileNotFoundError(
            f"Missing SQL file: {sql_file}"
        )



    sql = sql_file.read_text(
        encoding="utf-8"
    )



    with engine.begin() as connection:


        connection.execute(
            text(sql)
        )



    print(
        "SUCCESS: fact_sales loaded"
    )
