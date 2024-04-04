print("********************************************"
      " Banka uygulamama hoşgeldiniz la "
      "********************************************")


sabit_kullanici_adi="YUSUF"
sabit_kullanici_şifre="Sertkaya.47"

giriş_hakki=3

bakiye=1000

while True:
    kullanici_adi=input("Kullanıcı adınız nedir")
    kullanici_şifre=input("şifeniz")
    if(kullanici_adi==sabit_kullanici_adi and kullanici_şifre !=sabit_kullanici_şifre):
        print("Şifre yanlış lan")
        giriş_hakki-=1
        print("KAlan Giriş Hakkı :",giriş_hakki)


    elif (kullanici_adi != sabit_kullanici_adi and kullanici_şifre == sabit_kullanici_şifre):
        print("Kullanıcı adı yanlış yanlış lan")
        giriş_hakki-=1
        print("KAlan Giriş Hakkı :",giriş_hakki)



    elif (kullanici_adi != sabit_kullanici_adi and kullanici_şifre != sabit_kullanici_şifre):
        print("Hem kullanıcı ismi hem şifre yanlış lan")
        giriş_hakki-=1
        print("KAlan Giriş Hakkı :",giriş_hakki)




    if (giriş_hakki == 0):
        print("GİRİŞ hakkın kalmadı aptal")
        break


    if(kullanici_adi==sabit_kullanici_adi and kullanici_şifre==sabit_kullanici_şifre):
        print("Başarıyla Giriş yapmışsın aferin moron")

        while True:

            menu = int(input("Para çekmek için 1\n"
                         "Para yatırmak için 2\n"
                         "kredi çekmek için 3\n"
                         "Çıkış için 4 e bas\n"
                         "Seçimini yap:"))

            if (menu == 1):
                Çekilen_para = int(input("ÇEKMEK İSTEDİĞİNİZ MİKTARI SÖYLE LA: "))
                bakiye -= Çekilen_para
                print("Güncel BAkiye", bakiye)


            elif (menu == 2):
                Yatrırlan_para = int(input("YATIRMAK İSTEDİĞİNİZ MİKTARI SÖYLE LA: "))
                bakiye += Yatrırlan_para
                print("Güncel BAkiye", bakiye)



            elif (menu == 3):
                Kredi = int(input("Kredi çekmek istiyorsun ha söyle kredi notun kaç: "))

                if (Kredi > 95):
                    print("Tamam sana Kredi verecez")
                else:
                    print("Yok sana kredi mredi")
            else:
                print("Geçersiz işlem")
                break
            if(menu==4):
                print("bye bye arada gel öyle para kazandır bize")