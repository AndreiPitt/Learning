import mysql.connector

try:
    CONNECTION = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="", database="gymdb")
    print("S-a facut conexiunea")

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

    # insert = "INSERT INTO `objects`(`object_id`, `frame_id`, `name`, `description`) VALUES ('7','1','obiect nou','')"
    # cursor.execute(insert)
    # CONNECTION.commit()

    # print(lista_frameuri)
    # print(lista_taskuri)


def id_max_task():
    cursor.execute(sel_tabel2)
    lista_actualizata = cursor.fetchall()
    # print(lista_actualizata)
    return max(lista_actualizata)[0]


def adauga_in_db(frame_id, object_name, description):
    id_task = id_max_task()
    id_task += 1
    insert = f"INSERT INTO `objects`(`object_id`, `frame_id`, `name`, `description`) " \
             f"VALUES ('{id_task}','{frame_id}','{object_name}','{description}')"
    cursor.execute(insert)
    CONNECTION.commit()


