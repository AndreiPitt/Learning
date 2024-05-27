from tkinter import *
from db import lista_frameuri


class frameuri:
    obiecte = lista_frameuri
    mid = {"x1": 348.0, "y1": 306.0, "x2": 526.5763397216797, "y2": 497.0}
    width = 398.6
    height = 191.0

    def __init__(self, root, sursa_imagine, text: str, idd: int):
        self.id = idd
        self.tasks = []
        self.frame = Frame(root, width=frameuri.width, height=frameuri.height, bg="#D9D9D9")
        self.canvas = Canvas(self.frame, width=frameuri.width, height=28, bg="#ffffff", highlightthickness=0, relief="ridge")
        self.canvas2 = Canvas(self.frame, width=frameuri.width, height=35, bg="#D9D9D9", highlightthickness=0, relief="ridge")

        self.imagine_canvas = self.canvas.create_image(
            16,
            15,
            image=sursa_imagine
        )
        self.text_canvas = self.canvas.create_text(
            150,
            7,
            anchor="nw",
            text=text,
            fill="#1E1E1E",
            font=("Rowdies Regular", 16 * -1),
        )

        self.progressbar = self.canvas2.create_rectangle(
            20,
            10,
            375,
            5,
            fill="#ffffff",
            outline=""
            )

        self.progress = self.canvas2.create_rectangle(
            20,
            10,
            177,
            5,
            fill="#00BFFF",
            outline="")

        self.text_progress = self.canvas2.create_text(
            175,
            14,
            anchor="nw",
            text="50%",
            fill="#000000",
            font=("Rowdies Regular", 16 * -1),
        )

        self.frame.place(x=frameuri.mid["x1"], y=frameuri.mid["y1"])
        self.canvas.place(x=0, y=0)
        self.canvas2.place(x=0, y=156)
