# Alıştırma 1
kisisel_bilgiler = {
    "isim": "Yavuz",
    "yas": 39,
    "sehir": "İstanbul"
}

kisisel_bilgiler["meslek"] = "Öğretmen"
kisisel_bilgiler["yas"] = kisisel_bilgiler["yas"] + 1
del kisisel_bilgiler["sehir"]
print(kisisel_bilgiler)

# Alıştırma 2

stok_durumu = {"elma": 50, "muz": 30, "portakal": 45}
urun_adi = input("Hangi ürünün stok durumunu bilmek istersiniz?")

stok_miktari = stok_durumu.get(urun_adi)
if stok_miktari:
    print(f"{urun_adi} ürününden stokta {stok_miktari} adet bulunmaktadır.")
else:
    print(f"Üzgünüz, {urun_adi} stoklarımızda bulunmamaktadır.")

for urun, stok in stok_durumu.items():
    print(f"{urun} --> {stok} adet")

# Alıştırma 3
cumle = "merhaba dünya"
harf_frekanslari = {}
for harf in cumle:
    if harf == " ":
        continue
    if harf not in harf_frekanslari:
        harf_frekanslari[harf] = 1
    else:
        harf_frekanslari[harf] += 1

print(harf_frekanslari)
