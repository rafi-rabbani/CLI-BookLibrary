
#* ======================================================================#
#*                                                                       #
#* proyek  : perpustakaan digital                                        #
#* tanggal : 21-09-2025                                                  #
#*                                                                       #
#* ======================================================================#

import os
import CRUD as CRUD

if __name__ == "__main__":
    # membersihkan terminal sebelumnya
    match os.name:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    # header
    print(f"{'='*133}\n        {'  SELAMAT DATANG DI PERPUSTAKAAN  ':-^117}        \n      {'        by Tora Santaroo        ':-^121}      \n{'='*133}")

    # mengecek apakah file database ada
    CRUD.init_terminal()

    # melakukan perulangan hingga user berhenti mengoperasikan program
    while(True):
        # menghapus terminal sebelumnya
        match os.name:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        # header
        print(f"{'='*133}\n        {'  SELAMAT DATANG DI PERPUSTAKAAN  ':-^117}        \n      {'        by Tora Santaroo        ':-^121}      \n{'='*133}")
        # mengambil input CRUD
        input_user = input("\n1. Lihat koleksi\n2. Tambah koleksi\n3. Ubah koleksi\n4. Hapus koleksi\n\nSilahkan pilih nomor opsi (1-4) : ")
        # memilih input user
        match input_user:
            case "1": CRUD.read_terminal()
            case "2": CRUD.create_terminal()
            case "3": CRUD.update_terminal()
            case "4": CRUD.delete_terminal()
            case _: print("input tidak sesuai")

        # menanyakan apakah user akan melanjutkan program
        lanjut = input("lanjutkan program (y/n) : ")
        # jika tidak maka loop berhenti
        if lanjut.lower() == "n":
            # memanggil fungsi save untuk menyimpan data ke dalam file txt
            CRUD.save_database()
            break
    # footer
    print(f"\n{'PROGRAM PERPUSTAKAAN DIGITAL TELAH BERAKHIR!!':-^133}\n")