Harga_Daging = 45000
Beli_Daging = int(input("Masukkan jumlah daging yang dibeli: "))

if Beli_Daging == 2:
    print(f"--- Total_harga_daging = {Beli_Daging * Harga_Daging - 5000} ---")
    print("Anda mendapatkan diskon 5000")
elif Beli_Daging > 5:
    print(f"--- Total_harga_daging = {Beli_Daging * Harga_Daging - 5000} ---")
    print("Anda mendapatkan diskon 7000")

else: 
    print(f"--- Total_harga_daging = {Beli_Daging * Harga_Daging} ---")
    print("Maaf, Anda tidak mendapatkan diskon")
