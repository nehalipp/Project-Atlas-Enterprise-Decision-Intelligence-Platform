from pathlib import Path
from sqlalchemy import text

from etl.database import engine


SQL_PATH = (
    Path(__file__)
    .resolve()
    .parents[2]
    /
    "sql"
    /
    "staging"
)


FILES = [

    "customers_clean.sql",

    "products_clean.sql",

    "suppliers_clean.sql",

    "locations_clean.sql",

    "employees_clean.sql",

    "sales_transactions_clean.sql"

]


def run():

    print("="*60)
    print("PROJECT ATLAS STAGING TRANSFORMATION")
    print("="*60)


    with engine.begin() as connection:

        for file in FILES:

            print(f"\nExecuting {file}")

            sql_file = SQL_PATH / file
            if not sql_file.exists():
                raise FileNotFoundError(
                    f"Missing SQL file: {sql_file}"
                )
            sql = sql_file.read_text()

            connection.execute(
                text(sql)
            )

            print("SUCCESS")


    print("\nSTAGING LOAD COMPLETED")


if __name__ == "__main__":
    run()