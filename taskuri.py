from tkinter import *
from db import *


class taskuri:
    obiecte = lista_taskuri
    nr_taskuri = 0
    obiecte_cod = []

    def __init__(self, root, entry, x, y):
        self.checkbutton = Checkbutton(root, bg="#D9D9D9")
        self.label = Label(root, bg="#D9D9D9", text=entry)
        self.description = ""
        self.checkbutton.place(x=x, y=y)
        self.label.place(x=30 + x, y=y)
        taskuri.nr_taskuri += 1
        taskuri.obiecte_cod.append(self)

    @classmethod
    def creaza_task(cls, root: object, entry, button):
        nr = len(root.tasks)
        if nr == 0:

            t1 = taskuri(root.frame, entry, x=20, y=40)
            root.tasks.append(t1)
            adauga_in_db(frame_id=root.id, object_name=entry, description="")
            taskuri.nr_taskuri += 1

        elif nr == 1:

            t2 = taskuri(root.frame, entry, x=20, y=80)
            root.tasks.append(t2)
            adauga_in_db(frame_id=root.id, object_name=entry, description="")
            taskuri.nr_taskuri += 1

        elif nr == 2:

            t3 = taskuri(root.frame, entry, x=20, y=120)
            root.tasks.append(t3)
            adauga_in_db(frame_id=root.id, object_name=entry, description="")
            taskuri.nr_taskuri += 1

        elif nr == 3:

            t4 = taskuri(root.frame, entry, x=250, y=40)
            root.tasks.append(t4)
            adauga_in_db(frame_id=root.id, object_name=entry, description="")
            taskuri.nr_taskuri += 1

        elif nr == 4:

            t5 = taskuri(root.frame, entry, x=250, y=80)
            root.tasks.append(t5)
            adauga_in_db(frame_id=root.id, object_name=entry, description="")
            taskuri.nr_taskuri += 1

        elif nr == 5:
            t6 = taskuri(root.frame, entry, x=250, y=120)
            root.tasks.append(t6)
            adauga_in_db(frame_id=root.id, object_name=entry, description="")
            taskuri.nr_taskuri += 1

            print("Ai atins limita maxima de task-uri!!")
            button.configure(state=DISABLED)

    @classmethod
    def ia_din_db(cls, root, command):
        nr_tasks = len(root.tasks)
        tasks = root.tasks

        if nr_tasks == 1:
            t1 = taskuri(root.frame, tasks[0][2], x=20, y=40)
            return t1

        elif nr_tasks == 2:
            t1 = taskuri(root.frame, tasks[0][2], x=20, y=40)
            t2 = taskuri(root.frame, tasks[1][2], x=20, y=80)
            return [t1, t2]

        elif nr_tasks == 3:
            t1 = taskuri(root.frame, tasks[0][2], x=20, y=40)
            t2 = taskuri(root.frame, tasks[1][2], x=20, y=80)
            t3 = taskuri(root.frame, tasks[2][2], x=20, y=120)
            return [t1, t2, t3]

        elif nr_tasks == 4:
            t1 = taskuri(root.frame, tasks[0][2], x=20, y=40)
            t2 = taskuri(root.frame, tasks[1][2], x=20, y=80)
            t3 = taskuri(root.frame, tasks[2][2], x=20, y=120)
            t4 = taskuri(root.frame, tasks[3][2], x=250, y=40)
            return [t1, t2, t3, t4]

        elif nr_tasks == 5:
            t1 = taskuri(root.frame, tasks[0][2], x=20, y=40)
            t2 = taskuri(root.frame, tasks[1][2], x=20, y=80)
            t3 = taskuri(root.frame, tasks[2][2], x=20, y=120)
            t4 = taskuri(root.frame, tasks[3][2], x=250, y=40)
            t5 = taskuri(root.frame, tasks[4][2], x=250, y=80)
            return [t1, t2, t3, t4, t5]

        elif nr_tasks == 6:
            t1 = taskuri(root.frame, tasks[0][2], x=20, y=40)
            t2 = taskuri(root.frame, tasks[1][2], x=20, y=80)
            t3 = taskuri(root.frame, tasks[2][2], x=20, y=120)
            t4 = taskuri(root.frame, tasks[3][2], x=250, y=40)
            t5 = taskuri(root.frame, tasks[4][2], x=250, y=80)
            t6 = taskuri(root.frame, tasks[5][2], x=250, y=120)
            command.configure(state=DISABLED)
            print("Ai maximul de task-uri disponibile")
            return [t1, t2, t3, t4, t5, t6]

    @classmethod
    def cleartasks(cls, root):
        root.tasks.clear()
