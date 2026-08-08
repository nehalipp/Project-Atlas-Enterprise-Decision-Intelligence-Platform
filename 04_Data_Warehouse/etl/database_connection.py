from sqlalchemy import create_engine


def get_engine():

    return create_engine(
        "postgresql://localhost:5432/project_atlas_dw"
    )