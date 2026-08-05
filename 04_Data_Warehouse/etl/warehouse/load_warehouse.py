"""
==========================================================
Project Atlas

Warehouse Load Orchestrator

Purpose:
    Execute dimension and fact loading pipeline.

==========================================================
"""


from etl.warehouse.load_dimensions import load_dimensions
from etl.warehouse.load_fact_sales import load_fact_sales



def run():

    print("=" * 60)
    print("PROJECT ATLAS WAREHOUSE LOAD")
    print("=" * 60)


    print("\nStarting Dimension Loads")

    load_dimensions()


    print("\nStarting Fact Load")

    load_fact_sales()


    print("\n")
    print("=" * 60)
    print("WAREHOUSE LOAD COMPLETED SUCCESSFULLY")
    print("=" * 60)



if __name__ == "__main__":

    run()