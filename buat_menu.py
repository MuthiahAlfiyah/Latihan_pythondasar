import json

# Data menu yang akan ditulis ke file JSON
data = {
    "makanan": {
        "1": {"nama": "Ayam", "Harga per kg": 50000, "Stok": 100},
        "2": {"nama": "Sapi", "Harga per kg": 12000, "Stok": 80},
        "3": {"nama": "Babi", "Harga per kg": 10000, "Stok": 50}
    }
}

# Tulis ke file menu.json
with open("menu.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print("✅ File menu.json berhasil dibuat!")
print("Sekarang Anda bisa jalankan: python datamenu.py")