#!/usr/bin/python

import Tkinter
import tkMessageBox

top = Tkinter.Tk()


def helloCallBack():
    tkMessageBox.showinfo("Title", "Message")


B = Tkinter.Button(top, text="Hello", command=helloCallBack)
BB = Tkinter.Button(top, text="Hello2", command=helloCallBack)

B.pack()
BB.pack()
top.mainloop()
