from tkinter import *
import sqlite3
#import tkinter as tk


conn = sqlite3.connect("library.db")
c = conn.cursor()
c.execute("INSERT INTO Library_database values('shakxcvckd','shxcvxcdds','dsfxcvxcsdfsd','sdxcvxcfsdf')")
c.execute("""Select * from Library_database""")
print(c.fetchall())
'''c.execute("""CREATE TABLE Library_database (
         title text,
         author text,
         year text,
         ISBN text)""") '''

#create window objet
window =Tk()
#window = tk.Tk()
def view_all_records():
    list1.delete()
    c.execute("""Select * from Library_database""")
    list1.insert(END, c.fetchall())
def on_click():
    title = textBox.get("1.0","end-1c")
    author = author_text.get("1.0","end-1c")
    year = year_text.get("1.0","end-1c")
    isbn = isbn_text.get("1.0","end-1c")
    c.execute("INSERT IN"
              "TO Library_database values(?,?,?,?)",(title,author,year,isbn))
    c.execute("""Select * from Library_database""")
    rows = c.fetchall()
    for row in rows:
     list1.insert(END,row)

def search_entry():
    title = textBox.get("1.0", "end-1c")
    author = author_text.get("1.0", "end-1c")
    year = year_text.get("1.0", "end-1c")
    isbn = isbn_text.get("1.0", "end-1c")
    c.execute("select * from Library_database where title = ? OR author = ? OR year = ? OR ISBN = ?",(title,author,year,isbn))
    print(c.fetchall())
  #list1.insert(END, c.fetchall())
    #c.execute(sql,(title,author,year,isbn))
#    c.execute("""Select * from Library_database where """)

def close_window():
    window.destroy()
#define four label title author year ISBN

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l1=Label(window,text="Author")
l1.grid(row=0,column=2)

l1=Label(window,text="Year")
l1.grid(row=1,column=0)

l1=Label(window,text="ISBN")
l1.grid(row=1,column=2)

#define Entities
#title_text=StringVar()
#e1=Entry(window,textvariable=title_text)
#e1.grid(row=0,column=1)

textBox=Text(window, height=1, width=15)
textBox.grid(row=0,column=1)

author_text=Text(window, height=1, width=15)
author_text.grid(row=0,column=3)

year_text=Text(window, height=1, width=15)
year_text.grid(row=1,column=1)

isbn_text=Text(window, height=1, width=15)
isbn_text.grid(row=1,column=3)


#define list
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#attach scrollebar to list

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(xscrollcommand=sb1.set)
sb1.configure(command=list1.xview)

#define button
window.bind("<Return>", view_all_records)
b1=Button(window,text="View All",command=view_all_records,width=12)
b1.grid(row=2,column=3)

window.bind("<Return>", search_entry)
b1=Button(window,text="Search Entry",command=search_entry,width=12)
b1.grid(row=3,column=3)

window.bind("<Return>", on_click)
b1=Button(window,text="Add Entry",command=on_click,width=12)
b1.grid(row=4,column=3)

b1=Button(window,text="Update Entry",width=12)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete Selected",width=12)
b1.grid(row=6,column=3)

window.bind("<Return>", close_window)
b1=Button(window,text="Close",command=close_window,width=12)
b1.grid(row=7,column=3)



window.mainloop()


