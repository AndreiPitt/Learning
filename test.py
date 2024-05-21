
import tkinter as tk
import datetime

def get_day_of_year():
    azi = datetime.date.today()
    ziua_curenta = azi.timetuple().tm_yday
    year = azi.year
    zile_din_an = 366 if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else 365
    tuplu = (ziua_curenta, zile_din_an)
    return tuplu

def update_progress_bar(canvas, progress_bar, x1, y1, x2, y2, progress):
    # Calculează lățimea nouă bazată pe procentul de progres
    new_width = x1 + (x2 - x1) * progress / 100
    # Actualizează coordonatele dreptunghiului de progres
    canvas.coords(progress_bar, x1, y1, new_width, y2)

# Creează fereastra principală
root = tk.Tk()
root.title("Progress of the Year")
root.geometry("400x300")

# Creează un canvas
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Coordonate pentru progress bar
x1, y1, x2, y2 = 35.73651123046875, 158.78286743164062, 193.95391845703125, 185.20130729675293

# Creează conturul progress bar-ului
canvas.create_rectangle(x1, y1, x2, y2, outline="#D9D9D9")

# Creează progress bar-ul inițial (0% progres)
progress_bar = canvas.create_rectangle(x1, y1, x1, y2, fill="#1E1E1E", outline="")

# Obține ziua curentă și numărul total de zile din an
ziua_curenta, zile_din_an = get_day_of_year()

# Calculează progresul ca procent
progres = (ziua_curenta / zile_din_an) * 100

# Actualizează progress bar-ul cu progresul calculat
update_progress_bar(canvas, progress_bar, x1, y1, x2, y2, progres)

# Afișează procentul de progres
progres_label = tk.Label(root, text=f"Progresul zilei din an: {progres:.2f}%")
progres_label.pack(pady=20)

root.mainloop()
