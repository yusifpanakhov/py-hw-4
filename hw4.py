import json
import os

FAYL = "expenses.json"

def yüklə():
    if os.path.exists(FAYL):
        with open(FAYL, "r") as f:
            return json.load(f)
    return []

def yadda_saxla(data):
    with open(FAYL, "w") as f:
        json.dump(data, f, indent=2)

def xərc_əlavə_et():
    başlıq = input("Başliq: ")
    kateqoriya = input("Kateqoriya: ")
    məbləğ = float(input("Mebleg: "))
    data = yüklə()
    data.append({"başliq": başlıq, "kateqoriya": kateqoriya, "mebleg": məbləğ})
    yadda_saxla(data)
    print("Elavə olundu.")

def xərc_sil():
    başlıq = input("Silinecek başliq: ")
    data = yüklə()
    data = [x for x in data if x["başliq"] != başliq]
    yadda_saxla(data)
    print("Silindi")

def xərc_yenilə():
    başlıq = input("Yenilenecek başliq: ")
    yeni_məbləğ = float(input("Yeni mebleğ: "))
    data = yüklə()
    for x in data:
        if x["başliq"] == başlıq:
            x["mebleğ"] = yeni_məbləğ
    yadda_saxla(data)
    print("Yenilendi.")

def menyu():
    while True:
        print("\n1. Xerc elave et")
        print("2. Xerc sil")
        print("3. Xerc yenile")
        print("4. Çix")

        secim = input("Secim: ")

        if secim == "1":
            xərc_əlavə_et()
        elif secim == "2":
            xərc_sil()
        elif secim == "3":
            xərc_yenilə()
        elif secim == "4":
            print("Sag ol ")
            break
        else:
            print("Yanlis secim.")

menyu()