from pathlib import Path

import pandas as pd


def save_csv(df, filename):

    output_folder = Path(__file__).parent.parent

    output_file = output_folder / filename

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(f"Saved {output_file}")

    print(f"Rows: {len(df):,}")