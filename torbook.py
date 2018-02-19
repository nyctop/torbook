import subprocess
subprocess.run("clear", shell=True)
print("""
 /$$$$$$$$                  /$$$$$$$                      /$$      
|__  $$__/                 | $$__  $$                    | $$      
   | $$  /$$$$$$   /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$
   | $$ /$$__  $$ /$$__  $$| $$$$$$$  /$$__  $$ /$$__  $$| $$  /$$/
   | $$| $$  \ $$| $$  \__/| $$__  $$| $$  \ $$| $$  \ $$| $$$$$$/ 
   | $$| $$  | $$| $$      | $$  \ $$| $$  | $$| $$  | $$| $$_  $$ 
   | $$|  $$$$$$/| $$      | $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$
   |__/ \______/ |__/      |_______/  \______/  \______/ |__/  \__/
                                                                   
                    Torbook by Nycto - Version 1.0                 
""")
def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1.Arama Motorları")
    print("2.Marketler")
    print("3.Hosting")
    print("4.Bloglar")
    print("5.Forumlar ve Kanallar")
    print("6.Email ve Mesajlar")
    print("7.Politik")
    print("8.Hacking - Warez")
    print("9.Erotic 18+")
    print("10.Yeni Adres Ekle")
    print("11.Adresleri Güncelle")
    print("12.ÇIKIŞ")
    print(67 * "-")
print_menu()

def eklemenu():
    print("""Hangi Menüye Ekleme Yapmak İstiyorsunuz ?
    1-Arama Motorları
    2-Marketler
    3-Hosting
    4-Bloglar
    5-Forum ve Kanallar
    6-Email ve Mesajlar
    7-Politik
    8-Hacking ve Warezler
    9-Erotik
    """)
while True:
    try:
        secim = int(input("Seçim: [1-12](Geri Gitmek için ('0') / Çıkış için ('12') kullanın:  "))
        if secim == 1:
            subprocess.run("clear", shell=True)
            d1=open("se.txt","r")
            print(d1.read())
            d1.close()
        elif secim == 2:
            subprocess.run("clear", shell=True)
            d2=open("ma.txt","r")
            print(d2.read())
        elif secim == 3:
            subprocess.run("clear", shell=True)
            d3=open("ho.txt","r")
            print(d3.read())
        elif secim == 4:
            subprocess.run("clear", shell=True)
            d4=open("bl.txt","r")
            print(d4.read())
        elif secim == 5:
            subprocess.run("clear", shell=True)
            d5=open("fc.txt","r")
            print(d5.read())
        elif secim == 6:
            subprocess.run("clear", shell=True)
            d6=open("em.txt","r")
            print(d6.read())
        elif secim == 7:
            subprocess.run("clear", shell=True)
            d7=open("po.txt","r")
            print(d7.read())
        elif secim == 8:
            subprocess.run("clear", shell=True)
            d8=open("ha.txt","r")
            print(d8.read())
        elif secim == 9:
            subprocess.run("clear", shell=True)
            d9=open("er.txt","r")
            print(d9.read())
        elif secim == 10:
            subprocess.run("clear", shell=True)
            eklemenu()
            ide = int(input("Hangi Menu:[1-9] "))
            if ide == 1:
                with open("se.txt", "a") as f:
                   f.write(input("Adres:")+"\n")
                   print("Adres Eklendi...")
            elif ide == 2:
                adres = input("Adres:")
                with open("ma.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 3:
                with open("ho.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 4:
                with open("bl.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 5:
                with open("fc.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 6:
                with open("em.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 7:
                with open("po.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 8:
                with open("ha.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
            elif ide == 9:
                with open("er.txt", "a") as f:
                   f.write(input("Adres:") + "\n")
                   print("Adres Eklendi...")
        elif secim == 12:
            subprocess.run("clear", shell=True)
            exit()
        elif secim == 0:
            print_menu()
        elif secim == 11:
            print("Yeni Versiyonda Aktif Olacak.../ Geri Dönmek İçin '0'")
    except ValueError:
        subprocess.run("clear", shell=True)
        print("Sayi Canım..Sayı gir diyoruz!Rakam.12345678910 gibi sayılar..")
        print_menu()

