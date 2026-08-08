"""
Project Atlas
Extract Pipeline Runner
"""

from etl.extract.extract_csv_to_raw import run_extract


if __name__ == "__main__":

    print(
        """
====================================
Project Atlas Extract Pipeline
CSV → RAW
====================================
"""
    )


    run_extract()


    print(
        """
====================================
Extract Completed Successfully
====================================
"""
    )