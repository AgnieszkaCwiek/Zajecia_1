from random import randint

from spotkanie2.zajecia2_zad2_pd_interakcja import zapalki_uzytkownika

#dodać sobie jakas walidacje??  Projektowanie??

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
    print(f"Startujemy z {ilosc_zapalek} zapałkami")

    while ilosc_zapalek > 1:
        ilosc_zapalek -= zapalki_uzytkownika()
        print(f"Zostało {ilosc_zapalek} zapałek")
        tura_uzytkownika = False

        if ilosc_zapalek == 1:
            break

        komputer_wzial = pan_madry_komputer(ilosc_zapalek)
        print(f"Komputer wziął {komputer_wzial} zapałek")
        tura_uzytkownika = True

        ilosc_zapalek -= komputer_wzial

        print(f"Zostało {ilosc_zapalek} zapałek")

    if tura_uzytkownika:
        print("Komputer wygrał")
    else:
        print("Wygrałeś!!!")

zapalki()