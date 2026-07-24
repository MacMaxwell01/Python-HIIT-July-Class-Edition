import sqlite3

# Opening the database
conn = sqlite3.connect("testing.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS
    students(
    id INTEGER PRIMARY KEY,
    matric_number TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT
    )
""")

# putting values into the table

query = """
INSERT INTO students (matric_number, first_name, last_name)
    VALUES(?, ?, ?)
"""

cursor.execute(query, (19083848, "AdeQudud", "Qudud"))
cursor.execute(query, (19064042, "another student", "Student Last name"))

conn.commit()
cursor.close()
conn.close()