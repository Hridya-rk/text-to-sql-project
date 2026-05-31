import pandas as pd
import sqlite3

df = pd.read_csv("../data/sample.csv")

conn = sqlite3.connect("project.db")

df.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

print("Database created")