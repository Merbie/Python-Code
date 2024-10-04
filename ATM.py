class ATM:
    def __init__(self, saldo_awal=0):
        self.saldo = saldo_awal
        self.transaksi = []

    def lihat_saldo(self):
        print(f"Saldo Anda saat ini: Rp {self.saldo}")
        self.transaksi.append(f"Lihat saldo: Rp {self.saldo}")

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Berhasil menambahkan saldo sebesar Rp {jumlah}")
            self.transaksi.append(f"Tambah saldo: Rp {jumlah}")
        else:
            print("Jumlah yang ditambahkan harus positif.")

    def tarik_tunai(self, jumlah):
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Berhasil menarik tunai sebesar Rp {jumlah}")
            self.transaksi.append(f"Tarik tunai: Rp {jumlah}")
        elif jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk penarikan ini.")
        else:
            print("Jumlah yang ditarik harus positif.")

    def lihat_riwayat_transaksi(self):
        if self.transaksi:
            print("Riwayat Transaksi:")
            for transaksi in self.transaksi:
                print(f"- {transaksi}")
        else:
            print("Belum ada transaksi.")


class Bank:
    def __init__(self):
        # Dictionary untuk menyimpan data pengguna: username sebagai key dan ATM sebagai value
        self.pengguna = {}

    def registrasi(self, username, password):
        if username in self.pengguna:
            print("Username sudah terdaftar. Silakan gunakan username lain.")
        else:
            self.pengguna[username] = {'password': password, 'atm': ATM(100000)}
            print(f"Akun berhasil dibuat untuk {username} dengan saldo awal Rp 100000.")

    def login(self, username, password):
        if username in self.pengguna and self.pengguna[username]['password'] == password:
            print(f"Login berhasil! Selamat datang, {username}!")
            return self.pengguna[username]['atm']
        else:
            print("Login gagal! Username atau password salah.")
            return None

# Membuat sistem bank yang mengelola banyak akun pengguna
bank = Bank()

# Fungsi untuk interaksi dengan pengguna
def mulai():
    while True:
        print("\n=== Selamat Datang di ATM ===")
        print("1. Registrasi Akun")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            bank.registrasi(username, password)
        
        elif pilihan == '2':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            akun_atm = bank.login(username, password)

            if akun_atm:
                while True:
                    print("\n=== Menu ATM ===")
                    print("1. Lihat Saldo")
                    print("2. Tambah Saldo")
                    print("3. Tarik Tunai")
                    print("4. Lihat Riwayat Transaksi")
                    print("5. Logout")
                    pilihan_atm = input("Pilih menu (1-5): ")

                    if pilihan_atm == '1':
                        akun_atm.lihat_saldo()
                    elif pilihan_atm == '2':
                        jumlah = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
                        akun_atm.tambah_saldo(jumlah)
                    elif pilihan_atm == '3':
                        jumlah = int(input("Masukkan jumlah saldo yang ingin ditarik: "))
                        akun_atm.tarik_tunai(jumlah)
                    elif pilihan_atm == '4':
                        akun_atm.lihat_riwayat_transaksi()
                    elif pilihan_atm == '5':
                        print(f"Logout berhasil. Sampai jumpa, {username}!")
                        break
                    else:
                        print("Pilihan tidak valid, silakan coba lagi.")
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan layanan ATM!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Memulai aplikasi
mulai()
