# Alıştırma 1 (Kolay): Basit Sıralama

sayilar = [4, 1, 7, 3, 9, 2, 8, 5, 6]
sayilar.sort()
print(f"Küçükten büyüğe: {sayilar}")
sayilar.sort(reverse=True)
print(f"Büyükten küçüğe: {sayilar}")

# Alıştırma 2
kelimeler = ["elma", "Karpuz", "muz", "Armut", "çilek"]
alfabetik_sirali_liste = sorted(kelimeler, key=str.lower)
print(alfabetik_sirali_liste)
uzunluga_gore_liste = sorted(kelimeler, key=len)
print(uzunluga_gore_liste)

# Alıştırma 3
ogrenciler = [["Ali", 85], ["Zeynep", 92], ["Can", 78], ["Ayşe", 92], ["Veli", 85]]

def ilk_eleman(liste):
    return liste[1]

alf_sirali_liste = sorted(ogrenciler, key=ilk_eleman, reverse=True)
print(alf_sirali_liste)

def detayli_sirali(liste):
    return -liste[1],liste[0]
alf_detayli_sirali_liste=sorted(ogrenciler, key=detayli_sirali)
print(alf_detayli_sirali_liste)
