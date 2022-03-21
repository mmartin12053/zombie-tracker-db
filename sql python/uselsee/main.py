import sqlite3
from datetime import date

conn = sqlite3.connect('test.db')
c = conn.cursor()

def go():
    global conn, c

    F_name = input("what is your first name:\n")
    L_name = input("what is your last name:\n")
    user_email = input("what is your Email:\n")
    t = date.today()

    print(F_name)
    print(L_name)
    print(user_email)
    print(t)
    



    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS testTable(first_name TEXT, last_name TEXT, user_email TEXT, timestamp TEXT)')

    def data_entry():
        c.execute(f'INSERT INTO testTable VALUES("{F_name}", "{L_name}", "{user_email}", "{t}")')
        conn.commit()



    create_table()
    data_entry()

def read_from_db():
    global conn, c


    c.execute("SELECT * FROM testTable")
    data = c.fetchall()
    print(data)
    k = input("press an key to continue:\n")


def main():

    prompt = int(input("would you like to add a new record(1), see the record(2) or end the program(3):\n"))

    if prompt == 1:
        print("you have chosen option 1:\n")
        go()
        main()
    elif prompt == 2:
        print("you have chosen option 2:\n")
        read_from_db()
        main()
    elif prompt == 3:
        print("goodbye")
        c.close()
        conn.close()
    else:
        print("command not recognized, please try again:\n")
        main()



