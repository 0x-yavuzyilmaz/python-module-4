# Alıştırma 1
kelimeler = ["python", "öğrenmek", "çok", "güzel"]
print([len(kelime) for kelime in kelimeler])

# Alıştırma 2

sayilar = [1, -5, 12, -8, 15, 2, -10, 7]
pozitiflerin_iki_kati = [sayi * 2 for sayi in sayilar if sayi > 0]
print(pozitiflerin_iki_kati)

# Alıştırma 3
fiyatlar = [100, 150, 80, 220, 50, 400]

etiketler = ["Pahalı" if fiyat > 100 else "Uygun" for fiyat in fiyatlar]
print(etiketler)

# Bonus.

ic_ice_liste = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

tek_liste = [eleman for liste in ic_ice_liste for eleman in liste]
print(tek_liste)






