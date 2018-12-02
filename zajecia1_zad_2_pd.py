def rachunek(kwota):
    wynik = {
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }
    nominaly = [20, 10, 5, 2, 1]
    for element in nominaly:
        wynik[element] = kwota // element
        kwota -= (kwota // element) * element

    return wynik


print(rachunek(123))