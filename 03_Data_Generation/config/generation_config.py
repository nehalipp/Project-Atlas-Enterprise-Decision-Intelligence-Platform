"""
Project Atlas: Enterprise Decision Intelligence Platform

Synthetic Data Generation Configuration

Purpose:
Centralized configuration parameters used by all
synthetic enterprise data generators.
"""


# ==============================
# Dataset Volume Configuration
# ==============================

# Master data entities

CUSTOMER_COUNT = 50000

PRODUCT_COUNT = 5000

SUPPLIER_COUNT = 1000

EMPLOYEE_COUNT = 10000

LOCATION_COUNT = 250

MACHINE_COUNT = 1500


# Transactional datasets

SALES_TRANSACTION_COUNT = 500000

INVENTORY_RECORD_COUNT = 250000

PRODUCTION_EVENT_COUNT = 300000

MAINTENANCE_EVENT_COUNT = 100000

ENERGY_RECORD_COUNT = 150000


# ==============================
# Date Configuration
# ==============================

START_DATE = "2021-01-01"

END_DATE = "2026-06-30"


# ==============================
# Data Quality Issue Rates
# ==============================

"""
These percentages intentionally introduce
real-world enterprise data problems.
"""


MISSING_VALUE_RATE = 0.05
# 5% missing values


DUPLICATE_RECORD_RATE = 0.02
# 2% duplicate records


INVALID_CATEGORY_RATE = 0.01
# 1% invalid categories


DATE_ERROR_RATE = 0.01
# 1% incorrect dates


OUTLIER_RATE = 0.005
# 0.5% abnormal values


# ==============================
# Business Domain Values
# ==============================


COUNTRIES = [
    "United States",
    "Canada",
    "Germany",
    "Sweden",
    "United Kingdom",
    "France",
    "India",
    "Japan"
]


REGIONS = [
    "North America",
    "Europe",
    "Asia Pacific",
    "Latin America"
]


CUSTOMER_SEGMENTS = [
    "Enterprise",
    "Mid Market",
    "Small Business",
    "Consumer"
]


INDUSTRIES = [
    "Manufacturing",
    "Healthcare",
    "Technology",
    "Retail",
    "Finance",
    "Energy",
    "Logistics"
]


PRODUCT_CATEGORIES = [
    "Industrial Equipment",
    "Software",
    "Electronics",
    "Healthcare Equipment",
    "Consumer Products",
    "Automotive Parts"
]


DEPARTMENTS = [
    "Engineering",
    "Sales",
    "Finance",
    "Human Resources",
    "Operations",
    "Supply Chain",
    "Information Technology",
    "Marketing"
]


JOB_TITLES = [
    "Data Analyst",
    "Software Engineer",
    "Mechanical Engineer",
    "Operations Manager",
    "Financial Analyst",
    "Product Manager",
    "Sales Representative"
]


# ==============================
# Output Configuration
# ==============================

OUTPUT_PATH = "../output/"