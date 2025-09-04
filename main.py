# Alıştırma 1
from collections import defaultdict

renkler = ["kırmızı", "mavi", "yeşil", "kırmızı", "sarı", "mavi", "kırmızı"]
renkler_sayaci = defaultdict(int)
for renk in renkler:
    renkler_sayaci[renk] += 1

print(renkler_sayaci)

# Alıştırma 2
from collections import defaultdict

metin = "programlama"
harf_konumlari = defaultdict(list)

for indeks, harf in enumerate(metin):
    harf_konumlari[harf].append(indeks)
print(harf_konumlari)

# Alıştırma 3
from collections import defaultdict

mac_sonuclari = [
    ("Galatasaray", 3),
    ("Fenerbahçe", 1),
    ("Beşiktaş", 3),
    ("Galatasaray", 1),
    ("Fenerbahçe", 3),
    ("Galatasaray", 3)
]

puan_tablosu = defaultdict(int)

for mac_sonucu in mac_sonuclari:
    takim, puan = mac_sonucu
    puan_tablosu[takim] += puan

print("--- PUAN TABLOSU ---")
for takim, puan in puan_tablosu.items():
    print(f"{takim:<12}: {puan}")


