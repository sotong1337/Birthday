from flask import Flask, request, render_template, redirect, url_for
import os, sqlite3
from datetime import date
#datetime only imported to get today's date
from helper import *

dir_file = os.path.abspath(os.path.dirname(__file__))
db = os.path.join(dir_file, "../bday_list.db")

app = Flask(__name__)

today = date.today()
tdy_day = today.strftime("%d")
tdy_month = today.strftime("%m")
tdy_year = today.strftime("%Y")

@app.route('/')
def home():

    query = """SELECT Names.Name, Birthday.Notes, Birthday.Secret
            FROM Names, Birthday
            WHERE Birthday.day = ?
            And Birthday.month = ?
            And Birthday.ID = Names.ID"""

    conn = sqlite3.connect(db)
    cursor = conn.execute(query, (int(tdy_day), int(tdy_month)))
    data = cursor.fetchall()

    conn.close()
    
    names = []
    messages = []
    secret = []

    txt1 = tdy_day + "/" + tdy_month

    for i in data:
        names.append(i[0])
        messages.append(i[1])
        secret.append(i[2])
    
    bday = False

    n = len(data)
    if n > 0:
        bday = True

    upcoming_date = add_n_days_from_a_date(tdy_day + tdy_month + tdy_year, 30)
    upcoming_day = upcoming_date[:2]
    upcoming_month = upcoming_date[2:4]
    upcoming_year = upcoming_date[4:]
    
    query = """SELECT Names.Name, Birthday.day, Birthday.month
        FROM Names, Birthday
        WHERE ((Birthday.day > ? AND Birthday.month = ?)
        OR (Birthday.day < ? AND Birthday.month = ?))
        And Birthday.ID = Names.ID"""

    conn = sqlite3.connect(db)
    cursor = conn.execute(query, (int(tdy_day), int(tdy_month), int(upcoming_day), int(upcoming_month)))
    data2 = cursor.fetchall()

    conn.close()

    data_lst2 = []

    for i in data2:

        weekday = weekday_of_date(f"{str(i[1]).zfill(2)}{str(i[2]).zfill(2)}{tdy_year}")

        if upcoming_month == "01":
            weekday = weekday_of_date(f"{str(i[1]).zfill(2)}{str(i[2]).zfill(2)}{upcoming_year}")

        data_lst2.append([i[0], i[1], i[2], weekday])

    return render_template("index.html", bday = bday, txt1 = txt1, n = n, names = names, messages = messages, data_lst2 = data_lst2)

@app.route('/db_view')
def db_view():

    query = """SELECT Names.ID, Names.Name, Birthday.day, Birthday.month, Birthday.notes
        FROM Names, Birthday
        WHERE Birthday.ID = Names.ID
        ORDER BY Birthday.month, Birthday.day"""

    conn = sqlite3.connect(db)
    cursor = conn.execute(query)
    data = cursor.fetchall()

    conn.close()

    id_ = []
    names = []
    days = []
    months = []
    notes = []
    n = len(data)

    for i in data:
        id_.append(i[0])
        names.append(i[1])
        days.append(i[2])
        months.append(i[3])
        notes.append(i[4])

    return render_template("db_view.html", n = n, id_ = id_, names = names, days = days, months = months, notes = notes)

@app.route('/edit_data/<id_>')
def edit_data(id_):

    query = """SELECT Names.ID, Names.Name, Birthday.day, Birthday.month, Birthday.notes
        FROM Names, Birthday
        WHERE Birthday.ID = Names.ID AND Names.ID = ?"""

    conn = sqlite3.connect(db)
    cursor = conn.execute(query, (id_, ))
    data = cursor.fetchall()

    conn.close()

    id_, name_, day, month, notes = data[0]

    return render_template("edit_data.html", id_ = id_, name_ = name_, day = day, month = month, notes = notes)

@app.route('/process_edit', methods = ['GET', 'POST'])
def process_edit():
    if request.method == "POST":
        id_ = request.form["id_"]
        name_ = request.form["name_"]
        days = request.form["days"]
        months = request.form["months"]
        msg = request.form["message"]

        query = """ UPDATE Names
        SET Name = ?
        WHERE ID = ?"""

        query2 = """ UPDATE Birthday
        SET Day = ?, Month = ?, Notes = ?
        WHERE ID = ?"""
        
        conn = sqlite3.connect(db)
        conn.execute(query, (name_, id_))
        conn.execute(query2, (days, months, msg, id_))

        conn.commit()
        conn.close()

        return redirect("/edit_data/" + id_)

    else:
        id_ = request.args["id_"]

        conn = sqlite3.connect(db)
        conn.execute("DELETE FROM Names WHERE ID = ?", (id_,))
        conn.execute("DELETE FROM Birthday WHERE ID = ?", (id_,))

        conn.commit()
        conn.close()

        return redirect(url_for("db_view"))

@app.route('/add_profile', methods = ['GET', 'POST'])
def add_profile():

    if request.method == "GET":
        return render_template("new_profile.html")
    
    else:
        name_ = request.form["name_"]
        days = request.form["days"]
        months = request.form["months"]
        msg = request.form["message"]

        query = "INSERT INTO Names(Name) VALUES(?)"
        query2 = "INSERT INTO Birthday(Day, Month, Notes) VALUES(?, ?, ?)"

        conn = sqlite3.connect(db)
        conn.execute(query, (name_, ))
        conn.execute(query2, (days, months, msg))

        conn.commit()
        conn.close()

        return redirect(url_for("db_view"))

@app.route('/hw')
def hw():
    return render_template("hw.html")

@app.route('/result')
def hw_process():

    opt = request.args["opt"]

    try:
        if opt == "is_leap_year":
            y = request.args["y"]
            ans = is_leap_year(int(y))
        
        if opt == "days_in_month":
            y = request.args["m"]
            ans = days_in_month(int(y))

        if opt == "num_of_leap_years":
            y = request.args["y1"]
            y2 = request.args["y2"]
            ans = num_of_leap_years(int(y), int(y2))

        if opt == "is_valid_date":
            y = request.args["d"]
            ans = False
            if num_of_days_from_1900(y):
                ans = True

        if opt == "num_of_days_from_1900":
            y = request.args["d1"]
            ans = num_of_days_from_1900(y)

        if opt == "days_between_2_dates":
            y = request.args["d2"]
            y2 = request.args["d3"]
            ans = days_between_2_dates(y, y2)

        if opt == "add_n_days_after_1900":
            y = request.args["n"]
            ans = add_n_days_after_1900(int(y))

        if opt == "add_n_days_from_a_date":
            y = request.args["n1"]
            y2 = request.args["d4"]
            ans = add_n_days_from_a_date(y2, int(y))

        if opt == "weekday_of_date":
            y = request.args["d5"]
            ans = weekday_of_date(y)
    except:
        ans = False
    return render_template("hw_process.html", ans = ans)
    

if __name__ == "__main__":
    app.run(debug = True)