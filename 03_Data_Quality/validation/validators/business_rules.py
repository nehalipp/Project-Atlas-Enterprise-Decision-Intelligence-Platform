"""
Project Atlas: Enterprise Decision Intelligence Platform

Business Validation Rules

Contains domain specific checks.
"""


# =====================================================
# Sales Rules
# =====================================================

def validate_sales(df):

    issues = []


    # Quantity validation

    if "quantity" in df.columns:

        invalid = (
            df["quantity"] <= 0
        ).sum()

        if invalid > 0:

            issues.append(
                f"Invalid quantity records: {invalid}"
            )



    # Revenue validation

    if all(
        col in df.columns
        for col in [
            "quantity",
            "unit_price",
            "revenue"
        ]
    ):

        mismatch = (

            abs(
                df["quantity"]
                *
                df["unit_price"]
                -
                df["revenue"]
            )

            > 0.01

        ).sum()


        if mismatch > 0:

            issues.append(
                f"Revenue calculation mismatch: {mismatch}"
            )


    return issues



# =====================================================
# Inventory Rules
# =====================================================


def validate_inventory(df):

    issues=[]


    if "inventory_quantity" in df.columns:

        invalid = (

            df["inventory_quantity"] < 0

        ).sum()


        if invalid > 0:

            issues.append(
                f"Negative inventory records: {invalid}"
            )


    return issues



# =====================================================
# Manufacturing Rules
# =====================================================


def validate_production(df):

    issues=[]


    if "quantity_produced" in df.columns:


        invalid = (

            df["quantity_produced"] < 0

        ).sum()


        if invalid > 0:

            issues.append(
                f"Negative production records: {invalid}"
            )


    return issues



# =====================================================
# ESG Rules
# =====================================================


def validate_esg(df):

    issues=[]


    numeric_columns = [

        "energy_consumption",

        "carbon_emission",

        "waste_quantity"

    ]


    for column in numeric_columns:


        if column in df.columns:


            invalid=(

                df[column] < 0

            ).sum()


            if invalid > 0:

                issues.append(
                    f"{column} contains negative values: {invalid}"
                )


    return issues