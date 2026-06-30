Harga_Daging = 50000

#Input Pembelian
Beli_Daging = int(input("Masukkan jumlah daging yang dibeli: "))
Bayar_awal =int(Beli_Daging * Harga_Daging)
#Prob pembelian
if Beli_Daging > 5:
     diskon = 7000
     total = Bayar_awal - diskon
elif Beli_Daging >= 2:
     diskon = 5000
     total = Bayar_awal - diskon
else: 
    diskon = 0
    total = Bayar_awal - diskon

print("Total harga: Rp", total)

Klarifikasi=input("Apakah ingin beli lagi? (Cukup/Iya): ")

while Klarifikasi == "Iya":
     Beli_Daging2= int(input("Masukkan jumlah daging yang dibeli: "))
     Bayar_inf = int(Beli_Daging2 * Harga_Daging)
     total_all = Bayar_awal + Bayar_inf
     if Beli_Daging2 > 5:
        diskon = 7000
        total = total_all - diskon
     elif Beli_Daging2 >= 2:
        diskon = 5000
        total = total_all - diskon
     else: 
        diskon = 0
        total = total_all
     print("Total harga: Rp", total)
     Klarifikasi=input("Apakah ingin beli lagi? (Cukup/Iya): ")

print("Total keseluruhan harga yang dibayar: Rp", total)   


