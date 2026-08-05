"""
Project Atlas: Enterprise Decision Intelligence Platform

Synthetic Enterprise Data Generation Configuration

Central configuration used by all synthetic data generators.

Domains:
- Core Business
- Master Data
- Workforce
- Manufacturing
- Finance
- ESG
"""


from datetime import date



# =====================================================
# REPRODUCIBILITY
# =====================================================

RANDOM_SEED = 42



# =====================================================
# DATASET VOLUMES
# =====================================================


# Dimensions

CUSTOMER_COUNT = 50000

PRODUCT_COUNT = 5000

SUPPLIER_COUNT = 1000

LOCATION_COUNT = 250

EMPLOYEE_COUNT = 10000

MACHINE_COUNT = 1500



# Facts

SALES_TRANSACTION_COUNT = 500000

PRODUCTION_EVENT_COUNT = 300000

MAINTENANCE_EVENT_COUNT = 100000

FINANCIAL_TRANSACTION_COUNT = 500000

ACCOUNT_COUNT = 500

BUDGET_COUNT = 5000

ENERGY_RECORD_COUNT = 150000

EMISSION_RECORD_COUNT = 150000

WASTE_RECORD_COUNT = 100000

INVENTORY_RECORD_COUNT = 250000



# =====================================================
# DATE CONFIGURATION
# =====================================================


START_DATE = date(
    2021,
    1,
    1
)


END_DATE = date(
    2026,
    6,
    30
)



# =====================================================
# DATA QUALITY
# =====================================================


MISSING_VALUE_RATE = 0.05

DUPLICATE_RECORD_RATE = 0.02

INVALID_CATEGORY_RATE = 0.01

DATE_ERROR_RATE = 0.01

OUTLIER_RATE = 0.005



# =====================================================
# GEOGRAPHY DOMAIN
# =====================================================


COUNTRIES = [

    "United States",
    "Canada",
    "Germany",
    "Sweden",
    "United Kingdom",
    "France",
    "India",
    "Japan",
    "Australia",
    "Netherlands"

]



REGIONS = [

    "North America",

    "Europe",

    "Asia Pacific"

]



COUNTRY_LOCATION_MAP = {


    "United States": {

        "region": "North America",

        "states": [
            "California",
            "Texas",
            "New York",
            "Illinois",
            "Washington",
            "Pennsylvania",
            "Michigan",
            "Ohio"
        ],

        "cities": [
            "San Francisco",
            "Austin",
            "New York City",
            "Chicago",
            "Seattle",
            "Philadelphia",
            "Detroit",
            "Columbus"
        ]

    },


    "Canada": {

        "region": "North America",

        "states": [
            "Ontario",
            "British Columbia",
            "Quebec",
            "Alberta"
        ],

        "cities": [
            "Toronto",
            "Vancouver",
            "Montreal",
            "Calgary"
        ]

    },


    "Germany": {

        "region": "Europe",

        "states": [
            "Bavaria",
            "Berlin",
            "Hesse",
            "North Rhine-Westphalia"
        ],

        "cities": [
            "Munich",
            "Berlin",
            "Frankfurt",
            "Cologne"
        ]

    },


    "Sweden": {

        "region": "Europe",

        "states": [
            "Stockholm County",
            "Vastra Gotaland",
            "Skane"
        ],

        "cities": [
            "Stockholm",
            "Gothenburg",
            "Malmo"
        ]

    },


    "United Kingdom": {

        "region": "Europe",

        "states": [
            "England",
            "Scotland",
            "Wales"
        ],

        "cities": [
            "London",
            "Manchester",
            "Edinburgh"
        ]

    },


    "France": {

        "region": "Europe",

        "states": [
            "Ile-de-France",
            "Occitanie",
            "Auvergne-Rhone-Alpes"
        ],

        "cities": [
            "Paris",
            "Toulouse",
            "Lyon"
        ]

    },


    "India": {

        "region": "Asia Pacific",

        "states": [
            "Maharashtra",
            "Karnataka",
            "Delhi",
            "Tamil Nadu"
        ],

        "cities": [
            "Mumbai",
            "Bangalore",
            "Delhi",
            "Chennai"
        ]

    },


    "Japan": {

        "region": "Asia Pacific",

        "states": [
            "Tokyo",
            "Osaka",
            "Kyoto"
        ],

        "cities": [
            "Tokyo",
            "Osaka",
            "Kyoto"
        ]

    },


    "Australia": {

        "region": "Asia Pacific",

        "states": [
            "New South Wales",
            "Victoria",
            "Queensland"
        ],

        "cities": [
            "Sydney",
            "Melbourne",
            "Brisbane"
        ]

    },


    "Netherlands": {

        "region": "Europe",

        "states": [
            "North Holland",
            "South Holland",
            "Utrecht"
        ],

        "cities": [
            "Amsterdam",
            "Rotterdam",
            "Utrecht"
        ]

    }

}

