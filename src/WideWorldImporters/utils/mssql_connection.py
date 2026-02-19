import pyodbc
import os
from dotenv import load_dotenv

def server_connect():
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

    return conn