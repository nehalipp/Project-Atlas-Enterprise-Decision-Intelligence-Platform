import numpy as np


def add_missing_values(df, column, rate):

    rows = int(len(df) * rate)

    idx = np.random.choice(
        df.index,
        rows,
        replace=False
    )

    df.loc[idx, column] = None

    return df


def add_duplicates(df, rate):

    rows = int(len(df) * rate)

    duplicates = df.sample(
        rows,
        random_state=42
    )

    return df._append(
        duplicates,
        ignore_index=True
    )