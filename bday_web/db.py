import os, sqlite3, csv

dir_file = os.path.abspath(os.path.dirname(__file__))
db = os.path.join(dir_file, "bday_list.db")

def read_names():
    conn = sqlite3.connect(db)
    file = os.path.join(dir_file, "data files/Name_lst.csv")
    query = "INSERT INTO Names(ID, Name) VALUES(?, ?)"

    with open(file , "r") as f:
        r = csv.reader(f)
        next(r)
        for i in r:
            conn.execute(query, tuple(i))
    
    conn.commit()
    conn.close()

def read_bdays():
    conn = sqlite3.connect(db)
    file = os.path.join(dir_file, "data files/Bday_lst.csv")
    query = "INSERT INTO Birthday(ID, Day, Month, Notes, Secret) VALUES(?, ?, ?, ?, ?)"

    with open(file , "r") as f:
        r = csv.reader(f)
        next(r)
        for i in r:
            conn.execute(query, tuple(i))
    
    conn.commit()
    conn.close()

read_names()
read_bdays()