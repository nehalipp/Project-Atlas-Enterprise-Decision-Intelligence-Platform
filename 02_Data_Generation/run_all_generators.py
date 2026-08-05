"""
Project Atlas: Enterprise Decision Intelligence Platform

Enterprise Synthetic Data Generation Pipeline

Purpose:
Central orchestration script that executes all
dimension and fact data generators.

Usage:

python3 run_all_generators.py

"""


import subprocess
import os
import time



# =====================================================
# PATH CONFIGURATION
# =====================================================


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)



# =====================================================
# GENERATOR EXECUTION ORDER
# =====================================================

"""
Execution order matters.

Dimensions first:
    Customers
    Products
    Suppliers
    Locations
    Employees
    Machines


Facts afterwards:
    Sales
    Production
    Maintenance
    Finance
    Budget
    ESG

"""


GENERATORS = [

    # ==============================
    # DIMENSIONS
    # ==============================


    (
        "Customers",
        "dimensions/customers/generate_customers.py"
    ),


    (
        "Products",
        "dimensions/products/generate_products.py"
    ),


    (
        "Suppliers",
        "dimensions/suppliers/generate_suppliers.py"
    ),


    (
        "Locations",
        "dimensions/locations/generate_locations.py"
    ),


    (
        "Employees",
        "dimensions/employees/generate_employees.py"
    ),


    (
        "Machines",
        "dimensions/machines/generate_machines.py"
    ),

    (
    "Accounts",
    "dimensions/accounts/generate_accounts.py"
    ),


    # ==============================
    # FACTS
    # ==============================

    (
    "Inventory",
    "facts/inventory/generate_inventory.py"
    ),


    (
        "Sales Transactions",
        "facts/sales/generate_sales.py"
    ),


    (
        "Production",
        "facts/production/generate_production.py"
    ),


    (
        "Maintenance",
        "facts/maintenance/generate_maintenance.py"
    ),


    (
        "Financial Transactions",
        "facts/finance/generate_financial_transactions.py"
    ),


    (
        "Budgets",
        "facts/budgets/generate_budget.py"
    ),


    (
        "Energy Consumption",
        "facts/energy/generate_energy.py"
    ),


    (
        "Carbon Emissions",
        "facts/emissions/generate_emissions.py"
    ),


    (
        "Waste Management",
        "facts/waste/generate_waste.py"
    )

]



# =====================================================
# EXECUTION FUNCTION
# =====================================================


def run_generator(
    name,
    script
):


    print("\n" + "="*70)

    print(
        f"Starting: {name}"
    )

    print("="*70)



    script_path = os.path.join(

        BASE_DIR,

        script

    )


    if not os.path.exists(script_path):

        print(
            f"ERROR: Missing file {script_path}"
        )

        return False



    try:


        start=time.time()



        result=subprocess.run(

            [

                "python3",

                script_path

            ],


            capture_output=True,

            text=True

        )



        duration=time.time()-start



        if result.returncode !=0:


            print(

                f"FAILED: {name}"

            )


            print(

                result.stderr

            )


            return False



        else:


            print(

                result.stdout

            )


            print(

                f"Completed {name} in {duration:.2f} seconds"

            )


            return True



    except Exception as e:


        print(

            f"Exception while running {name}"

        )


        print(e)


        return False





# =====================================================
# MAIN PIPELINE
# =====================================================


def main():


    print("\n")

    print("="*70)

    print(

        "PROJECT ATLAS DATA GENERATION PIPELINE"

    )

    print("="*70)



    pipeline_start=time.time()



    results=[]



    for name,script in GENERATORS:


        success=run_generator(

            name,

            script

        )


        results.append(

            (

                name,

                success

            )

        )



    total_time=time.time()-pipeline_start



    print("\n")

    print("="*70)

    print("PIPELINE SUMMARY")

    print("="*70)



    for name,status in results:


        result="SUCCESS" if status else "FAILED"


        print(

            f"{name:<35} {result}"

        )



    print("\n")

    print(

        f"Total execution time: {total_time/60:.2f} minutes"

    )


    print("="*70)





if __name__=="__main__":

    main()