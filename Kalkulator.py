def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Pembagian dengan nol tidak diperbolehkan."

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
    elif pilihan == '2':
        print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
    elif pilihan == '3':
        print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
    elif pilihan == '4':
        print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

kalkulator()
