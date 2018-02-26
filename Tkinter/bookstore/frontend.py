"""
This program stores the book information such as:
---------------------------------------------------------------
Title, Author, ISBN, Year

Also, the user can perform the following operations on the app:
----------------------------------------------------------------
View all records,
Search for a record
Add a record
Delete a record
Update a record
close

"""
import backend
from tkinter import *


def view_all():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)


def insert_command():
    backend.insert(str(title_text.get()),author_text.get(),year_text.get(),isbn_text.get())



def update_command():


def delete_command():





window = Tk()
window.title("Book Store")

l1= Label(window,text='Title')
l1.grid(row=0,column=0)

l2= Label(window,text='Author')
l2.grid(row=0,column=2)

l3= Label(window,text='Year')
l3.grid(row=1,column=0)

l4= Label(window,text='ISBN')
l4.grid(row=1,column=2)

title_text=StringVar()
e1= Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2= Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3= Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4= Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text='View all',width=12,command=view_all)
b1.grid(row=2,column=3)

b2=Button(window,text='Search entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text='Add entry',width=12,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(window,text='Update',width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text='Delete',width=12,command=delete_command)
b5.grid(row=6,column=3)



window.mainloop()