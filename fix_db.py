import sqlite3

conn = sqlite3.connect("projects.db")
c = conn.cursor()

try:
    c.execute("ALTER TABLE projects ADD COLUMN writer TEXT")
    print("Writer column added.")
except:
    print("Writer column already exists.")

conn.commit()
conn.close()
