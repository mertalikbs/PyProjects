print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine Avı oyununa hoş geldin.")
print("Görevin hazineyi bulmak. Başlıyoruz!") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

s1 = input("Bir yol ayrımındasın. Gidebileceğin yalnızca iki yön var. Birini seç: sağ veya sol. ")
if s1 == "sol":
  s2 = input("Karşına bir göl çıktı. Gölün ortasındaki adada hazine kutusu görüyorsun. Yüzerek karşıya mı geçeceksin yoksa tekne mi bekleyeceksin? beklerim veya yüzerim şeklinde cevap yazmalısın. ")
  if s2 == "beklerim":
    s3 = input("Son aşamaya geldin. Dikkatli karar ver ki hazineye ulaşasın. Karşında üç kapı var. Hangi renkli olanı seçeceksin? kırmızı, mavi veya yeşil. ")
    if s3 == "kırmızı":
      print("Kızıl alevlerin içerisinde yanarak can verdin. Her şey buraya kadarmış.")
    elif s3 == "mavi":
      s4 = input("Evet!! Orada. Git ve hediyeni al. Oha! Yarın unutacağın bu oyunda sadece sanal dünyada geçerli 1 milyon dolar çeki. Hayatın kurtuldu!")
    if s3 == "yeşil":
      print("Kocaman siyah kürklü, kurtadamdan bozma bir canavarın saldırısına uğradın. Tanınmayacak haldesin. Geçmiş olsun.")
      
  if s1 == "yüzerim":
    print("Bilmediğin göllerde yüzmemelisin. Timsah saldırısına uğradın ve acı bir şekilde katledildin.")
else:
  print("Upss. Yapraklarla örtülü bir çukuru fark edemedin ve kuyuya çok sert bir şekilde düştün. Ne yazık ki yardımdan çok uzak bir noktadasın. Tek yapman gereken yardım gelmesini ummak. Oyun biti.")