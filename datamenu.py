import json

# ============================================
# Fungsi untuk membaca file JSON
# ============================================
def read_json_file():
    try:
        print("Membaca file menu.json...")
        with open("menu.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print("File berhasil dibaca!")
        return data
    except FileNotFoundError:
        print("Error: File menu.json tidak ditemukan!")
        return None


# ============================================
# Fungsi untuk menampilkan menu
# ============================================
def tampilkan_menu(data):
    print("\n=== DAFTAR MENU DAGING ===")
    menu = data["makanan"]
    for nomor, info in menu.items():
        print(f"{nomor}. {info['nama']} - Rp{info['Harga per kg']}/kg (Stok: {info['Stok']} kg)")
    print("===========================")

# ============================================
# Fungsi untuk menghitung harga dan diskon
# ============================================
def hitung_harga(nama_daging, jumlah_kg, harga_per_kg):
    bayar_awal = int(jumlah_kg * harga_per_kg)
    diskon = 0
    pesan = ""

    if nama_daging == "Ayam":
        if jumlah_kg >= 5:
            diskon = 0.1 * harga_per_kg
            pesan = f"Anda mendapatkan diskon 10% untuk Ayam: Rp{diskon}"
        else:
            pesan = "Maaf, pembelian Ayam minimal 5 kg untuk dapat diskon"
            
    elif nama_daging == "Babi":
        if jumlah_kg >= 3:
            diskon = 0.12 * harga_per_kg
            pesan = f"Anda mendapatkan diskon 12% untuk Babi: Rp{diskon}"
        else:
            pesan = "Maaf, pembelian Babi minimal 3 kg untuk dapat diskon"
            
    elif nama_daging == "Sapi":
        if jumlah_kg >= 5:
            diskon = 0.15 * harga_per_kg
            pesan = f"Anda mendapatkan diskon 15% untuk Sapi: Rp{diskon}"
        else:
            pesan = "Maaf, pembelian Sapi minimal 5 kg untuk dapat diskon"

    total = bayar_awal - diskon
    return total, pesan

# ============================================
# Fungsi utama aplikasi kasir
# ============================================
def aplikasi_kasir():
    print("Memulai aplikasi kasir...")
    
    data = read_json_file()
    if data is None:
        print("Program berhenti karena tidak bisa membaca data.")
        return None
    
    total = 0

    print("=== APLIKASI KASIR DAGING ===")

    # Transaksi pertama
    tampilkan_menu(data)
    pilihan = input("Masukkan nomor daging yang ingin dibeli (1/2/3): ")
    
    if pilihan not in data["makanan"]:
        print("Pilihan tidak valid!")
        return None
    
    info_daging = data["makanan"][pilihan]
    nama_daging = info_daging["nama"]
    harga_per_kg = info_daging["Harga per kg"]
    
    beli_daging = float(input(f"Masukkan jumlah {nama_daging} yang dibeli (dalam kg): "))
    
    total, pesan = hitung_harga(nama_daging, beli_daging, harga_per_kg)
    print(pesan)
    print("Total harga: Rp", total)
    
    data["makanan"][pilihan]["Stok"] -= beli_daging

    # Loop untuk beli lagi
    Klarifikasi = input("Apakah ingin beli lagi? (Cukup/Iya): ")

    while Klarifikasi == "Iya":
        tampilkan_menu(data)
        pilihan = input("Masukkan nomor daging yang ingin dibeli (1/2/3): ")
        
        if pilihan not in data["makanan"]:
            print("Pilihan tidak valid!")
            Klarifikasi = input("Apakah ingin beli lagi? (Cukup/Iya): ")
            continue
        
        info_daging = data["makanan"][pilihan]
        nama_daging = info_daging["nama"]
        harga_per_kg = info_daging["Harga per kg"]
        
        beli_daging2 = float(input(f"Masukkan jumlah {nama_daging} yang dibeli (dalam kg): "))
        
        total_transaksi, pesan = hitung_harga(nama_daging, beli_daging2, harga_per_kg)
        total += total_transaksi
        
        print(pesan)
        print("Total harga transaksi ini: Rp", total_transaksi)
        
        data["makanan"][pilihan]["Stok"] -= beli_daging2
        
        Klarifikasi = input("Apakah ingin beli lagi? (Cukup/Iya): ")


    print("\n=================================")
    print("Total keseluruhan harga yang dibayar: Rp", total)
    print("=================================")
    print("Terima kasih telah berbelanja!")

# ============================================
# Entry point
# ============================================
if __name__ == "__main__":
    aplikasi_kasir()