from random import randint

from zajecia2_zad2_pd_interakcja import zapalki_uzytkownika


def pan_madry_komputer(ilosc_zapalek):
    if ilosc_zapalek % 4 == 2:
        return 1
    if ilosc_zapalek % 4 == 3:
        return 2
    if ilosc_zapalek % 4 == 0:
        return 3
    return 1


def zapalki():
    ilosc_zapalek = randint(7, 20)
    tura_uzytkownika = True
    print("Startujemy z {} zapałkami".format(ilosc_zapalek))

    while ilosc_zapalek > 1:
        ilosc_zapalek -= zapalki_uzytkownika()
        print("Zostało {} zapałek".format(ilosc_zapalek))
        tura_uzytkownika = False

        if ilosc_zapalek == 1:
            break

        komputer_wzial = pan_madry_komputer(ilosc_zapalek)
        print("Komputer wziął {} zapałek".format(komputer_wzial))
        tura_uzytkownika = True

        ilosc_zapalek -= komputer_wzial

        print("Zostało {} zapałek".format(ilosc_zapalek))

    if tura_uzytkownika:
        print("Komputer wygrał")
    else:
        print("Wygrałeś!!!")

zapalki()