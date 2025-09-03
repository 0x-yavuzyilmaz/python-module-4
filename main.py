# Alıştırma 1 (Kolay): İsim Düzeltici

isimler = [" aLi ", "VELİ ", "\tayşe\n", " fatma"]
temiz_isimler = []
for isim in isimler:
    temiz_isimler.append(isim.strip().lower().title())

print(temiz_isimler)


# Alıştırma 2 (Orta Zorluk): URL Oluşturucu ("Slugify")

def slugify(baslik: str) -> str:
    baslik = (baslik.strip().lower().replace("ğ", "g").replace("ı", "i").
              replace("ü", "u").replace("ö", "o")
              .replace("ç", "c").replace("ş", "s"))
    baslik_liste = baslik.split()
    baslik_slug = "-".join(baslik_liste)
    return baslik_slug


ornek_baslik = " Python Öğrenmek ne kadar da Güzel! "

print(slugify(ornek_baslik))


def slugify_pythonic(baslik: str) -> str:
    baslik = baslik.lower().strip()
    karakter_haritasi = {
        "ğ": "g",
        "ı": "i",
        "ş": "s",
        "ö": "o",
        "ü": "u",
        "ç": "c"
    }
    for eski, yeni in karakter_haritasi.items():
        baslik = baslik.replace(eski, yeni)
    baslik_liste = baslik.split()
    baslik_slug = "-".join(baslik_liste)
    return baslik_slug


print(slugify_pythonic(ornek_baslik))

# Alıştırma 3 (İleri Seviye): Veri Ayıklayıcı

ham_veri = """ isim|soyisim|yas|sehir Ali|Yılmaz|30|İstanbul Ayşe|Kaya|25|Ankara Veli|Can|45|İzmir """
islenmis_veri = ham_veri.strip()
satirlar = islenmis_veri.split(" ")
basliklar = satirlar[0].split("|")
degerler_listesi = []

for kisi in satirlar[1:]:
    degerler_listesi.append(kisi.split("|"))

for kisi in degerler_listesi:
    for indeks in range(len(kisi)):
        print(f"{basliklar[indeks].title()}: {kisi[indeks]}", end=", ")

    print("\n")
