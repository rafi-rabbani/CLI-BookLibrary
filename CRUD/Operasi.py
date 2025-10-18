import time
from . import Database
from .Util import str_random

def ambil_database():
    """membaca database dan memasukkannya kedalam dict in list"""
    try:
        # membaca file txt (r)
        with open(Database.DB_NAME, "r") as file:
            # membuat loop untuk mengambil setiap baris di file txt
            for line in file:
                # membuat list in list untuk setiap baris file dan menghapus karakter kosong (" ", "\n")
                data_break = line.strip().split(",")

                # membuat dict dari detail buku yang sudah di pecah di dalam list
                buku = {
                        "pk"        : data_break[0],
                        "date_add"  : data_break[1],
                        "judul"     : data_break[2],
                        "penulis"   : data_break[3],
                        "tahun"     : data_break[4]
                        }

                # memasukkan dict ke dalam list
                Database.DB_LIST.append(buku)

    except:
        print("database gagal diambil")

def format_data(data):
    """memformat database sebelum masuk ke file txt"""
    return (
            f"{data["pk"]       :<{Database.TEMPLATE_LEN["pk"]}},"
            f"{data["date_add"] :<{Database.TEMPLATE_LEN["date_add"]}},"
            f"{data["judul"]    :<{Database.TEMPLATE_LEN["judul"]}},"
            f"{data["penulis"]  :<{Database.TEMPLATE_LEN["penulis"]}},"
            f"{data["tahun"]    :<{Database.TEMPLATE_LEN["tahun"]}}\n"
            )

def create_first_data():
    """membuat data pertama, jika file belum ada"""
    # mengambil input judul
    judul = input("JUDUL \t: ")
    # mengambil input penulis
    penulis = input("PENULIS\t: ")
    # validasi input tahun
    while(True):
        try:
            # mengambil input tahun
            tahun = input("TAHUN\t: ")
            # validasi input tahun
            if len(tahun) == 4:
                break
            else:
                print("Tahun tidak sesuai, silahkan masukkan tahun lagi")
        except:
            print("Tahun harus berupa angka, silahkan masukkan tahun lagi")

    # mengubah data buku jadi dict
    data = {
    "pk"        : (str_random(Database.PK_LEN)),
    "date_add"  : (time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())),
    "judul"     : judul,
    "penulis"   : penulis,
    "tahun"     : tahun
    }

    # memasukkan dict data buku ke list utama
    Database.DB_LIST.append(data)

def read(**kwargs):
    data_buku = Database.DB_LIST
    jumlah_buku = len(Database.DB_LIST)

    if "no_buku" in kwargs:
        index_buku = kwargs["no_buku"]-1
        if index_buku < 0 or index_buku >= jumlah_buku: # kondisi salah
            print("nomor buku tidak sesuai")
            return False
        else:
            return data_buku[index_buku]
    else: 
        return data_buku
    
    # try:
    #     with open(Database.DB_NAME, "r") as file:
    #         isi = file.readlines() # membuat list dari database per baris
    #         jumlah_buku = len(isi) # menghitung jumlah data di list

    # except:
    #     print("database gagal dibaca")
    #     return False
    
def create(judul, penulis, tahun):
    # mengubah data buku jadi dict
    data = {
    "pk"        : (str_random(Database.PK_LEN)),
    "date_add"  : (time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())),
    "judul"     : judul,
    "penulis"   : penulis,
    "tahun"     : tahun
    }

    # memasukkan dict data buku ke list utama
    Database.DB_LIST.append(data)

    # data = Database.TEMPLATE.copy()

    # data["pk"] = str_random(Database.PK_LEN)
    # data["date_add"] = time.strftime("%d-%m-%Y %H:%M (GMT%z)", time.gmtime())
    # data["judul"] = judul
    # data["penulis"] = penulis
    # data["tahun"] = str(tahun)

    # isi_data = format_data(data)

    # try:
    #     with open(Database.DB_NAME, "a", encoding="utf-8") as file:
    #         file.write(isi_data)
    # except:
    #     print("data gagal tersimpan")

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