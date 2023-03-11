import csv
from datetime import datetime

#################################################################
#PİZZA BÖLÜMÜ

class Pizza:
    def __init__(self):
        self.description = " "
        self.price = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.price = 25.0

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.price = 20.0

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.price = 30.0

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Dominos Pizza"
        self.price = 35.0

#################################################################
#SOS BÖLÜMÜ

class Sos(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class ZeytinSosu(Sos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin Sosu"
        self.price = 4.0


class MantarSos(Sos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar Sos"
        self.price = 5.0


class Keci_PeyniriSos(Sos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri Sosu"
        self.price = 1.0


class EtSos(Sos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et Sosu"
        self.price = 9.0


class SoganSos(Sos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan Sosu"
        self.price = 7.0


class MisirSos(Sos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır Sosu"
        self.price = 6.0

#################################################################
#SİPARİŞ BÖLÜMÜ

class Siparis:
    def __init__(self):
        self.pizza = None
        self.sos = None
        self.isim = ""
        self.tcno = ""
        self.odeme_yontemi = ""
        self.credit_card_number = ""
        self.credit_card_password = ""

    def set_pizza(self, pizza):
        self.pizza = pizza

    def set_sos(self, sos):
        self.sos = sos

    def set_isim(self, isim):
        self.isim = isim

    def set_tcno(self, tcno):
        self.tcno = tcno

    def set_odeme_yontemi(self, odeme_yontemi):
        self.odeme_yontemi = odeme_yontemi

    def set_credit_card_number(self, credit_card_number):
        self.credit_card_number = credit_card_number

    def set_credit_card_password(self, credit_card_password):
        self.credit_card_password = credit_card_password

    def kaydet(self):
        headers = ["Tarih", "Urun", "Tutar(TL)", "Adet", "Toplam Tutar"]
        with open("Orders_Database.csv", mode="a", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["SIPARIS***", "TUTAR***", "AD***", "TC***", "ODEME YONTEMI***", datetime.now()])
            writer.writerow([
                self.pizza.get_description() + " + " + self.sos.get_description(),
                self.pizza.get_cost() + self.sos.get_cost(),
                self.isim,
                self.tcno,
                self.odeme_yontemi,
                self.credit_card_number,
                self.credit_card_password])

#################################################################
#MAIN

def main():
    with open('Menu_1.txt', 'r',encoding="utf-8") as f:
        menu_items = f.readlines()
    for item in menu_items:
        print(item.strip())
    while True:
        print("********* PİZZA SEÇİNİZ *********")
        pizza_secimi = input("Pizza seçiminiz (1-4): ")

        if pizza_secimi == "1":
            pizza = KlasikPizza()
        elif pizza_secimi == "2":
            pizza = MargheritaPizza()
        elif pizza_secimi == "3":
            pizza = TurkPizza()
        elif pizza_secimi == "4":
            pizza = DominosPizza()

        else:
            print("Geçersiz seçim!")
            continue

        while True:
            print("********* SOS SEÇİNİZ *********")
            sos_secimi = input("Sos seçiminiz (1-6): ")
            if sos_secimi == "1":
                sos = ZeytinSosu(pizza)
            elif sos_secimi == "2":
                sos = MantarSos(pizza)
            elif sos_secimi == "3":
                sos = Keci_PeyniriSos(pizza)
            elif sos_secimi == "4":
                sos = EtSos(pizza)
            elif sos_secimi == "5":
                sos = SoganSos(pizza)
            elif sos_secimi == "6":
                sos = MisirSos(pizza)
            else:
                print("Geçersiz seçim!")
                continue

            break

        print(pizza.get_description() + " + " + sos.description + "\n")
        print("TOPLAM: {}$\n".format(pizza.get_cost() + sos.get_cost()))




        while True:
            isim = input("İsminizi girin: ")
            if isim.isalpha():
                print()
            else:
                print("Lütfen sayı yazmayın.")
                continue
            break

        while True:
            tcno = input("TC numaranızı girin: ")
            if tcno.isdigit() and len(tcno) == 11:
                print()
            else:
                print("Lütfen geçerli bir tc numarası girin. TC numarası sadece rakamlardan oluşmalı ve 11 haneli olmalıdır.")
                continue
            break

        while True:
            odeme_yontemi = input("Ödeme yönteminizi girin (nakit/kredi kartı): ")
            if str(odeme_yontemi) == "kredi kartı":

                while True:
                    credit_card_number = input("Lütfen kredi kartı numaranızı girin: ")
                    if credit_card_number.isdigit() and len(credit_card_number) == 16:
                        print()
                    else:
                        print("Lütfen geçerli bir 16 haneli kredi kartı numarası girin.")
                        continue
                    break


                credit_card_password = input("Lütfen şifrenizi giriniz: ")



            if odeme_yontemi not in ["nakit", "kredi kartı"]:
                print("Geçersiz ödeme yöntemi!")
                continue
            break






        siparis = Siparis()
        siparis.set_pizza(pizza)
        siparis.set_sos(sos)
        siparis.set_isim(isim)
        siparis.set_tcno(tcno)

        if str(odeme_yontemi) == "kredi kartı":
            siparis.set_credit_card_number(credit_card_number)
            siparis.set_credit_card_password(credit_card_password)
            siparis.set_odeme_yontemi(odeme_yontemi)
        elif str(odeme_yontemi) == "nakit":
            siparis.set_odeme_yontemi(odeme_yontemi)

        siparis.kaydet()

        print()
        print("Siparişiniz kaydedildi.")

        print()
        cevap = input("Yeni bir sipariş vermek istiyor musunuz? (e/h): ")
        if cevap.lower() != "e":
            break


if __name__ == "__main__":
    main()

#################################################################