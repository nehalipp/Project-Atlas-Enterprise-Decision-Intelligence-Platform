"""
Project Atlas
CSV Source Configuration

Defines all CSV sources and their target raw tables.
"""

CSV_SOURCES = {

    # ==========================
    # Dimension Tables
    # ==========================

    "accounts": {
        "file": "dimensions/accounts/output/raw_accounts.csv",
        "schema": "raw",
        "table": "accounts"
    },

    "customers": {
        "file": "dimensions/customers/output/raw_customers.csv",
        "schema": "raw",
        "table": "customers"
    },

    "products": {
        "file": "dimensions/products/output/raw_products.csv",
        "schema": "raw",
        "table": "products"
    },

    "suppliers": {
        "file": "dimensions/suppliers/output/raw_suppliers.csv",
        "schema": "raw",
        "table": "suppliers"
    },

    "locations": {
        "file": "dimensions/locations/output/raw_locations.csv",
        "schema": "raw",
        "table": "locations"
    },

    "employees": {
        "file": "dimensions/employees/output/raw_employees.csv",
        "schema": "raw",
        "table": "employees"
    },

    "machines": {
        "file": "dimensions/machines/output/raw_machines.csv",
        "schema": "raw",
        "table": "machines"
    },


    # ==========================
    # Fact Tables
    # ==========================

    "sales_transactions": {
        "file": "facts/sales/output/raw_sales_transactions.csv",
        "schema": "raw",
        "table": "sales_transactions"
    },

    "production": {
        "file": "facts/production/output/raw_production.csv",
        "schema": "raw",
        "table": "production"
    },

    "maintenance": {
        "file": "facts/maintenance/output/raw_maintenance.csv",
        "schema": "raw",
        "table": "maintenance"
    },

    "financial_transactions": {
        "file": "facts/finance/output/raw_financial_transactions.csv",
        "schema": "raw",
        "table": "financial_transactions"
    },

    "budget": {
        "file": "facts/budgets/output/raw_budget.csv",
        "schema": "raw",
        "table": "budget"
    },

    "energy_consumption": {
        "file": "facts/energy/output/raw_energy_consumption.csv",
        "schema": "raw",
        "table": "energy_consumption"
    },

    "emissions": {
        "file": "facts/emissions/output/raw_emissions.csv",
        "schema": "raw",
        "table": "emissions"
    },

    "waste": {
        "file": "facts/waste/output/raw_waste.csv",
        "schema": "raw",
        "table": "waste"
    },

    "inventory": {
        "file": "facts/inventory/output/raw_inventory.csv",
        "schema": "raw",
        "table": "inventory"
    }

}