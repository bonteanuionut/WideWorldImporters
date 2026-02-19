import pandas as pd
from WideWorldImporters.utils.mssql_connection import server_connect

# Create connection to MSSQL
conn = server_connect()

# Parse sql code
with open(
    r"src\WideWorldImporters\sql_scripts\purchase_orders_deduplication.sql", "r"
) as f:
    sql_script = f.read()

purchase_orders_deduplication_df = pd.read_sql(sql_script, conn)
purchase_orders_deduplication_df.to_excel(
    "outputs/purchase_orders_deduplication.xlsx", index=False
)

conn.close()