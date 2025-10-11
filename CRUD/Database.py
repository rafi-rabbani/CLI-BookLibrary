from . import Operasi

DB_NAME = "data.txt"

TEMPLATE = {
    "pk" : "xxxxxx",
    "date_add" : "yyyy-mm-dd",
    "penulis" : 255 * " ",
    "judul" : 255 * " ",
    "tahun" : "yyyy"
}

def init_terminal():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init selesai!!")
    except:
        print("Database tidak ditemukan, membuat Database baru")
        Operasi.create_first_data()
