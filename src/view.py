import tkinter as tk
from tkinter import ttk


class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Session and To-Do List")

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.gym_sessions_label = ttk.Label(self.main_frame, text="Gym Sessions:")
        self.gym_sessions_label.grid(row=0, column=0, sticky=tk.W)

        self.gym_sessions_listbox = tk.Listbox(self.main_frame, height=6)
        self.gym_sessions_listbox.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.tasks_label = ttk.Label(self.main_frame, text="To-Do List:")
        self.tasks_label.grid(row=2, column=0, sticky=tk.W)

        self.tasks_listbox = tk.Listbox(self.main_frame, height=6)
        self.tasks_listbox.grid(row=3, column=0, sticky=(tk.W, tk.E))

    def display_gym_sessions(self, gym_sessions):
        self.gym_sessions_listbox.delete(0, tk.END)
        for session in gym_sessions:
            self.gym_sessions_listbox.insert(tk.END, session)

    def display_tasks(self, tasks):
        self.tasks_listbox.delete(0, tk.END)
        for task in tasks:
            self.tasks_listbox.insert(tk.END, task)
