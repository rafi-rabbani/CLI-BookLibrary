import time
from . import Database
from .Util import str_random

def create_first_data():
    penulis = input("Penulis\t: ")
    judul = input("Judul \t: ")
    tahun = input("Tahun \t: ")

    data = Database.TEMPLATE.copy()

    data["pk"] = str_random(6)
    data["date_add"] = time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    isi_data = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}'

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(isi_data)
    except:
        print("data pertama gagal dibuat")

def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            isi = file.readlines()
            return isi
    except:
        print("database gagal dibaca")
        return False