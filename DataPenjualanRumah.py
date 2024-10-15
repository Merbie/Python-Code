# list data penjualan
data_penjualan = [
    {"Nama_Barang": "Pensil", "Jumlah_Terjual": 100, "Harga": 2000},
    {"Nama_Barang": "Buku Tulis", "Jumlah_Terjual": 50, "Harga": 5000},
    {"Nama_Barang": "Penggaris", "Jumlah_Terjual": 30, "Harga": 3000},
    {"Nama_Barang": "Bolpoin", "Jumlah_Terjual": 70, "Harga": 4000},
    {"Nama_Barang": "Penghapus", "Jumlah_Terjual": 40, "Harga": 1500},
    {"Nama_Barang": "Spidol", "Jumlah_Terjual": 20, "Harga": 6000},
    {"Nama_Barang": "Stapler", "Jumlah_Terjual": 15, "Harga": 8000},
    {"Nama_Barang": "Amplop", "Jumlah_Terjual": 60, "Harga": 1000},
    {"Nama_Barang": "Map Plastik", "Jumlah_Terjual": 25, "Harga": 7000},
    {"Nama_Barang": "Kertas HVS", "Jumlah_Terjual": 80, "Harga": 1200}
]

# menghitung total pendapatan
total_pendapatan = 0
barang_terlaris = None
jumlah_terjual_terbanyak = 0

print("Data Penjualan:")
for item in data_penjualan:
    # menghitung pendapatan perbarang
    total_pendapatan_barang = item["Jumlah_Terjual"] * item["Harga"]
    item["Total_Pendapatan"] = total_pendapatan_barang
    total_pendapatan += total_pendapatan_barang
    
    # mencari barang terlaris
    if item["Jumlah_Terjual"] > jumlah_terjual_terbanyak:
        barang_terlaris = item
        jumlah_terjual_terbanyak = item["Jumlah_Terjual"]
    
    # menampilkan data penjualan setiap barang
    print(f"{item['Nama_Barang']}: Jumlah Terjual = {item['Jumlah_Terjual']}, Harga = Rp {item['Harga']}, Total Pendapatan = Rp {total_pendapatan_barang}")

# menampilkan hasil analisis
print(f"\nTotal Pendapatan Keseluruhan: Rp {total_pendapatan}")
if barang_terlaris:
    print(f"Barang Terlaris: {barang_terlaris['Nama_Barang']} (Jumlah Terjual: {barang_terlaris['Jumlah_Terjual']})")
