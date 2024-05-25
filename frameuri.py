from tkinter import *


class frameuri:
    obiecte = []
    dr = {"x1": 568.0, "y1": 306.0, "x2": 746.5763397216797, "y2": 497.0}
    mid = {"x1": 348.0, "y1": 306.0, "x2": 526.5763397216797, "y2": 497.0}
    st = {"x1": 128.0, "y1": 306.0, "x2": 306.5763397216797, "y2": 497.0}
    width = 178.5763397216797
    height = 191.0

    def __init__(self, root, flag: str, sursa_imagine, text: str):
        self.tasks = []
        self.frame = Frame(root, width=frameuri.width, height=frameuri.height, bg="#D9D9D9")
        self.canvas = Canvas(self.frame, width=frameuri.width, height=28, bg="#ffffff", highlightthickness=0, relief="ridge")
        self.imagine_canvas = self.canvas.create_image(
            16,
            15,
            image=sursa_imagine
        )
        self.text_canvas = self.canvas.create_text(
            40,
            7,
            anchor="nw",
            text=text,
            fill="#1E1E1E",
            font=("Rowdies Regular", 16 * -1),
        )
        if flag == "dr":
            self.frame.place(x=frameuri.dr["x1"], y=frameuri.dr["y1"])
            self.canvas.place(x=0, y=0)
        elif flag == "mid":
            self.frame.place(x=frameuri.mid["x1"], y=frameuri.mid["y1"])
            self.canvas.place(x=0, y=0)
        elif flag == "st":
            self.frame.place(x=frameuri.st["x1"], y=frameuri.st["y1"])
            self.canvas.place(x=0, y=0)
        else:
            print("EROARE: Nu ai pus un flag valid (dr,mid,st)!")
            print("Frame ul nu a fost afisat!")
        frameuri.obiecte.append(self)
