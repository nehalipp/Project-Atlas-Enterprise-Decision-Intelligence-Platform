"""
Project Atlas
SQL Analytics Result Exporter

Reads SQL queries and exports results into named CSV files.

SQL file format:

-- OUTPUT: filename.csv

SELECT ...
"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import re


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

DATABASE_URL = (
    "postgresql+psycopg2://postgres:postgres"
    "@localhost:5432/project_atlas_dw"
)


engine = create_engine(DATABASE_URL)


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).parent

RESULTS_DIR = BASE_DIR / "Query_Results"

RESULTS_DIR.mkdir(
    exist_ok=True
)


SQL_FILES = sorted(
    BASE_DIR.glob("*.sql")
)


# ==========================================================
# EXTRACT OUTPUT FILE NAME
# ==========================================================

def extract_output_name(statement):

    """
    Finds:
    
    -- OUTPUT: filename.csv
    
    """

    match = re.search(
        r"--\s*OUTPUT:\s*(.+\.csv)",
        statement,
        re.IGNORECASE
    )


    if match:

        return match.group(1).strip()


    return None



# ==========================================================
# CLEAN SQL
# ==========================================================

def clean_query(statement):

    """
    Removes comments before executing SQL.
    """

    lines = []

    for line in statement.split("\n"):

        if line.strip().startswith("--"):

            continue

        lines.append(line)


    return "\n".join(lines).strip()



# ==========================================================
# SPLIT SQL QUERIES
# ==========================================================

def extract_queries(sql):

    queries = []


    statements = sql.split(";")

    for statement in statements:

        if "select" in statement.lower():

            queries.append(
                statement.strip()
            )


    return queries



# ==========================================================
# EXPORT
# ==========================================================

def export_results():


    print("\nProject Atlas SQL Export Started\n")


    file_count = 0



    for sql_file in SQL_FILES:


        print(
            f"Processing {sql_file.name}"
        )


        with open(
            sql_file,
            "r",
            encoding="utf-8"
        ) as file:

            sql_content = file.read()



        statements = sql_content.split(";")



        for statement in statements:


            if "select" not in statement.lower():

                continue



            output_name = extract_output_name(
                statement
            )


            if not output_name:

                print(
                    "Skipping query: No OUTPUT filename"
                )

                continue



            query = clean_query(
                statement
            )



            try:

                df = pd.read_sql(
                    query,
                    engine
                )


                output_path = (
                    RESULTS_DIR
                    /
                    output_name
                )


                df.to_csv(
                    output_path,
                    index=False
                )


                print(
                    f"✓ Created {output_name}"
                )


                file_count += 1



            except Exception as e:

                print(
                    f"✗ Failed {output_name}"
                )

                print(e)



    print(
        f"\nCompleted. {file_count} files created."
    )



if __name__ == "__main__":

    export_results()