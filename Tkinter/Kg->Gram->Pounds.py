from tkinter import *


def kg_convert():
    grams = float(kg_input.get()) * 1000
    t2.insert(END, grams)

    pounds = float(kg_input.get()) * 2.20462
    t3.insert(END, pounds)

    ounces = float(kg_input.get()) * 35.274
    t4.insert(END, ounces)


window = Tk()
window.title("Convert KG to other measures")

l1 = Label(window,text='KG')
l1.grid(row=0, column=0)

kg_input = StringVar()
e1 = Entry(window, textvariable=kg_input)
e1.grid(row=0, column=1)

b1 = Button(window, text='Convert', command=kg_convert)
b1.grid(row=0, column=2)

t2 = Text(window,height=1,width=20,relief="groove")
t2.grid(row=2,column=0)

t3 = Text(window, height=1, width=20)
t3.grid(row=2,column=1)

t4 = Text(window, height=1, width=20)
t4.grid(row=2,column=2)

window.mainloop()










