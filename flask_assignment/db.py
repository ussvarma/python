import sqlite3

conn = sqlite3.connect("books.sqlite")  # for establishing connection with database

cursor = conn.cursor()  # for creating table
sql_query = """CREATE TABLE book(
      id integer PRIMARY KEY,
      author text NOT NULL,
      language text NOT NULL,
      title text NOT NULL
      )
"""

cursor.execute(sql_query)
