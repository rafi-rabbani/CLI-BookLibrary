from . import Operasi

DB_NAME = "library.txt"
DB_LIST = []

PK_LEN = 6

TEMPLATE_LEN = {
    "pk"        : PK_LEN,
    "date_add"  : 30,
    "judul"     : 225,
    "penulis"   : 225,
    "tahun"     : 4
}

def init_terminal():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init selesai!!")
    except:
        print("Database tidak ditemukan, membuat Database baru")
        Operasi.create_first_data()
