# ALIŞTIRMA 1
isimler = [" ali", "VELİ ", " ayşe\n"]
isimler_map = map(lambda isim: isim.strip().title(), isimler)
isimler_list = list(isimler_map)
print(isimler_list)

isimler_list_comp = [isim.strip().title() for isim in isimler_list]
print(isimler_list_comp)

# Alıştırma 2

urunler = [
    {"isim": "Laptop", "fiyat": 25000},
    {"isim": "Mouse", "fiyat": 250},
    {"isim": "Klavye", "fiyat": 500},
    {"isim": "Monitör", "fiyat": 3000}
]

urunler_filter_nesne = filter(lambda urun: urun["fiyat"] < 1000, urunler)
urunler_filter_liste = list(urunler_filter_nesne)
print(urunler_filter_liste)

urunler_list_comp = [urun for urun in urunler if urun["fiyat"] < 1000]
print(urunler_list_comp)

#Alıştırma 3
sayilar = [-10, 5, 0, -2, 8, -1, 3]

filter_pozitif = filter(lambda x: x <= 0, sayilar)
map_n_to_p = map(lambda x: -x, filter_pozitif)
liste = list(map_n_to_p)
print(liste)

list_comp_liste = [abs(x) for x in sayilar if x <= 0]
print(list_comp_liste)

