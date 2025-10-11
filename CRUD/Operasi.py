import time
from . import Database
from .Util import str_random

def create_first_data():
    judul = input("JUDUL \t: ")
    penulis = input("PENULIS\t: ")
    while(True):
        try:
            tahun = int(input("TAHUN\t: "))

            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun tidak sesuai, silahkan masukkan tahun lagi")
        except:
            print("Tahun harus berupa angka, silahkan masukkan tahun lagi")


    data = Database.TEMPLATE.copy()

    data["pk"] = str_random(6)
    data["date_add"] = time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    isi_data = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

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
    
def create(judul, penulis, tahun):
    # try:
        data = Database.TEMPLATE.copy()

        data["pk"] = str_random(6)
        data["date_add"] = time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())
        data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
        data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
        data["tahun"] = str(tahun)

        isi_data = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

        try:
            with open(Database.DB_NAME, "a", encoding="utf-8") as file:
                file.write(isi_data)
        except:
            print("data gagal tersimpan")