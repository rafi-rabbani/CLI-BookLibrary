from . import Operasi

def read_terminal():
    # mengambil list database
    data = Operasi.read()

    # persiapan penulisan tabel
    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    tahun = "TAHUN"

    #* header
    print(f"\n{'='*133}")

    # header tabel
    print(f"|{index:^4}|{judul:^58}|{penulis:^59}|{tahun:^7}|")
    print("-"*133)

    # mengulang untuk setiap buku
    for index,data_buku in enumerate(data):
        # mengambil detail tiap data buku
        pk = data_buku["pk"]
        date_add = data_buku["date_add"]
        judul = data_buku["judul"]
        penulis = data_buku["penulis"]
        tahun = data_buku["tahun"]
        # mengeluarkan detail buku di dalam tabel
        print(f"|{(str(index+1)) + '.':^4}| {judul:57}| {penulis:58}| {tahun:^4}  |")

    #* footer
    print(f"{'='*133}\n")

def create_terminal():
    #* header
    print(f"\n{'='*133}")
    
    # mengambil data buku dari user
    print(F"{'SILAHKAN MASUKKAN DATA BUKU BARU':^133}")
    print(f"{'='*133}")
    # mengambil input judul
    judul = input("JUDUL\t: ")
    # mengambil input penulis
    penulis = input("PENULIS\t: ")
    # perulangan validasi input tahun
    while(True):
        try:
            # mengambil input tahun
            tahun = int(input("TAHUN\t: "))
            # validasi input
            if len(str(tahun)) == 4:
                break
            # jika tahun tidak sesuai
            else:
                print("Tahun tidak sesuai, silahkan masukkan tahun lagi")
        # jika tahun bukan berupa angka
        except:
            print("Tahun harus berupa angka, silahkan masukkan tahun lagi")

    #* footer
    print(f"{'='*133}\n")

    # memanggil operasi create dan memberikan input user berupa (judul, penulis, tahun)
    Operasi.create(judul, penulis, tahun)
    print(f"{'BUKU TERSIMPAN':^133}")
    # menampilkan database buku yang sudah tersimpan
    read_terminal()

def update_terminal():
    # menampilkan list buku yang ada
    read_terminal()

    #* header
    print(f"\n{'='*133}")

    # validasi apakah data buku yg di masukkan ada di dalam list
    while(True):
        # meminta input nomor buku
        no_buku = int(input("Silahkan pilih nomor buku yang akan diubah\nNOMOR BUKU\t: "))
        # mengambil data buku dari (read funtion) berdasarkan No. buku
        data_buku = Operasi.read(no_buku = no_buku)
        # jika data buku ada di dalam list, perulangan berhent
        if data_buku:
            break
        else:
            print("buku yang di pilih tidak valid\n")

    # mengambil data tiap komponen
    pk = data_buku["pk"]
    date_add = data_buku["date_add"]
    judul = data_buku["judul"]
    penulis = data_buku["penulis"]
    tahun = data_buku["tahun"]

    # melakukan perulangan hingga user berhenti mengedit
    while(True):
        # mengambil input komponen yg ingin di ubah
        option = int(input(
            "\nSilahkan pilih komponen yang ingin anda ubah" +
            f"\n1. Judul\t:{judul}" +
            f"\n2. Penulis\t:{penulis}" +
            f"\n3. Tahun\t:{tahun}" +
            "\nNomor komponen : "))
        
        # memilih komponen untuk diubah
        match (option):
            # mengambil input judul
            case 1 : judul = input("\njudul\t: ")
            # mengambil input penulis
            case 2 : penulis = input("\npenulis\t: ")
            case 3 :
                # melakukan validasi untuk input tahun
                while(True):
                    # validasi tipe data tahun
                    try:
                        # mengambil input tahun
                        tahun = int(input("\ntahun\t: "))
                        # jika tahun sesuai, maka looping berhenti
                        if (len(str(tahun)) == 4):
                            break
                        else:
                            print("tahun tidak valid")
                    # keluar jika tahun bukan int
                    except:
                        print("tahun harus berupa angka")
            # validasi jika komponen yg dipilih tidak ada
            case _ :
                print("nomor komponen tidak valid")
        
        #* footer
        print(f"{'='*133}\n")

        # menanyakan apakah user ingin terus mengedit komponen
        lanjut = input("lanjutkan mengubah komponen? (y/n) : ")
        # jika tidak, maka loop berhenti
        if lanjut.lower() == "n":
            break

    # memanggil update funtion dari operasi
    Operasi.update(pk, date_add, no_buku, judul, penulis, tahun)