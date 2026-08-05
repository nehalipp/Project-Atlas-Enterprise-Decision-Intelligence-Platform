"""
==========================================================
Project Atlas
Raw Data Ingestion Pipeline

Purpose:
    Load generated CSV files into PostgreSQL raw schema.

Source:
    03_Data_Generation/output

Target:
    PostgreSQL raw schema

Tables:
    raw.customers
    raw.products
    raw.suppliers
    raw.locations
    raw.employees
    raw.sales_transactions

==========================================================
"""


from pathlib import Path

import pandas as pd

from sqlalchemy import text

from etl.database import engine

from etl.config import (
    SOURCE_SYSTEM,
    RAW_SCHEMA,
    LOAD_CHUNK_SIZE
)



# ---------------------------------------------------------
# Project Paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_FOLDER = (
    PROJECT_ROOT
    / "03_Data_Generation"
    / "output"
)



# ---------------------------------------------------------
# Source File → Raw Table Mapping
# ---------------------------------------------------------

DATASETS = {

    "raw_customers.csv":
        "customers",

    "raw_products.csv":
        "products",

    "raw_suppliers.csv":
        "suppliers",

    "raw_locations.csv":
        "locations",

    "raw_employees.csv":
        "employees",

    "raw_sales_transactions.csv":
        "sales_transactions"

}



# ---------------------------------------------------------
# Load Single Dataset
# ---------------------------------------------------------

def load_dataset(file_name, table_name):


    file_path = DATA_FOLDER / file_name


    print("\n" + "-" * 60)

    print(f"Loading File: {file_name}")

    print("-" * 60)



    if not file_path.exists():

        raise FileNotFoundError(
            f"Missing file: {file_path}"
        )



    # -----------------------------------------------------
    # Read CSV
    # -----------------------------------------------------

    df = pd.read_csv(file_path)



    # -----------------------------------------------------
    # Add ETL Metadata
    # -----------------------------------------------------

    df["source_system"] = SOURCE_SYSTEM

    df["ingestion_timestamp"] = pd.Timestamp.now()



    print(
        f"Records Found: {len(df)}"
    )


    print(
        f"Columns: {len(df.columns)}"
    )



    # -----------------------------------------------------
    # Clear Existing Raw Data
    # -----------------------------------------------------

    with engine.begin() as connection:

        connection.execute(
            text(
                f"TRUNCATE TABLE {RAW_SCHEMA}.{table_name}"
            )
        )



    # -----------------------------------------------------
    # Load Into PostgreSQL Raw Schema
    # -----------------------------------------------------

    df.to_sql(

        name=table_name,

        con=engine,

        schema=RAW_SCHEMA,

        if_exists="append",

        index=False,

        chunksize=LOAD_CHUNK_SIZE

    )


    print(
        f"Loaded Successfully: {RAW_SCHEMA}.{table_name}"
    )




# ---------------------------------------------------------
# Pipeline Runner
# ---------------------------------------------------------

def run_raw_ingestion():


    print("=" * 60)

    print(
        "PROJECT ATLAS RAW DATA INGESTION PIPELINE"
    )

    print("=" * 60)



    for file_name, table_name in DATASETS.items():


        load_dataset(

            file_name,

            table_name

        )



    print("\n")

    print("=" * 60)

    print(
        "RAW INGESTION COMPLETED SUCCESSFULLY"
    )

    print("=" * 60)




# ---------------------------------------------------------
# Execute Pipeline
# ---------------------------------------------------------

if __name__ == "__main__":

    run_raw_ingestion()