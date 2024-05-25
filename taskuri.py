from tkinter import *


class taskuri:

    nr_taskuri = 0

    def __init__(self, root, entry, x, y):
        self.checkbutton = Checkbutton(root, bg="#D9D9D9")
        self.label = Label(root, bg="#D9D9D9", text=entry.get())
        entry.delete(0, END)
        self.checkbutton.place(x=x, y=y)
        self.label.place(x=2 * x, y=y)
        taskuri.nr_taskuri += 1
