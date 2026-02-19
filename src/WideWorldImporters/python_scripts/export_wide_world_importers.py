import pandas as pd
import argparse
from WideWorldImporters.utils.mssql_connection import server_connect
from jinja2 import Template
import os

# Create connection to MSSQL
conn = server_connect()

# Create the arguments parser
parser = argparse.ArgumentParser(
    prog="WideWorldImporters",
    description="Query the Purchasing schema fromm WideWorldImporters to replicate the report in tests/fixtures",
)


# Add arguments
parser.add_argument("--trc-type", default=5, type=int, help="Transaction type")
parser.add_argument(
    "--trc-month", default=11, type=int, help="Transaction month (e.g.: 1, 2, ... 12)"
)
parser.add_argument("--trc-year", default=2015, type=int, help="Transaction year")

# Grab arguments
args = parser.parse_args()

# Parse sql code
with open(
    r"src\WideWorldImporters\sql_scripts\wide_world_importers_report.sql", "r"
) as f:
    sql_template = Template(f.read())

# Assign arguments to be used in the sql script
sql_query = sql_template.render(
    transaction_type=args.trc_type,
    transaction_month=args.trc_month,
    transaction_year=args.trc_year,
)

report = pd.read_sql(sql_query, conn)

# Save the result to an excel file
os.makedirs("outputs", exist_ok=True)
report.to_excel("outputs/report.xlsx", index=False)

# Close connection to the server
conn.close()
