import tkinter as tk
import ttkbootstrap as ttk

bg_color = "#dbd5d5"


class Window(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.dashboard = ttk.Frame(self)
        self.taskboard = ttk.Frame(self)
        self.workout = ttk.Frame(self)

        self.label1 = ttk.Label(self.dashboard, text="Acesta este Tab 1", background=bg_color)
        self.label1.pack(fill="both", expand=True)

        self.label2 = ttk.Label(self.taskboard, text="Acesta este Tab 2", background=bg_color)
        self.label2.pack(fill="both", expand=True)

        self.label3 = ttk.Label(self.workout, text="Acesta este Tab 3", background=bg_color)
        self.label3.pack(fill="both", expand=True)