# =====================================================
# CITY COORDINATES
# =====================================================


CITY_COORDINATES = {


    # United States

    "San Francisco": {
        "latitude": 37.7749,
        "longitude": -122.4194
    },

    "Austin": {
        "latitude": 30.2672,
        "longitude": -97.7431
    },

    "New York City": {
        "latitude": 40.7128,
        "longitude": -74.0060
    },

    "Chicago": {
        "latitude": 41.8781,
        "longitude": -87.6298
    },

    "Seattle": {
        "latitude": 47.6062,
        "longitude": -122.3321
    },

    "Philadelphia": {
        "latitude": 39.9526,
        "longitude": -75.1652
    },

    "Detroit": {
        "latitude": 42.3314,
        "longitude": -83.0458
    },

    "Columbus": {
        "latitude": 39.9612,
        "longitude": -82.9988
    },


    # Canada

    "Toronto": {
        "latitude": 43.6532,
        "longitude": -79.3832
    },

    "Vancouver": {
        "latitude": 49.2827,
        "longitude": -123.1207
    },

    "Montreal": {
        "latitude": 45.5017,
        "longitude": -73.5673
    },

    "Calgary": {
        "latitude": 51.0447,
        "longitude": -114.0719
    },


    # Germany

    "Munich": {
        "latitude": 48.1351,
        "longitude": 11.5820
    },

    "Berlin": {
        "latitude": 52.5200,
        "longitude": 13.4050
    },

    "Frankfurt": {
        "latitude": 50.1109,
        "longitude": 8.6821
    },

    "Cologne": {
        "latitude": 50.9375,
        "longitude": 6.9603
    },


    # Sweden

    "Stockholm": {
        "latitude": 59.3293,
        "longitude": 18.0686
    },

    "Gothenburg": {
        "latitude": 57.7089,
        "longitude": 11.9746
    },

    "Malmo": {
        "latitude": 55.6050,
        "longitude": 13.0038
    },


    # UK

    "London": {
        "latitude": 51.5074,
        "longitude": -0.1278
    },

    "Manchester": {
        "latitude": 53.4808,
        "longitude": -2.2426
    },

    "Edinburgh": {
        "latitude": 55.9533,
        "longitude": -3.1883
    },


    # France

    "Paris": {
        "latitude": 48.8566,
        "longitude": 2.3522
    },

    "Toulouse": {
        "latitude": 43.6047,
        "longitude": 1.4442
    },

    "Lyon": {
        "latitude": 45.7640,
        "longitude": 4.8357
    },


    # India

    "Mumbai": {
        "latitude": 19.0760,
        "longitude": 72.8777
    },

    "Bangalore": {
        "latitude": 12.9716,
        "longitude": 77.5946
    },

    "Delhi": {
        "latitude": 28.6139,
        "longitude": 77.2090
    },

    "Chennai": {
        "latitude": 13.0827,
        "longitude": 80.2707
    },


    # Japan

    "Tokyo": {
        "latitude": 35.6762,
        "longitude": 139.6503
    },

    "Osaka": {
        "latitude": 34.6937,
        "longitude": 135.5023
    },

    "Kyoto": {
        "latitude": 35.0116,
        "longitude": 135.7681
    },


    # Australia

    "Sydney": {
        "latitude": -33.8688,
        "longitude": 151.2093
    },

    "Melbourne": {
        "latitude": -37.8136,
        "longitude": 144.9631
    },

    "Brisbane": {
        "latitude": -27.4698,
        "longitude": 153.0251
    },


    # Netherlands

    "Amsterdam": {
        "latitude": 52.3676,
        "longitude": 4.9041
    },

    "Rotterdam": {
        "latitude": 51.9244,
        "longitude": 4.4777
    },

    "Utrecht": {
        "latitude": 52.0907,
        "longitude": 5.1214
    }

}



# =====================================================
# LOCATION DOMAIN
# =====================================================


LOCATION_TYPES = [

    "Manufacturing Plant",

    "Warehouse",

    "Distribution Center",

    "Corporate Office",

    "Research Facility"

]


OPERATING_STATUS = [

    "Active",

    "Inactive",

    "Under Maintenance"

]



# =====================================================
# CUSTOMER DOMAIN
# =====================================================


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

    "Logistics",

    "Automotive"

]



# =====================================================
# PRODUCT DOMAIN
# =====================================================


PRODUCT_CATEGORIES = [

    "Industrial Equipment",

    "Software",

    "Electronics",

    "Healthcare Equipment",

    "Consumer Products",

    "Automotive Parts",

    "Renewable Energy Equipment"

]


