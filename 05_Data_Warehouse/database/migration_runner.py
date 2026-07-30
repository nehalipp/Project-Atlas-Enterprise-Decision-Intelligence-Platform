"""
Project Atlas
Database Migration Runner
"""

from pathlib import Path
from sqlalchemy import create_engine, text

# ---------------------------------------------------
# Update these values for your environment
# ---------------------------------------------------

DATABASE_URL = (
    "postgresql+psycopg2://"
    "postgres:YOUR_PASSWORD@localhost:5432/project_atlas_dw"
)

# ---------------------------------------------------

engine = create_engine(DATABASE_URL, future=True)

migrations_path = Path(__file__).parent / "migrations"

migration_files = sorted(
    migrations_path.glob("*.sql")
)

print("=" * 60)
print("PROJECT ATLAS DATABASE MIGRATIONS")
print("=" * 60)

with engine.begin() as connection:

    for migration in migration_files:

        print(f"Running {migration.name}")

        sql = migration.read_text(encoding="utf-8")

        connection.execute(text(sql))

        print("✓ Completed")

print("\nAll migrations completed successfully.")