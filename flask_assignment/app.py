# importing libraries
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


# connection with database
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except Exception as e:
        print(e)
    return conn


@app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connection()
    conn.cursor()

    if request.method == "GET":  # retrieves information
        cursor = conn.execute("SELECT * FROM book")  # query
        books = []
        for row in cursor.fetchall():
            books.append(dict(id=row[0], author=row[1], language=row[2], title=row[3]))
        if books is not None:
            return jsonify(books)

    if request.method == "POST":  # for adding new data
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        # query for inserting a row  into table
        sql = """INSERT INTO book (author, language,title) 
            VALUES (?,?,?)
        """
        cursor = conn.execute(sql, (new_author, new_lang, new_title))
        conn.commit()  # saving the changes
        return f"Book with the id: {cursor.lastrowid} created successfully"


@app.route("/book/<int:id>", methods=["GET", "POST", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200  # indicates request has been succeeded
        else:
            return "Something wrong", 404  # the server cannot find the requested resource.

    if request.method == "PUT":  # for updating existing data
        sql = """UPDATE book SET 
                title=?,
                author=?,
                language=?
            WHERE id=?"""
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title
        }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":  #for deleting existing data
        sql = """ DELETE FROM book  WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "The book  with id:{} has been deleted ".format(id, ), 200


if __name__ == '__main__':
    app.run(debug=True,port=5000)