PRODUCT_STATUS = [

    "Active",

    "Discontinued",

    "Under Development"

]



# =====================================================
# SUPPLIER DOMAIN
# =====================================================


SUPPLIER_CATEGORIES = [

    "Raw Materials",

    "Technology Provider",

    "Equipment Supplier",

    "Logistics Provider",

    "Packaging Supplier"

]


SUPPLIER_STATUS = [

    "Active",

    "Inactive",

    "Under Review"

]



# =====================================================
# WORKFORCE DOMAIN
# =====================================================


DEPARTMENTS = [

    "Engineering",

    "Sales",

    "Finance",

    "Human Resources",

    "Operations",

    "Supply Chain",

    "Information Technology",

    "Marketing",

    "Manufacturing"

]


JOB_TITLES = [

    "Data Analyst",

    "Senior Data Analyst",

    "Software Engineer",

    "Mechanical Engineer",

    "Operations Manager",

    "Financial Analyst",

    "Product Manager",

    "Sales Representative",

    "Manufacturing Engineer",

    "HR Specialist"

]


EMPLOYMENT_STATUS = [

    "Active",

    "Inactive",

    "On Leave"

]



# =====================================================
# MANUFACTURING DOMAIN
# =====================================================


MACHINE_TYPES = [

    "CNC Machine",

    "Assembly Line",

    "Robotic Arm",

    "Packaging Machine",

    "Injection Molding Machine"

]


MACHINE_MANUFACTURERS = [

    "Siemens",

    "ABB",

    "Bosch",

    "GE Manufacturing",

    "Fanuc",

    "Honeywell"

]


PRODUCTION_STATUS = [

    "Completed",

    "Failed",

    "In Progress"

]


MAINTENANCE_TYPES = [

    "Preventive",

    "Corrective",

    "Emergency"

]



# =====================================================
# FINANCE DOMAIN
# =====================================================


ACCOUNT_TYPES = [

    "Revenue",

    "Expense",

    "Asset",

    "Liability",

    "Equity"

]


TRANSACTION_TYPES = [

    "Revenue",

    "Purchase",

    "Payroll",

    "Operating Expense",

    "Investment"

]



# =====================================================
# ESG DOMAIN
# =====================================================


ENERGY_SOURCES = [

    "Electricity",

    "Natural Gas",

    "Solar",

    "Wind"

]


EMISSION_TYPES = [

    "CO2",

    "Methane",

    "Nitrous Oxide"

]


WASTE_TYPES = [

    "Plastic",

    "Metal",

    "Chemical",

    "Organic"

]



# =====================================================
# SALES DOMAIN
# =====================================================


SALES_CHANNELS = [

    "Online",

    "Direct Sales",

    "Partner",

    "Retail"

]


# =====================================================
# MACHINE DOMAIN
# =====================================================


MACHINE_STATUS = [

    "Operational",

    "Idle",

    "Under Maintenance",

    "Retired"

]



# =====================================================
# PRODUCTION DOMAIN
# =====================================================


PRODUCTION_TYPES = [

    "Assembly",

    "Fabrication",

    "Packaging",

    "Quality Inspection"

]



# =====================================================
# MAINTENANCE DOMAIN
# =====================================================


MAINTENANCE_STATUS = [

    "Completed",

    "Scheduled",

    "Pending",

    "Cancelled"

]



# =====================================================
# FINANCE DOMAIN EXTENSIONS
# =====================================================


BUDGET_CATEGORIES = [

    "Operations",

    "Marketing",

    "Research",

    "Manufacturing",

    "Technology",

    "Human Resources"

]



# =====================================================
# ESG DOMAIN EXTENSIONS
# =====================================================


EMISSION_SCOPES = [

    "Scope 1",

    "Scope 2",

    "Scope 3"

]



EMISSION_SOURCES = [

    "Manufacturing",

    "Transportation",

    "Energy Consumption",

    "Business Travel"

]



DISPOSAL_METHODS = [

    "Recycling",

    "Landfill",

    "Incineration",

    "Composting"

]


WASTE_CATEGORIES = [

    "Plastic",

    "Metal",

    "Chemical",

    "Organic",

    "Electronic"

]



# =====================================================
# INVENTORY DOMAIN
# =====================================================


INVENTORY_STATUS = [

    "Available",

    "Reserved",

    "Damaged",

    "Out of Stock"

]



# =====================================================
# ACCOUNTING EXTENSIONS
# =====================================================


CURRENCIES = [

    "USD",

    "EUR",

    "SEK",

    "INR",

    "GBP"

]


PAYMENT_METHODS = [

    "Credit Card",

    "Bank Transfer",

    "Invoice",

    "Direct Debit"

]

# =====================================================
# OUTPUT
# =====================================================


OUTPUT_PATH = "../output/"