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

    isi_data = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(isi_data)
    except:
        print("data pertama gagal dibuat")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            isi = file.readlines() # membuat list dari database
            jumlah_buku = len(isi) # menghitung jumlah data di list

            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku >= jumlah_buku: # kondisi salah
                    print("nomor buku tidak sesuai")
                    return False
                else:
                    return isi[index_buku]
            else: 
                return isi
    except:
        print("database gagal dibaca")
        return False
    
def create(judul, penulis, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = str_random(6)
    data["date_add"] = time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    isi_data = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(isi_data)
    except:
        print("data gagal tersimpan")

def update(pk, date_add, no_buku, judul, penulis, tahun):

    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    isi_data = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    panjang_data = len(isi_data)

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(isi_data)
            file.flush()
    except:
        print("perubahan gagal tersimpan")