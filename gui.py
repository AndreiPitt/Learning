from pathlib import Path

from tkinter import *
from orasidata import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\zona de lucru\myapp\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def schimba_in_float():
    a = int(detaliidatatimp()[2]) / 23
    a = a * 100
    b = int(detaliidatatimp()[3]) / 7
    b = b * 100
    c = int(get_day_of_year()[0]) / float(get_day_of_year()[1])
    c = c * 100
    tuplu = (a, b, c)
    return tuplu


def update_custom_progress_bar(progress_bar, x1, y1, x2, y2, progress):
    # Calculează lățimea barei de progres bazată pe progresul curent
    new_width = x1 + (x2 - x1) * progress / 100
    # Actualizează bara de progres
    canvas.coords(progress_bar, x1, y1, new_width, y2)


def update_ceas():
    x = detaliidatatimp()[4]
    canvas.itemconfig(ceas, text=x)
    canvas.after(1000, update_ceas)


def update_temperatura():

    temperatura = returneaza_temperatura()
    canvas.itemconfig(grade, text=temperatura)


def tip_vreme():
    timp = detaliidatatimp()[2]
    vreme = returneaza_descriere_vremea()
    tip = {"Clear": 1, "Clouds": 2, "Rain": 3, "Thunderstorm": 3}

    # De la 6 dimineata pana la ora 22
    if timp in range(6, 23) and tip[vreme] == 1:
        canvas.itemconfig(image_6, image=iconvreme1)
    # De la ora 23 pana la 6 dimineata
    if (timp == 23 or timp in range(0, 6)) and tip[vreme] == 1:
        canvas.itemconfig(image_6, image=iconvreme2)
    if tip[vreme] == 2:
        canvas.itemconfig(image_6, image=iconvreme4)
    if tip[vreme] == 3:
        canvas.itemconfig(image_6, image=iconvreme3)


window = Tk()

window.geometry("900x700")
window.configure(bg="#9D9D9D")

canvas = Canvas(
    window,
    bg="#9D9D9D",
    height=700,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

zi = detalii_zile()

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    33.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    44.01031494140625,
    34.23529052734375,
    image=image_image_2
)

canvas.create_text(
    84.85714721679688,
    14.0,
    anchor="nw",
    text="GYM ",
    fill="#000000",
    font=("Rowdies Regular", 36 * -1)
)

# Progress bar
canvas.create_rectangle(
    35.73651123046875,
    158.78286743164062,
    193.95391845703125,
    185.20130729675293,
    fill="",
    outline="#D9D9D9")

progress1 = canvas.create_rectangle(
    35.73651123046875,
    158.78286743164062,
    193.95391845703125,
    185.20130729675293,
    fill="#1E1E1E",
    outline="")
update_custom_progress_bar(progress1, 35.73651123046875, 158.78286743164062, 193.95391845703125, 185.20130729675293,
                           schimba_in_float()[1])
canvas.create_rectangle(
    35.555572509765625,
    124.0,
    193.77297973632812,
    150.4184398651123,
    fill="",
    outline="#D9D9D9")
progress2 = canvas.create_rectangle(
    35.555572509765625,
    124.0,
    193.77297973632812,
    150.4184398651123,
    fill="#1E1E1E",
    outline="")
update_custom_progress_bar(progress2, 35.555572509765625, 124.0, 193.77297973632812, 150.4184398651123,
                           schimba_in_float()[2])

canvas.create_rectangle(
    35.73651123046875,
    194.3063201904297,
    193.95391845703125,
    220.724760055542,
    fill="",
    outline="#D9D9D9")
progress3 = canvas.create_rectangle(
    35.73651123046875,
    194.3063201904297,
    193.95391845703125,
    220.724760055542,
    fill="#1E1E1E",
    outline="")
update_custom_progress_bar(progress3, 35.73651123046875, 194.3063201904297, 193.95391845703125, 220.724760055542,
                           schimba_in_float()[0])

canvas.create_text(
    213.29824829101562,
    199.0,
    anchor="nw",
    text=f"Day: {detaliidatatimp()[2]}/23",
    fill="#FFFFFF",
    font=("Rowdies Regular", 13 * -1)
)

