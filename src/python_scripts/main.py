import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

with open(r"src\sql_scripts\test.sql", "r") as f:
    sql_script = f.read()
report = pd.read_sql(sql_script, conn)

report.to_csv("outputs/report.csv", index=False)