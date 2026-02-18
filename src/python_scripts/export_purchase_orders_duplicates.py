import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

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
with open(r"src\sql_scripts\purchase_orders_deduplication.sql", "r") as f:
    sql_script = f.read()

purchase_orders_deduplication_df = pd.read_sql(sql_script, conn)
purchase_orders_deduplication_df.to_excel("outputs/purchase_orders_deduplication.xlsx", index=False)