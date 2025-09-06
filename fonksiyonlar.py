from collections import Counter


def dosyayi_oku(dosya_yolu: str) -> str:
    with open(dosya_yolu, 'r', encoding='utf-8') as f: icerik = f.read()
    return icerik


def metni_temizle(metin: str) -> List[str]:
    metin = (metin.lower().replace(',', ' ').replace('.', ' ')
             .replace('?', ' ').replace('!', ' ').replace(';', ' '))
    return metin.strip().split()


def kelimeleri_say(kelime_listesi: List[str]) -> Counter:
    return Counter(kelime_listesi)


def istenmeyenleri_cikar(frekanslar: Counter, istenmeyenler: set) -> Counter:
    for kelime in istenmeyenler:
        frekanslar.pop(kelime, None)

    return frekanslar


def sonucu_goster(frekanslar: Counter, adet: int) -> None:
    frekanslar_list = Counter(frekanslar).most_common(adet)
    print("KELİME FREKANS TABLOSU":)
    print("-" * 30)
    for sira, (kelime, frekanslar) in enumerate(frekanslar_list):
        print(f"{sira}.: {kelime} kelimesi : {frekanslar} adet ")
