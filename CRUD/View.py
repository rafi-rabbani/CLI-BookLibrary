from . import Operasi

def read_terminal():
    data_file = Operasi.read()

    index = "NO"
    penulis = "PENULIS"
    judul = "JUDUL"
    tahun = "TAHUN"

    #* header
    print(f"\n{'='*133}")

    print(f"|{index:^4}|{judul:^58}|{penulis:^59}|{tahun:^7}|")
    print("-"*133)

    #* data
    for index,data in enumerate(data_file):

        # memisah data (break) melalui [,]
        data_break = data.strip().split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        print(f"|{(str(index+1)) + '.':^4}| {judul:.57}| {penulis:.58}| {tahun:^4}  |")

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

