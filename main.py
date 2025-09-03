# Alıştırma 4
urun_stoklari = {"elma": 50, "muz": 30, "portakal": 0, "karpuz": 15}

tukenmis_urunler = [anahtar.upper() for anahtar, deger in urun_stoklari.items() if deger == 0]

print(tukenmis_urunler)



# Alıştırma 5

cumleler = ["Python öğrenmek harika", "List comprehension çok güçlü bir araç", "Veri bilimi eğlenceli"]

a_iceren_uzun_kelimeler = [kelime for cumle in cumleler for kelime in cumle.split() if
                           len(kelime) > 5 and "a" in kelime]
print(a_iceren_uzun_kelimeler)


# Alıştırma 6.

matris = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transpose_matris = [[satir[sutun_indeksi] for satir in matris] for sutun_indeksi in range(len(matris[0]))]
print(transpose_matris)