import tkinter as tk
import ttkbootstrap as ttk

from src.View.panel import Panel
from src.View.window import Window


class View:
    """
    View in MVC pattern assumes role of rendering user interface to the user, and maintaining  an up-to-date View as
    it handles user interaction it receives from Controller.
    """

    def __init__(self):
        # Init main window
        self.root = ttk.Window()
        self.root.title("My app")
        self.root.geometry("1200x800")
        self.root.minsize(1200, 800)

        # Define a grid
        self.root.grid_columnconfigure(index=0, weight=1, uniform="a")
        self.root.grid_columnconfigure(index=1, weight=3, uniform="a")
        self.root.grid_rowconfigure(index=0, weight=1, uniform="a")

        # Layout
        self._create_panel()
        self._create_frontend()

    def _create_panel(self):
        # Create left side of the main window
        panel = Panel(self.root)
        panel.grid(row=0, column=0, sticky="nsew")

    def _create_frontend(self):
        frontend = Window(self.root)
        frontend.dashboard.pack(expand=True, fill="both")
        frontend.grid(row=0, column=1, sticky="nsew")

    def start(self):
        self.root.mainloop()
