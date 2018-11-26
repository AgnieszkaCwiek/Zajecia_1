def rozmien(portfel, kwota):
    wynik = [0] * len(portfel)
    for index in range(len(portfel)):
        nominal = len(portfel) - index - 1
        if nominal == 0:
            break
        ilosc = portfel[nominal]
        ile_potrzeba = kwota // nominal
        if ile_potrzeba > ilosc:
            wynik[nominal] = ilosc
            kwota -= nominal * ilosc
        else:
            wynik[nominal] = ile_potrzeba
            kwota -= nominal * ile_potrzeba
    if kwota > 0:
        for nominal in range(len(portfel)):
            if portfel[nominal] - wynik[nominal] > 0:
                wynik[nominal] += 1
                kwota -= nominal
            if kwota <= 0:
                break
    return wynik


print(rozmien([0, 0, 6, 0, 0, 2], 21))
print(rozmien([0, 0, 0, 7, 0, 2], 21)) # czy wazniejsza ilosc czy precyzyjnosc?

