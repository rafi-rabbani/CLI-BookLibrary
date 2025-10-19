from . import Operasi

# nama file txt
DB_NAME = "library.txt"
# membuat list utama untuk penyimpanan sebelum masuk ke file txt
DB_LIST = []
# panjang pk
PK_LEN = 6
# template untuk format data di dalam file txt
TEMPLATE_LEN = {
    "pk"        : PK_LEN,
    "date_add"  : 30,
    "judul"     : 225,
    "penulis"   : 225,
    "tahun"     : 4
}

def init_terminal():
    """mengecek apakah database (file txt) ada atau tidak, jika tidak maka akan membuat file txt baru"""
    try:
        # membuka dalam mode (read)
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init selesai!!")
            # memanggil load database
            Operasi.load_database()
    # jika file txt tidak ada
    except:
        print("Database tidak ditemukan, membuat Database baru")
        # memanggil fungsi create data pertama
        Operasi.create_first_data()
