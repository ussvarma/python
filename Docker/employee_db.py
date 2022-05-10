import sqlite3

conn = sqlite3.connect("company.db")  # for establishing connection with database

cursor = conn.cursor()  # for creating table
sql_query = """CREATE TABLE tblemployee(
      id integer PRIMARY KEY autoincrement,
      name varchar(100) NOT NULL,
      department varchar(100) NOT NULL,
      phone varchar(100) NOT NULL
      )
"""

cursor.execute(sql_query)
