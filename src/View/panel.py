import tkinter as tk
import ttkbootstrap as ttk


class Panel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # App title
        name_of_app = ttk.Label(self,
                                text="  Creation🏋️",
                                bootstyle="info",
                                font=('Perpetua', 33),
                                anchor=tk.CENTER)

        name_of_app.pack(fill="x", pady=10)

        button1 = ttk.Button(self, text="Dashboard", width=30)
        button2 = ttk.Button(self, text="Tasks", width=30)
        button3 = ttk.Button(self, text="Workouts", width=30)

        button4 = ttk.Button(self, text="Profile", width=30)
        button5 = ttk.Button(self, text="Settings", width=30)

        mode_label = ttk.Label(self, text="Apparence Mode")
        mode = ttk.Menubutton(bootstyle="primary", text="Light")

        button1.pack(pady=10, ipady=10)
        button2.pack(pady=10, ipady=10)
        button3.pack(pady=10, ipady=10)

        button4.place(x=20, y=600, width=250, height=40)
        button5.place(x=20, y=650, width=250, height=40)
        mode_label.place(x=70, y=710, width=250, height=25)
        mode.place(x=20, y=740, width=250, height=40)
