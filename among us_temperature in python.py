from tkinter import *
import random

win = Tk()
win.title('temperature mission')
win.geometry('300x250')
win.resizable(width=False, height=True)

text1 = random.randint(-32, -20)

def btnpress():
    global text1
    text1 += 1
    print(text1)


tp = Label(win, text='temperature', bg='yellow')
tp.pack()

a = Frame(win)
a.pack()
aim = Label(a, text='aim')
aim.pack()
upbtn = Button(a, text='up', command=btnpress)
upbtn.pack()
view1 = Label(a, text=text1)

win.mainloop()