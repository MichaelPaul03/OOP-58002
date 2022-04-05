from tkinter import *
from tkinter import Listbox
from tkinter import ttk

win = Tk()
win.geometry("300x200+10+20")
win.title("Welcome to Python Programming")

# Button widget
btn = Button(win,text = "This is a button", fg = "Orange", bg = "Blue",bd=15)
btn.place(x=50, y=50)

# label widget
lbl = Label(win,text ="Gender", fg = "Blue", bg ="Yellow")
lbl.place(x=50, y=10)

# text field
txt = Entry(win,font =("Verdana",12),bd = 5)
txt.place(x=50,y=130)

# radio button

radio1 = Radiobutton(win, text = "Male", value = 1)
radio2 = Radiobutton(win, text = "Female", value = 2)
radio1.place(x=50, y=25)
radio2.place(x=110, y=25)

# list box

var = StringVar()
var.set("Student 1")

data = ("Student 1")
data1 = ("Student2")
data2 =("Student3")
lstbx: Listbox = Listbox(win,selectmode ="Single", height =5)

lstbx.insert(END,data)
lstbx.insert(END,data1)
lstbx.insert(END,data2)
lstbx.place(x=50, y=200)

cb = ttk.Combobox(win,values = data)
cb.place(x=50, y=300)


win.mainloop()

from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add', command = self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()