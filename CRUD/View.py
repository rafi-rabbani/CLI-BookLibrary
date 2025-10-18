from . import Operasi

def read_terminal():
    data = Operasi.read()

    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    tahun = "TAHUN"

    #* header
    print(f"\n{'='*133}")

    print(f"|{index:^4}|{judul:^58}|{penulis:^59}|{tahun:^7}|")
    print("-"*133)

    #* data
    for index,data_buku in enumerate(data):

        pk = data_buku["pk"]
        date_add = data_buku["date_add"]
        judul = data_buku["judul"]
        penulis = data_buku["penulis"]
        tahun = data_buku["tahun"]

        print(f"|{(str(index+1)) + '.':^4}| {judul:57}| {penulis:58}| {tahun:^4}  |")

    #* footer
    print(f"{'='*133}\n")

def create_terminal():
    #* header
    print(f"\n{'='*133}")
    
    #* data
    print(F"{'SILAHKAN MASUKKAN DATA BUKU BARU':^133}")
    print(f"{'='*133}")

    judul = input("JUDUL\t: ")
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

    #* footer
    print(f"{'='*133}\n")

    Operasi.create(judul, penulis, tahun)
    print(f"{'BUKU TERSIMPAN':^133}")
    read_terminal()

def update_terminal():
    read_terminal()

    #* header
    print(f"\n{'='*133}")

    while(True):
        no_buku = int(input("Silahkan pilih nomor buku yang akan diubah\nNOMOR BUKU\t: "))
        data_buku = Operasi.read(no_buku = no_buku) # mengambil data buku berdasarkan No. buku

        if data_buku:
            break

    # mengambil data tiap komponen
    data_break = data_buku.strip().split(",")
    pk = data_break[0].strip()
    date_add = data_break[1].strip()
    judul = data_break[2].strip()
    penulis = data_break[3].strip()
    tahun = data_break[4].strip()

    while(True):
        # data yang ingin diubah
        option = int(input(
            "\nSilahkan pilih komponen yang ingin anda ubah" +
            f"\n1. Judul\t:{judul:.50}" +
            f"\n2. Penulis\t:{penulis:.50}" +
            f"\n3. Tahun\t:{tahun:.50}" +
            "\nNomor komponen : "))
        
        # memilih komponen untuk diubah
        match (option):
            case 1 : judul = input("\njudul\t: ")
            case 2 : penulis = input("\npenulis\t: ")
            case 3 :
                while(True):
                    try:
                        tahun = int(input("\ntahun\t: "))
                        if (len(str(tahun)) == 4):
                            break
                        else:
                            print("tahun tidak valid")
                    except:
                        print("tahun harus berupa angka")
            case _ :
                print("nomor komponen tidak valid")
        
        #* footer
        print(f"{'='*133}\n")

        lanjut = input("lanjutkan mengubah komponen? (y/n) : ")
        if lanjut.lower() == "n":
            break

    Operasi.update(pk, date_add, no_buku, judul, penulis, tahun)




