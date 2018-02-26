from tkinter import *

root = Tk()
root.geometry("400x600+200+1")
root.configure(background='powder blue')
root.title("Calculator")
frame1 = Frame(root, height=600, width=400,)
frame1.pack()

operator = ""


def button_click(num):
    global operator
    operator = operator + str(num)
    text_input.set(operator)


def button_clear():
    global operator
    operator = " "
    text_input.set(operator)


def button_equals():
    global operator
    equal = eval(text_input.get())
    operator = str(equal)
    text_input.set(equal)


text_input = StringVar()
display = Entry(frame1,bd=30,textvariable=text_input, insertwidth=6,bg='powder blue',relief=SUNKEN)
display.grid(columnspan=4)

bt7 = Button(frame1,text='7',padx=10,pady=25,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(7)).grid(row=2,column=0)

bt8 = Button(frame1,text='8',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(8)).grid(row=2,column=1)

bt9 = Button(frame1,text='9',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(9)).grid(row=2,column=2)

bt_plus = Button(frame1,text='+',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click("+")).grid(row=2,column=3)

bt4 = Button(frame1,text='4',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(4)).grid(row=3,column=0)

bt5 = Button(frame1,text='5',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(5)).grid(row=3,column=1)

bt6 = Button(frame1,text='6',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(6)).grid(row=3,column=2)

bt_minus = Button(frame1,text='-',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click("-")).grid(row=3,column=3)

bt1 = Button(frame1,text='1',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(1)).grid(row=4,column=0)

bt2 = Button(frame1,text='2',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(2)).grid(row=4,column=1)

bt3 = Button(frame1,text='3',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(3)).grid(row=4,column=2)

bt_mult = Button(frame1,text='*',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click("*")).grid(row=4,column=3)

bt0 = Button(frame1,text='0',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click(0)).grid(row=5,column=0)

bt_canc = Button(frame1,text='C',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=button_clear).grid(row=5,column=1)

bt_equal = Button(frame1,text='=',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=button_equals).grid(row=5,column=2)

bt_div = Button(frame1,text='/',padx=16,pady=16,bd=8,fg="black", font=('arial',20, 'bold'),
             bg='powder blue',command=lambda: button_click("/")).grid(row=5,column=3)

root.mainloop()
