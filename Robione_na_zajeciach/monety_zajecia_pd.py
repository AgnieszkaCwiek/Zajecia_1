# zleeeee !!!!
def rozmien(portmonetka, kwota):
    wynik = [0] * len(portmonetka)
    zostalo = kwota
    for nominal in reversed(range(len(portmonetka))):
        if zostalo <= 0:
            break
        if portmonetka[nominal] == 0:
            continue  #doczytac co to robi

        liczba_nominalow = min(zostalo // nominal, portmonetka[nominal])
        zostalo -= liczba_nominalow * nominal
        portmonetka[nominal] -= liczba_nominalow
        wynik[nominal] = liczba_nominalow

    while zostalo > 0:
        if portmonetka == [0] * len(portmonetka):
            break
        for nominal in reversed(range(len(portmonetka))):
            if portmonetka[nominal] > 0:
                zostalo -= nominal
                portmonetka[nominal] -= 1
                wynik[nominal] += 1

    return wynik



print(rozmien([0, 0, 6, 0, 0, 2], 21))
print(rozmien([0, 0, 0, 7, 0, 2], 21))
print(rozmien([0, 2, 0, 0, 0, 5, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10], 123))  #zle to dziala!!!!
