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


başlıq = input("Başlıq: ")
kateqoriya = input("Kateqoriya: ")
məbləğ = float(input("Məbləğ: "))
data = yüklə()
data.append({"başlıq": başlıq, "kateqoriya": kateqoriya, "məbləğ": məbləğ})
yadda_saxla(data)
print("Əlavə olundu.")


def xərc_sil():


başlıq = input("Silinəcək başlıq: ")
data = yüklə()
data = [x for x in data if x["başlıq"] != başlıq]
yadda_saxla(data)
print("Silindi.")


def xərc_yenilə():


başlıq = input("Yenilənəcək başlıq: ")
yeni_məbləğ = float(input("Yeni məbləğ: "))
data = yüklə()
for x in data:
if x["başlıq"] == başlıq:
x["məbləğ"] = yeni_məbləğ
yadda_saxla(data)
print("Yeniləndi.")


def menyu():


while True:
print("\n1. Xərc əlavə et")
print("2. Xərc sil")
print("3. Xərc yenilə")
print("4. Çıx")

secim = input("Seçim: ")

if secim == "1":
xərc_əlavə_et()
elif secim == "2":
xərc_sil()
elif secim == "3":
xərc_yenilə()
elif secim == "4":
print("Sağ ol brat!")
break
else:
print("Yanlış seçim.")

menyu()
