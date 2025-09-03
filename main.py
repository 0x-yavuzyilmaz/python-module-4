# Alıştırma 1 (Kolay): Tekrar Edenleri Temizle

siparis_kodlari = [101, 102, 103, 101, 104, 102, 105, 106, 103]
print(f"Veri Kümesi: {set(siparis_kodlari)}, Veri Tipi: {type(set(siparis_kodlari))}")

python_kursu = {"Ali", "Veli", "Ayşe", "Fatma", "Can"}
web_gelistirme_kursu = {"Zeynep", "Buse", "Ali", "Can", "Mehmet"}


# Alıştırma 2


def yazdir(kume: set, baslik: str) -> None:
    print(baslik)
    print("-" * 25)
    for ogrenci in kume:
        print(ogrenci)
    print("-" * 25)
    print("\n")


kesisim_kurs = python_kursu.intersection(web_gelistirme_kursu)
birlesim_kurs = python_kursu.union(web_gelistirme_kursu)
yalniz_python = python_kursu.difference(web_gelistirme_kursu)

yazdir(kesisim_kurs, "Her iki kursa birden katılan öğrenciler:")
yazdir(birlesim_kurs, "Her iki kursa birden katılan öğrenciler:")
yazdir(yalniz_python, "Yalnız python kursuna katılan öğrenciler:")


# Alıştırma 3

def pangram_tester(cumle: str) -> None:
    """
    Verilen cümlenin pangram olup olmadığını test eder.
    Args:
        cumle(str):

    Returns:
        None

    """
    alfabe = set("abcdefghijklmnopqrstuvwxyz")
    set(cumle.lower())
    cumle_kumesi = set()

    for harf in set(cumle.lower()):
        if harf == " ":
            continue
        else:
            cumle_kumesi.add(harf)

    fark_kumesi = alfabe.difference(cumle_kumesi)
    if not fark_kumesi:
        print("Cümle bir pangramdır.")
    else:
        print(f"Cümle bir pangram değildir.Eksik olan harfler:")
        for harf in fark_kumesi:
            print(f"--{harf}--")


cumle = "the quick brown fox jumps over the lazy dog"
cumle2 = "merhaba dunya"
pangram_tester(cumle)
pangram_tester(cumle2)
