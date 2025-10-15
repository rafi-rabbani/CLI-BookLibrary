from . import Operasi

DB_NAME = "library.txt"

#* panjang setiap kolom
PK_LEN = 6
DATE_LEN = 30
JUDUL_LEN = 255
PENULIS_LEN = 255
TAHUN_LEN = 4

TEMPLATE = {
    "pk"        : PK_LEN        * " ",
    "date_add"  : DATE_LEN      * " ",
    "judul"     : JUDUL_LEN     * " ",
    "penulis"   : PENULIS_LEN   * " ",
    "tahun"     : TAHUN_LEN     * " "
}

def init_terminal():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init selesai!!")
    except:
        print("Database tidak ditemukan, membuat Database baru")
        Operasi.create_first_data()
