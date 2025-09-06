import fonksiyonlar as fn
import time
    """
    Kelime Frekans Analizörü programının ana pipeline programı.
    """

BASLIK = "Kelime Frekans Analizörü"
GENISLIK = 60
AYRAC = "=" * GENISLIK

print(f"\n{AYRAC}")
print(f"{BASLIK.center(GENISLIK)}")
print(f"{'Programına Hoş Geldiniz!'.center(GENISLIK)}")
print(f"{AYRAC}\n")
print("Lütfen aşağıdaki yönergeleri dikkatle takip ediniz.".center(GENISLIK))
print("\n")

while True:
    dosya_yolu = input("Dosya yolu giriniz: ")
    metin = fn.dosyayi_oku(dosya_yolu)
    if metin is not None:
        break

temizlenmis_metin = fn.metni_temizle(metin)
kelime_sayisi_counter = fn.kelimeleri_say(temizlenmis_metin)
time.sleep(1)
print("İstenmeyen kelimeleri giriniz. (Bitirmek için doğrudan Enter'a basınız)")

istenmeyen_kelimeler = set()
while True:
    kelime = input("İstenmeyen Kelime: ")
    if kelime == "":
        break
    istenmeyen_kelimeler.add(kelime)
print("\nOluşturulan istenmeyen kelimeler kümesi:")
print(istenmeyen_kelimeler)
time.sleep(1)
print("\n")

frekanslar = fn.istenmeyenleri_cikar(kelime_sayisi_counter, istenmeyen_kelimeler)
en_fazla_sinirla = int(input("En fazla kaç kelimenin sıklığını göstermek istersiniz:\n"))
fn.sonucu_goster(frekanslar, en_fazla_sinirla)

print(f"\n{AYRAC}")
