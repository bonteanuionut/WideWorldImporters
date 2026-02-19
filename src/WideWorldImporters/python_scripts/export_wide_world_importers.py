import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv
import argparse

# Load credentials
load_dotenv()

# Store credentials into their specific variables
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create connection to MSSQL
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

# Parse sql code
with open(r"src\sql_scripts\wide_world_importers_report.sql", "r") as f:
    sql_script = f.read()

# Create the arguments parser
parser = argparse.ArgumentParser(
                    prog="WideWorldImporters",
                    description="Query the Purchasing schema fromm WideWorldImporters to replicate the report in tests/fixtures"
                )


# Add arguments
parser.add_argument("-tt", "--trc-type", type = int, required = True, help = "Transaction type")
parser.add_argument("-tm", "--trc-month", type = int, required = True, help = "Transaction month (e.g.: 1, 2, ... 12)")
parser.add_argument("-ty", "--trc-year", type = int, required = True, help = "Transaction year")

# Grab arguments
args = parser.parse_args()

# Assign arguments to be used in the sql script (order matters)
params = [args.trc_type, args.trc_month, args.trc_year]
report = pd.read_sql(sql_script, conn, params=params)

# Save the result to an excel file
report.to_excel("outputs/report.xlsx", index=False)