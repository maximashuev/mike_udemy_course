import sqlite3


def get_connection():
    con = sqlite3.connect("database.sqlite3")
    con.execute("""
        CREATE TABLE IF NOT EXISTS data
        (username TEXT,password TEXT)
    """)
    return con

def insert_data(conection, username, password):
    cursor = conection.cursor()
    cursor.execute("INSERT INTO data VALUES(?,?)", (username, password))
    conection.commit()
    print("Account successfully created!\n" + "Welcome,{}.".format(username))


def verify_username(conection, username):
    cursor = conection.cursor()
    username_from_data= cursor.execute("SELECT username FROM data WHERE username =(?)", (username,)).fetchall()
    # print("Existing customer:",(name[0][0]))
    return (username_from_data[0][0])

def verify_password(conection,username):
    cursor=conection.cursor()
    pass_from_data=cursor.execute("SELECT password FROM data WHERE username =(?)",(username,)).fetchall()
    # print("Correct password")
    return (pass_from_data[0][0])

def close_account_by_name(connection, username):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE username = ?", (username,))
    connection.commit()
    print("Данные успешно удалены")