import time
from . import Database
from .Util import str_random

def format_data(data):
    pk = str(data.get("pk", " ")).strip().ljust(Database.PK_LEN)
    date_add = str(data.get("date_add", " ")).strip().ljust(Database.DATE_LEN)
    judul = str(data.get("judul", " ")).strip().ljust(Database.JUDUL_LEN)
    penulis = str(data.get("penulis", " ")).strip().ljust(Database.PENULIS_LEN)
    tahun = str(data.get("tahun", " ")).strip().ljust(Database.TAHUN_LEN)

    data_terformat = f'{pk},{date_add},{judul},{penulis},{tahun}\n'

    return data_terformat

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

    data["pk"] = (str_random(Database.PK_LEN))
    data["date_add"] = (time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime()))
    data["judul"] = judul
    data["penulis"] = penulis
    data["tahun"] = str(tahun)

    isi_data = format_data(data)

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

    data["pk"] = str_random(Database.PK_LEN)
    data["date_add"] = time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())
    data["judul"] = judul
    data["penulis"] = penulis
    data["tahun"] = str(tahun)

    isi_data = format_data(data)

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(isi_data)
    except:
        print("data gagal tersimpan")

def update(pk, date_add, no_buku, judul, penulis, tahun):

    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["judul"] = judul
    data["penulis"] = penulis
    data["tahun"] = str(tahun)

    isi_data = format_data(data)

    panjang_data = len(format_data(Database.TEMPLATE))

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(isi_data)
            file.flush()
    except:
        print("perubahan gagal tersimpan")