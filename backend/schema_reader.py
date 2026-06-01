import sqlite3

conn = sqlite3.connect("project.db")

cursor = conn.cursor()

cursor.execute(
    "PRAGMA table_info(students)"
)

print(cursor.fetchall())