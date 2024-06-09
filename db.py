import mysql.connector
from datetime import datetime, timedelta


def generate_dates_for_current_year():
    current_year = datetime.now().year
    start_date = datetime(current_year, 1, 1)
    end_date = datetime(current_year, 12, 31)
    delta = end_date - start_date
    listaaaaa = [start_date + timedelta(days=i) for i in range(delta.days + 1)]
    return listaaaaa


def date_exists(data):
    cursor.execute("SELECT 1 FROM frames WHERE date = %s", (data,))
    return cursor.fetchone() is not None


def id_max_task():
    cursor.execute(sel_tabel2)
    lista_actualizata = cursor.fetchall()
    if len(lista_actualizata) == 0:
        print("Lista de taskuri este inital goala !!!!!")
        print("Primul task a fost creat!")
        return 0
    else:
        # print(lista_actualizata)
        return max(lista_actualizata)[0]


def adauga_in_db(frame_id, object_name, description):
    id_task = id_max_task()
    id_task += 1
    insert = f"INSERT INTO `objects`(`object_id`, `frame_id`, `name`, `description`) " \
             f"VALUES ('{id_task}','{frame_id}','{object_name}','{description}')"
    cursor.execute(insert)
    CONNECTION.commit()


try:
    CONNECTION = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="", database="gymdb")
    # print("S-a facut conexiunea")

except Exception as e:
    print("Nu s-a facut conexiunea la baza de date!", e)


else:
    cursor = CONNECTION.cursor()

    sel_tabel = "SELECT * FROM frames"
    sel_tabel2 = "SELECT * FROM objects"
    cursor.execute(sel_tabel)
    lista_frameuri = cursor.fetchall()
    cursor.execute(sel_tabel2)
    lista_taskuri = cursor.fetchall()

    dates = generate_dates_for_current_year()

    # Inserarea datelor în tabela `frames` dacă nu există deja
    insert_query = "INSERT INTO frames (date) VALUES (%s)"
    for date in dates:
        date_str = date.strftime('%Y-%m-%d')
        if not date_exists(date_str):
            try:
                cursor.execute(insert_query, (date_str,))
                # print(f"Data {date_str} a fost inserată în tabel.")
            except mysql.connector.Error as err:
                print(f"Eroare la inserarea datei {date_str}: {err}")

    # Confirmarea inserării
    try:
        CONNECTION.commit()
        # print("Toate modificările au fost confirmate.")
    except mysql.connector.Error as err:
        print(f"Eroare la confirmarea modificărilor: {err}")
