# importing libraries
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# connection with database
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("company.db")
        conn.row_factory = sqlite3.Row

    except Exception as e:
        print(e)
    return conn


@app.route('/')
def index():
    conn = db_connection()
    cur = conn.cursor()
    # cur.execute("""INSERT INTO tblemployee(name,email, department,phone)
    #                         VALUES ("ussvarma","email","depart","phone")
    #                     """)
    # cur.execute("""DELETE FROM tblemployee
    #             WHERE name="ussvarma" and email="email" and department="depart" and phone="phone";""")
    cur.execute("SELECT * FROM tblemployee ORDER BY id")
    employee = cur.fetchall()
    # print(employee)
    return render_template('index.html', employee=employee)


# for adding new row
@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    conn = db_connection()
    cur = conn.cursor()
    # function for adding new record
    if request.method == 'POST':
        # print("post working")
        txtname = request.form['txtname']
        txtemail = request.form['txtemail']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        # print(txtname)
        if txtname == '':
            msg = 'Please Input name'
        elif txtemail == "":
            msg = "please input email"
        elif txtdepartment == '':
            msg = 'Please Input Department'
        elif txtphone == '':
            msg = 'Please Input Phone'
        else:
            sql = "SELECT * from tblemployee where email like ?"
            cur.execute(sql, [txtemail])
            result = cur.fetchall()
            # print(result)
            if len(result) >= 1:
                msg = "entered duplicated record"
            else:
                sql = """INSERT INTO tblemployee(name,email, department,phone) 
                            VALUES (?,?,?,?)
                        """
                cur.execute(sql,
                            (txtname, txtemail, txtdepartment, txtphone))
                conn.commit()
                cur.close()
                msg = 'New record created successfully'
    return jsonify(msg)


# for updating the record
@app.route("/ajax_update", methods=["POST", "GET"])
def ajax_update():
    conn = db_connection()
    cur = conn.cursor()
    # for updating recording
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtemail= request.form['txtemail']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        # print(string)
        sql = "SELECT * from tblemployee where email like ?"
        cur.execute(sql, [txtemail])
        result = cur.fetchall()
        # print(result)
        if len(result) >= 1:
            msg = "entered duplicated record"
        else:
            cur.execute("UPDATE tblemployee SET name = ?, email=?,department = ?, phone = ? WHERE id = ? ",
                        (txtname, txtemail, txtdepartment, txtphone, string))
            conn.commit()
            cur.close()
            msg = 'Record successfully Updated'
    return jsonify(msg)


# for deleting the record
@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    conn = db_connection()
    cur = conn.cursor()
    # for deleting record
    if request.method == 'POST':
        getid = request.form['string']
        # print(getid)
        cur.execute('DELETE FROM tblemployee WHERE id = {0}'.format(getid))
        conn.commit()
        cur.close()
        msg = 'Record deleted successfully'
    return jsonify(msg)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
