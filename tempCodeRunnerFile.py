import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()

# Add date column if not exists
try:
    c.execute("ALTER TABLE projects ADD COLUMN date TEXT")
    print("Date column added.")
except:
    print("Date column already exists.")

conn.commit()
conn.close()
