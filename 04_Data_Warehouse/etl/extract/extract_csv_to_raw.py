"""
==========================================================
Project Atlas

Extract CSV files into PostgreSQL raw schema.

Flow:

CSV Files
    |
    ↓
raw.*

Strategy:
    Full refresh load

Before every load:
    TRUNCATE raw table

==========================================================
"""

import os
import pandas as pd

from sqlalchemy import text

from etl.database_connection import get_engine
from etl.extract.config.source_config import CSV_SOURCES


BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../02_Data_Generation"
    )
)


def load_csv_to_raw(source_name, source_config):

    engine = get_engine()

    csv_path = os.path.join(
        BASE_PATH,
        source_config["file"]
    )

    schema = source_config["schema"]
    table = source_config["table"]


    print(f"\nLoading: {source_name}")


    if not os.path.exists(csv_path):

        raise FileNotFoundError(
            f"CSV not found: {csv_path}"
        )


    df = pd.read_csv(csv_path)


    print(
        f"Rows extracted: {len(df)}"
    )


    with engine.begin() as connection:

        # Full refresh RAW layer
        connection.execute(
            text(
                f"""
                TRUNCATE TABLE
                {schema}.{table};
                """
            )
        )


        df.to_sql(
            table,
            connection,
            schema=schema,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=5000
        )


    print(
        f"Loaded {schema}.{table}"
    )



def run_extract():

    print("="*60)
    print("Starting CSV → RAW Extraction")
    print("="*60)


    for name, config in CSV_SOURCES.items():

        load_csv_to_raw(
            name,
            config
        )


    print("="*60)
    print("Extraction Completed")
    print("="*60)



if __name__ == "__main__":

    run_extract()