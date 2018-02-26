from tkinter import *

window = Tk()                       # Create a empty window container

def km_to_miles():
    print(e1_value.get())            # Gets the value entered in the entry box
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)            # outputs the value onto text box


b1 = Button(window, text='Execute', command=km_to_miles)        # Creating a button
b1.grid(row=0, column=0)                   # Specify where you want the button to be in the window

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)                         # Creating the Entry field
e1.grid(row=0, column=1)

t1 = Text(window,height=1,width=20)        # Creating text field
t1.grid(row=0, column=2)

window.mainloop()                          # This is mandatory for the window to be in open until closed by the user