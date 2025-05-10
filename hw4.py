import json
import os

FAYL = "expenses.json"

def yukle():
    if os.path.exists(FAYL):
        with open(FAYL, "r") as f:
            return json.load(f)
    return []

def yadda_saxla(data):
    with open(FAYL, "w") as f:
        json.dump(data, f, indent=2)

def xerc_elave_et():
    basliq = input("Basliq: ")
    kateqoriya = input("Kateqoriya: ")
    mebleg = float(input("Mebleg: "))
    data = yukle()
    data.append({"basliq": basliq, "kateqoriya": kateqoriya, "mebleg": mebleg})
    yadda_saxla(data)
    print("Elave olundu.")

def xerc_sil():
    basliq = input("Silinecek basliq: ")
    data = yukle()
    data = [x for x in data if x["basliq"] != basliq]
    yadda_saxla(data)
    print("Silindi")

def xerc_yenile():
    basliq = input("Yenilenecek basliq: ")
    yeni_mebleg = float(input("Yeni mebleg: "))
    data = yukle()
    for x in data:
        if x["basliq"] == basliq:
            x["mebleg"] = yeni_mebleg
    yadda_saxla(data)
    print("Yenilendi.")

def menyu():
    while True:
        print("\n1. Xerc elave et")
        print("2. Xerc sil")
        print("3. Xerc yenile")
        print("4. cix")

        secim = input("Secim: ")

        if secim == "1":
            xerc_elave_et()
        elif secim == "2":
            xerc_sil()
        elif secim == "3":
            xerc_yenile()
        elif secim == "4":
            print("Sag ol ")
            break
        else:
            print("Yanlis secim.")

menyu()