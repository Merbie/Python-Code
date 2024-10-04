def tampilkan_menu():
    print("\n===== Menu Utama =====")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Hapus Data")
    print("4. Keluar")
    print("======================")

def tambah_data(data):
    item = input("Masukkan data: ")
    data.append(item)
    print(f"'{item}' berhasil ditambahkan.")

def lihat_data(data):
    if not data:
        print("Data kosong.")
    else:
        print("\nData yang tersimpan:")
        for index, item in enumerate(data, start=1):
            print(f"{index}. {item}")

def hapus_data(data):
    lihat_data(data)
    try:
        pilihan = int(input("\nPilih nomor data yang akan dihapus: "))
        if 1 <= pilihan <= len(data):
            item = data.pop(pilihan - 1)
            print(f"'{item}' berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def main():
    data = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tambah_data(data)
        elif pilihan == '2':
            lihat_data(data)
        elif pilihan == '3':
            hapus_data(data)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()