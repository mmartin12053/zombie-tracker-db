import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS testTable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute(f'INSERT INTO testTable VALUES(8675309, "today", "pizza", 26)')
    conn.commit()
    c.close()
    conn.close()



create_table()
data_entry()