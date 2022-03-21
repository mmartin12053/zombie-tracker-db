from cProfile import label
from faulthandler import disable
import sqlite3
from tkinter import *
from turtle import width
import uselsee.main as main

root = Tk()

name = Label(root, width = 35, text="name:")
e_name = Entry(root, width=35)
age = Label(root, width = 35, text='age:')
e_age = Entry(root, width=35)
type = Label(root, width = 35, text="type")
e_type = Entry(root, width=35)
lkl = Label(root, width = 35, text="last known location:")
e_lkl = Entry(root, width=35)
specialty = Label(root, width = 35, text="specialty")
e_specialty = Entry(root, width=35)
eats = Label(root, width = 35, text="what does it eat")
e_eats = Entry(root, width=35)

name.pack()
e_name.pack()
age.pack()
e_age.pack()
type.pack()
e_type.pack()
lkl.pack()
e_lkl.pack()
specialty.pack()
e_specialty.pack()
eats.pack()
e_eats.pack()



def click():
    mylable = Label(root, text= e_name.get())
    mylable.pack()
    name = str(e_name.get())

    mylable = Label(root, text= e_age.get())
    mylable.pack()
    age = str(e_age.get())

    mylable = Label(root, text= e_type.get())
    mylable.pack()
    type = str(e_type.get())

    mylable = Label(root, text= e_lkl.get())
    mylable.pack()
    lkl = str(e_lkl.get())

    mylable = Label(root, text= e_specialty.get())
    mylable.pack()
    specialty = str(e_specialty.get())

    mylable = Label(root, text= e_eats.get())
    mylable.pack()
    eats = str(e_eats.get())

    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS zombie(name TEXT, age TEXT, type TEXT, location TEXT, specialty TEXT, eats TEXT)')

    def data_entry():
        c.execute(f'INSERT INTO zombie VALUES("{name}", "{age}", "{type}", "{lkl}", "{specialty}", "{eats}")')
        conn.commit()
        c.close()
        conn.close()
        print("done")

    create_table()
    data_entry()

myButton = Button(root, text = 'submit', padx=50, pady=50, command=click)

myButton.pack()

root.mainloop() 






