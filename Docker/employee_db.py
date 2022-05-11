import sqlite3

conn = sqlite3.connect("company.db")  # for establishing connection with database

cursor = conn.cursor()  # for creating table
sql_query = """CREATE TABLE tblemployee(
      id integer PRIMARY KEY autoincrement ,
      name varchar(100) ,
      email varchar(100) ,
      department varchar(100) ,
      phone varchar(100)
      )
"""

cursor.execute(sql_query)
