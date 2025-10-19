import time
from . import Database
from .Util import str_random

def format_data(data):
    """memformat database sebelum masuk ke file txt"""
    return (
            f"{data["pk"]       :<{Database.TEMPLATE_LEN["pk"]}},"
            f"{data["date_add"] :<{Database.TEMPLATE_LEN["date_add"]}},"
            f"{data["judul"]    :<{Database.TEMPLATE_LEN["judul"]}},"
            f"{data["penulis"]  :<{Database.TEMPLATE_LEN["penulis"]}},"
            f"{data["tahun"]    :<{Database.TEMPLATE_LEN["tahun"]}}\n"
            )

def load_database():
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
    # mengambil list database buku
    data_buku = Database.DB_LIST
    # menghitung jumlah data buku
    jumlah_buku = len(Database.DB_LIST)

    # mengambil data buku berdasarkan no buku
    if "no_buku" in kwargs:
        # menghitung index buku berdasarkan no buku
        index_buku = kwargs["no_buku"]-1
        # jika no buku tidak ada
        if index_buku < 0 or index_buku >= jumlah_buku:
            print("nomor buku tidak sesuai")
            return False
        # jika no buku tersedia
        else:
            return data_buku[index_buku]
    # jika tidak mengambil data buku berdasarkan no buku
    else: 
        return data_buku
    
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

def update(pk, date_add, no_buku, judul, penulis, tahun):
    # mengubah data buku jadi dict
    data = {
    "pk"        : pk,
    "date_add"  : date_add,
    "judul"     : judul,
    "penulis"   : penulis,
    "tahun"     : tahun
    }
    # mengambil index buku berdasarkan no buk
    index_buku = no_buku-1
    # mengubah list data buku sesuai index
    Database.DB_LIST[index_buku] = data

def delete(no_buku):
    try:
        # menghitung index buku
        index_buku = no_buku - 1
        # menghapus data buku berdasarkan indexnya di list database
        Database.DB_LIST.pop(index_buku)
    except:
        print("buku gagal di hapus")
        

def save_database():
    """menyimpan list data utama yg telah terformat kedalam file txt"""
    try:
        # membuka dalam mode (w) (menulis ulang semua)
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            # mengulang untuk seluruh isi list
            for buku in Database.DB_LIST:
                # memformat tiap data dengan padding
                data_terformat = format_data(buku)
                # menulisnya di file txt
                file.write(data_terformat)
    except:
        # keluar jika data gagal tersimpan di file txt
        print("data gagal tersimpan")