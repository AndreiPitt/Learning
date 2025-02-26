import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="")
        self.label.pack()
        self.button = tk.Button(self, text="Click me", command=self.on_button_click)
        self.button.pack()

    def set_label_text(self, text):
        self.label.config(text=text)

    def on_button_click(self):
        pass  # Acesta va fi suprascris de către Presenter
