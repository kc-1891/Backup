from tkinter import *

class oops:

    def __init__(self,*args):
        self.frame = Frame(*args)
        self.frame.pack()

        self.PrintButton = Button(self.frame,text='Print text',command=self.print_text)
        self.PrintButton.pack(side=LEFT)

        self.ExitButton = Button(self.frame,text='Exit',command=self.frame.quit)
        self.ExitButton.pack(side=RIGHT)

        menu = Menu(*args)
        self.frame.config(menu=menu)

        submenu = Menu(menu)
        menu.add_cascade(label='file',menu=submenu)
        submenu.add_command(label='Now project',command=self.doNothing)
        submenu.add_separator()
        submenu.add_command(label='final project', command=self.doNothing)

        editMenu = Menu(menu)
        menu.add_cascade(label='edit',menu=editMenu)
        submenu.add_command(label='edit now',command=self.doNothing)
        submenu.add_separator()
        submenu.add_command(label='change', command=self.doNothing)


    def print_text(self):
        print('this is working correctly')



    def doNothing(self):
        print('Do nothing')


root = Tk()
ab1 = oops(root)

# child = Tk()
# ab2 = oops(child)
root.mainloop()
