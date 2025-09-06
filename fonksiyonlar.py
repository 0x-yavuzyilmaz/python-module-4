from collections import Counter
from typing import List

"""
"Kelime Frekans Analizörü" programı için gerekli olan fonksiyonlar modülü.
"""


def dosyayi_oku(dosya_yolu: str) -> str:
    """
    Metin verilerinin çekileceği dosyanın alıp içeriği string olarak döndürür.
    Args:
        dosya_yolu(str): dosya yolunun adı

    Returns:
        str: Dosyanın içeriğini string olarak döndürür.

    """

    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            icerik = f.read()
            return icerik
    except FileNotFoundError:
        print(f"Hata: '{dosya_yolu}' adında bir dosya bulunamadı.")
        return None


def metni_temizle(metin: str) -> List[str]:
    """
    Metinin tamamımı küçük harfe çevirir, noktalama işaretlerini ve metin uçlarındaki boşlukları temizler.
    Args:
        metin(str): metin içeriği

    Returns:
        list: Metin içeriğini temizledikten sonra içeriği liste olarak döndürür.

    """
    metin = (metin.lower().replace(',', ' ').replace('.', ' ')
             .replace('?', ' ').replace('!', ' ').replace(';', ' ').strip())
    return metin.split()


def kelimeleri_say(kelime_listesi: List[str]) -> Counter:
    """
    Liste halindeki metin içerğindeki kelimeleri Counter fonksiyonu ile sayar.
    Args:
        kelime_listesi(List): Metin içeriği liste olarak alınır

    Returns:
        Counter: Counter nesnesi olarak kelime ve sayıları döndürür.

    """
    return Counter(kelime_listesi)


def istenmeyenleri_cikar(frekanslar: Counter, istenmeyenler: set) -> Counter:
    """
    Sık geçen bağlaç, edat gibi kelimleri metinden çıkarma imkanı sağlar.
    Args:
        frekanslar(Counter): Metin içindeki kelimeler ve sayıları
        istenmeyenler(set): Çıkarılmak istenen kelimeler

    Returns:
        Counter: İstenmeyen kelimeler Counter nesnesinden çıkarılıp geri döndürülür.

    """
    for kelime in istenmeyenler:
        frekanslar.pop(kelime, None)

    return frekanslar


def sonucu_goster(frekanslar: Counter, adet: int) -> None:
    """
    En çok kelime listeleneceği kullanılıcıya sorulur ve uygun formatta sonuçlar listelenir.
    Args:
        frekanslar(Counter): Kelime sayıları ve frekanslarını içerir.
        adet(int):  En çok kelime listeleneceği tam sayı olarak alınır

    Returns:

    """
    frekanslar_list = Counter(frekanslar).most_common(adet)
    print("KELİME FREKANS TABLOSU")
    print("-" * 30)
    for sira, (kelime, frekanslar) in enumerate(frekanslar_list):
        print(f"{sira}.: {kelime} kelimesi : {frekanslar} adet ")
