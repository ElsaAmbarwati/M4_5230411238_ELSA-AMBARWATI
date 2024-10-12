class Debitur:
    def __init__(self, nama, ktp, limit):
        self.nama = nama
        self.ktp = ktp
        self.limit = limit

class Pinjaman:
    def __init__(self, debitur, jumlah, bunga, bulan, angsuran):
        self.debitur = debitur
        self.jumlah = jumlah
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = angsuran

daftar_debitur = [
    Debitur("Rimuru", "7890", 1700000),
    Debitur("Diablo", "8901", 1500000),
    Debitur("Carera", "9012", 1900000),
    Debitur("Testarossa", "0012", 7000000),
    Debitur("Ultima", "0013", 4500000),
]

daftar_pinjaman = [
    Pinjaman("Rimuru", 3000000, 2, 7, 125000),
    Pinjaman("Yanto", 5000000, 3, 10, 121000),
    Pinjaman("Diablo", 2000000, 4, 12, 210000)
]

def tampilkan_menu():
    print("=============== Aplikasi Admin Pinjol ===============")
    print("1. Kelola Debitur")
    print("2. Pinjaman")
    print("0. Keluar")
    pilihan = input("Masukan Pilihan : ")
    return pilihan

def kelola_debitur():
    while True:
        print("=============== Kelola Debitur ===============")
        print("1. Tampilkan Semua Debitur")
        print("2. Cari Debitur")
        print("3. Tambah Debitur")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu : ")
        
        if sub_menu == '1':
            print("=============== Daftar Debitur ===============")
            print("{:<15} {:<10} {:<15}".format("Nama Debitur", "No KTP", "Limit Pinjaman"))
            for debitur in daftar_debitur:
                print("{:<15} {:<10} Rp.{:<15,.0f}".format(debitur.nama, debitur.ktp, debitur.limit))
            

        elif sub_menu == '2':
            ktp = input("Masukkan No KTP: ")
            found = False
            for debitur in daftar_debitur:
                if debitur.ktp == ktp:
                    print(f"Nama: {debitur.nama}, Limit: Rp.{debitur.limit:,.0f}")
                    found = True
                    break
            if not found:
                print("Debitur tidak ditemukan.")
            

        elif sub_menu == '3':
            nama = input("Masukkan Nama: ")
            ktp = input("Masukkan No KTP: ")
            limit = int(input("Masukkan Limit Pinjaman: "))
            daftar_debitur.append(Debitur(nama, ktp, limit))
            print("Debitur berhasil ditambahkan!")
            

        elif sub_menu == '0':
            break

def menu_pinjaman():
    while True:
        print("=============== Menu Pinjaman ===============")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Pinjaman")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu : ")

        if sub_menu == '1':
            debitur = input("Masukkan Nama Debitur: ")
            jumlah = int(input("Masukkan Jumlah Pinjaman: "))
            bunga = int(input("Masukkan Bunga (%): "))
            bulan = int(input("Masukkan Lama Pinjaman (Bulan): "))
            angsuran = (jumlah * (1 + bunga / 100)) / bulan
            daftar_pinjaman.append(Pinjaman(debitur, jumlah, bunga, bulan, angsuran))
            print("Pinjaman berhasil ditambahkan!")
            

        elif sub_menu == '2':
            print("=============== Daftar Pinjaman ===============")
            print("{:<15} {:<15} {:<10} {:<10} {:<15}".format("Nama Debitur", "Pinjaman", "Bunga", "Bulan", "Angsuran(Bln)"))
            for pinjaman in daftar_pinjaman:
                print("{:<15} Rp.{:<15,.0f} {:<10}% {:<10} Rp.{:<15,.0f}".format(pinjaman.debitur, pinjaman.jumlah, pinjaman.bunga, pinjaman.bulan, pinjaman.angsuran))
           

        elif sub_menu == '0':
            break

while True:
    pilihan = tampilkan_menu()
    
    if pilihan == '1':
        kelola_debitur()
    elif pilihan == '2':
        menu_pinjaman()
    elif pilihan == '0':
        print("Keluar dari program...")
        break
