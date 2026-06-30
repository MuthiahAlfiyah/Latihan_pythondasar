#DAGING DAN PRICELIST
Daging = ["Ayam", "Sapi", "Babi"]
Price_kg = [15000, 12000, 10000]

total_keseluruhan = 0
total = 0


Question = Daging[int(input("Masukkan nomor daging yang ingin dibeli: ")) - 1]
beli_daging = float(input("Masukkan jumlah daging yang dibeli (dalam kg): "))
bayar_awal = int(beli_daging * Price_kg[Daging.index(Question)])

# Perbaikan: if-else per jenis daging
if Question == "Ayam":
    if beli_daging >= 5:
        diskon = 0.1 * Price_kg[0]
        total += bayar_awal - diskon
        print(f"Anda mendapatkan diskon 10% untuk Ayam: Rp{diskon}")
    else:
        total += bayar_awal
        print("Maaf, pembelian Ayam minimal 5 kg untuk dapat diskon")
        
elif Question == "Babi":
    if beli_daging >= 3:
        diskon = 0.12 * Price_kg[2]
        total += bayar_awal - diskon
        print(f"Anda mendapatkan diskon 12% untuk Babi: Rp{diskon}")
    else:
        total += bayar_awal
        print("Maaf, pembelian Babi minimal 3 kg untuk dapat diskon")
        
elif Question == "Sapi":
    if beli_daging >= 5:
        diskon = 0.15 * Price_kg[1]
        total += bayar_awal - diskon
        print(f"Anda mendapatkan diskon 15% untuk Sapi: Rp{diskon}")
    else:
        total += bayar_awal
        print("Maaf, pembelian Sapi minimal 5 kg untuk dapat diskon")

print("Total harga: Rp", total)

Klarifikasi = input("Apakah ingin beli lagi? (Cukup/Iya): ")

while Klarifikasi == "Iya":
    Question = Daging[int(input("Masukkan nomor daging yang ingin dibeli: ")) - 1]
    beli_daging2 = float(input("Masukkan jumlah daging yang dibeli (dalam kg): "))
    
    bayar_inf = int(beli_daging2 * Price_kg[Daging.index(Question)])
    total_all = total + bayar_inf
    # Perbaikan: if-else per jenis daging (sama seperti di atas)
    if Question == "Ayam":
        if beli_daging2 >= 5:
            diskon = 0.1 * Price_kg[0]
            total = total_all - diskon
            print(f"Anda mendapatkan diskon 10% untuk Ayam: Rp{diskon}")
        else:
            total = total_all
            print("Maaf, pembelian Ayam minimal 5 kg untuk dapat diskon")
            
    elif Question == "Babi":
        if beli_daging2 >= 3:
            diskon = 0.12 * Price_kg[2]
            total = total_all - diskon
            print(f"Anda mendapatkan diskon 12% untuk Babi: Rp{diskon}")
        else:
            total = total_all
            print("Maaf, pembelian Babi minimal 3 kg untuk dapat diskon")
            
    elif Question == "Sapi":
        if beli_daging2 >= 5:
            diskon = 0.15 * Price_kg[1]
            total = total_all - diskon
            print(f"Anda mendapatkan diskon 15% untuk Sapi: Rp{diskon}")
        else:
            total = total_all
            print("Maaf, pembelian Sapi minimal 5 kg untuk dapat diskon")
    

    print("Total harga transaksi ini: Rp", total)
    
    Klarifikasi = input("Apakah ingin beli lagi? (Cukup/Iya): ")

print("Total keseluruhan harga yang dibayar: Rp", total_keseluruhan)