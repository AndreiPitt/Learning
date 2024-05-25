from tkinter import *


class taskuri:

    nr_taskuri = 0
    obiecte = []

    def __init__(self, root, entry, x, y):
        self.checkbutton = Checkbutton(root, bg="#D9D9D9")
        self.label = Label(root, bg="#D9D9D9", text=entry.get())
        entry.delete(0, END)
        self.checkbutton.place(x=x, y=y)
        self.label.place(x=2 * x, y=y)
        taskuri.nr_taskuri += 1
        taskuri.obiecte.append(self)

    @classmethod
    def creaza_task(cls, root: object, entry, button):

        pozx, pozy = 20, 40
        if taskuri.nr_taskuri == 0:
            t1 = taskuri(root.frame, entry, x=pozx, y=pozy)
            root.tasks.append(t1)
        elif taskuri.nr_taskuri == 1:
            pozy = pozy + 20
            t2 = taskuri(root.frame, entry, x=pozx, y=pozy)
            root.tasks.append(t2)
        elif taskuri.nr_taskuri == 2:
            pozy = pozy + 40
            t3 = taskuri(root.frame, entry, x=pozx, y=pozy)
            root.tasks.append(t3)
        elif taskuri.nr_taskuri == 3:
            pozy = pozy + 60
            t4 = taskuri(root.frame, entry, x=pozx, y=pozy)
            root.tasks.append(t4)
        elif taskuri.nr_taskuri == 4:
            pozy = pozy + 80
            t5 = taskuri(root.frame, entry, x=pozx, y=pozy)
            root.tasks.append(t5)

            print("Ai atins limita maxima de task-uri!!")
            button.configure(state=DISABLED)
