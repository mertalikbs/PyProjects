#selam verilecek, menü ekranında kişileri göster, yeni kişi ekle tuşları olacak.

print("Rehbere hoş geldin.")

from replit import clear
from time import sleep
directory = {}

def adding():
    name = input("Eklenilen kişinin adı: ")
    number = input("  Eklenilen kişinin numarası: ")
    directory[name] = number

def removing():
    name = input("Çıkarılacak kişinin adı: ")
    if name in directory:
        answer = input(f"Çıkarmak istediğiniz kişinin numarası {directory[name]}\n  İşleme devam etmek istediğinize emin misiniz?\n    Evet için 'e', hayır için 'h' basın.")
        if answer == "e":
            del directory[name]
        if answer == "h":
            return
    else:
        print("Yazdığınız kişi rehberde bulunamadı.")
        

isContinue = True
while isContinue:
    demand = input("\nYapmak istediğiniz eylemi giriniz. Rehbere yeni kişi eklemek için 'a', rehberden birini çıkarmak için 'r' veya rehberinizdeki kişileri görmek için 's' tuşuna basın. Uygulamayı durdurmak için ise 'x' yazın.\n")
    if demand == "a":
        adding()
        clear()
    elif demand == "r":
        removing()
        clear()
    elif demand == "s":
        for i in directory:
            print(f"{i}: {directory[i]}")
        sleep(5)
        clear()
    elif demand == "x":
        isContinue = False
        print("Uygulama kapatılıyor...")
        sleep(3)
        clear()
    else:
        print("Yapmak istediğiniz işlem anlaşılamadı.")
        clear()