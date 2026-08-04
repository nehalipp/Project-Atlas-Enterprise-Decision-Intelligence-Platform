"""
==========================================================
Project Atlas
Database Migration Runner

Features
--------
- Executes migrations in order
- Bootstraps metadata schema automatically
- Tracks completed migrations
- Prevents duplicate execution
==========================================================
"""

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DATABASE')}"
)

engine = create_engine(DATABASE_URL, future=True)

migration_folder = Path(__file__).parent / "migrations"

migration_files = sorted(migration_folder.glob("*.sql"))

print("=" * 60)
print("PROJECT ATLAS MIGRATION RUNNER")
print("=" * 60)

BOOTSTRAP = {
    "001_create_extensions.sql",
    "002_create_schemas.sql",
    "003_create_metadata_schema.sql",
}

with engine.begin() as connection:

    # -------------------------------------------------------
    # Bootstrap migrations
    # -------------------------------------------------------

    for migration in migration_files:

        if migration.name not in BOOTSTRAP:
            continue

        print(f"\nExecuting {migration.name}")

        sql = migration.read_text(encoding="utf-8")

        start = time.time()

        connection.execute(text(sql))

        duration = round(time.time() - start, 2)

        print(f"SUCCESS ({duration}s)")

    # -------------------------------------------------------
    # Read migration history
    # -------------------------------------------------------

    executed = connection.execute(
        text(
            """
            SELECT migration_name
            FROM metadata.migration_history
            WHERE execution_status='SUCCESS'
            """
        )
    )

    completed = {row[0] for row in executed.fetchall()}

    # -------------------------------------------------------
    # Remaining migrations
    # -------------------------------------------------------

    for migration in migration_files:

        if migration.name in BOOTSTRAP:
            continue

        if migration.name in completed:

            print(f"SKIPPING {migration.name}")

            continue

        print(f"\nExecuting {migration.name}")

        sql = migration.read_text(encoding="utf-8")

        start = time.time()

        connection.execute(text(sql))

        duration = round(time.time() - start, 2)

        connection.execute(
            text(
                """
                INSERT INTO metadata.migration_history
                (
                    migration_name,
                    execution_status,
                    execution_duration_seconds
                )
                VALUES
                (
                    :name,
                    'SUCCESS',
                    :duration
                )
                """
            ),
            {
                "name": migration.name,
                "duration": duration,
            },
        )

        print(f"SUCCESS ({duration}s)")

print("\nMigration process completed.")