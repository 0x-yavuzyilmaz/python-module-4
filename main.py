# Alıştırma 1
us_al = lambda x, y: x ** y
print(us_al(5, 3))

# Alıştırma 2
urunler = [
    {"isim": "Laptop", "fiyat": 25000, "stok": 15},
    {"isim": "Mouse", "fiyat": 250, "stok": 150},
    {"isim": "Klavye", "fiyat": 500, "stok": 80}
]

fiyatlarina_gore_urunler = sorted(urunler, key=lambda urun: urun["fiyat"])

for urun in fiyatlarina_gore_urunler:
    print(urun)

print("\n")

stoklarina_gore_isimler = sorted(urunler, key=lambda urun: urun["stok"], reverse=True)
for urun in stoklarina_gore_isimler:
    print(urun)

# Alıştırma 3
noktalar = [(1, 5), (3, 2), (10, 1), (4, 4), (2, 8)]

orjine_uzaklik = sorted(noktalar, key=lambda nokta: nokta[0] ** 2 + nokta[1] ** 2)
print(orjine_uzaklik)

