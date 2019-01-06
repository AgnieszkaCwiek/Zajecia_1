def odsetki(oproc, czas, kwota):

    if czas == 12:  # lokata caloroczna
        odsetki_ost = kwota * oproc * (czas / 12)

    elif czas < 12: # lokata odnawialna
        odsetki_ost = 0
        ilosc_okresow = 12 // czas
        for i in range(ilosc_okresow):  # sprawdzic to jeszcze
            odsetki = kwota * oproc * (czas/12)
            kwota = kwota + odsetki
            odsetki_ost += odsetki


    return odsetki_ost

print(odsetki(0.03, 3, 1000))

print(odsetki(0.03, 12, 1000))