canvas.create_text(
    213.29824829101562,
    163.0,
    anchor="nw",
    text=f"Week: {detaliidatatimp()[3]}/7",
    fill="#FFFFFF",
    font=("Rowdies Regular", 13 * -1)
)

canvas.create_text(
    213.29824829101562,
    128.0,
    anchor="nw",
    text=f"Year: {get_day_of_year()[0]}/{get_day_of_year()[1]}",
    fill="#FFFFFF",
    font=("Rowdies Regular", 13 * -1)
)

ceas = canvas.create_text(
    351.0,
    128.0,
    anchor="nw",
    text="12:25:11",
    fill="#FFFFFF",
    font=("RUSerius Regular", 64 * -1)
)
update_ceas()

canvas.create_text(
    430.0,
    191.1376190185547,
    anchor="nw",
    text=detaliidatatimp()[1],
    fill="#FFFFFF",
    font=("RozhaOne Regular", 20 * -1)
)

grade = canvas.create_text(
    739.0,
    150.0,
    anchor="nw",
    text="25",
    fill="#FFFFFF",
    font=("Rowdies Regular", 36 * -1)
)

update_temperatura()

iconvreme1 = PhotoImage(
    file=relative_to_assets("sun.png"))
iconvreme2 = PhotoImage(
    file=relative_to_assets("moon.png"))
iconvreme3 = PhotoImage(
    file=relative_to_assets("rain.png"))
iconvreme4 = PhotoImage(
    file=relative_to_assets("fewclouds.png"))
image_6 = canvas.create_image(
    699.0,
    168.0,
    image=iconvreme1
)
tip_vreme()
image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    793.0,
    161.0,
    image=image_image_7
)

canvas.create_text(
    810.0,
    150.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Rowdies Regular", 36 * -1)
)

canvas.create_rectangle(
    15.0,
    521.0,
    885.0,
    684.0,
    fill="#918F8F",
    outline="")

canvas.create_rectangle(
    15.0,
    294.0,
    885.0,
    509.0,
    fill="#908F8F",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=841.0,
    y=363.0,
    width=36.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=25.0,
    y=363.0,
    width=36.0,
    height=80.0
)

canvas.create_rectangle(
    568.0,
    306.0,
    746.5763397216797,
    497.0,
    fill="#D9D9D9",
    outline="")

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    582.0,
    320.0,
    image=image_image_8
)

canvas.create_text(
    601.0,
    309.0,
    anchor="nw",
    text=zi[0],
    fill="#1E1E1E",
    font=("Rowdies Regular", 16 * -1)
)


image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    657.0,
    470.0,
    image=image_image_12
)

canvas.create_text(
    644.0,
    482.0,
    anchor="nw",
    text="50%",
    fill="#000000",
    font=("Rowdies Regular", 11 * -1)
)

canvas.create_rectangle(
    348.0,
    306.0,
    526.5763397216797,
    497.0,
    fill="#D9D9D9",
    outline="")

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    362.0,
    320.0,
    image=image_image_13
)

canvas.create_text(
    381.0,
    309.0,
    anchor="nw",
    text=zi[1],
    fill="#1E1E1E",
    font=("Rowdies Regular", 16 * -1)
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    437.0,
    470.0,
    image=image_image_17
)

canvas.create_text(
    424.0,
    482.0,
    anchor="nw",
    text="50%",
    fill="#000000",
    font=("Rowdies Regular", 11 * -1)
)

canvas.create_rectangle(
    128.0,
    306.0,
    306.5763397216797,
    497.0,
    fill="#D9D9D9",
    outline="")

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    142.0,
    320.0,
    image=image_image_18
)

canvas.create_text(
    161.0,
    309.0,
    anchor="nw",
    text=zi[2],
    fill="#1E1E1E",
    font=("Rowdies Regular", 16 * -1)
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    217.0,
    470.0,
    image=image_image_22
)

canvas.create_text(
    204.0,
    482.0,
    anchor="nw",
    text="50%",
    fill="#000000",
    font=("Rowdies Regular", 11 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=669.0,
    y=245.0,
    width=97.0,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=772.0,
    y=310.0,
    width=102.0,
    height=39.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=783.0,
    y=244.56097412109375,
    width=97.0,
    height=35.58536911010742
)
window.resizable(False, False)
window.mainloop()
