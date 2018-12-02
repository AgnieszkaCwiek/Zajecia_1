from zajecia2_zad3 import lista_dzielnikow


def pierwsza(n):
    return lista_dzielnikow(n) == [1, n]


if __name__ == '__main__':

    if pierwsza(24):
        print("Liczba jest pierwsza.")
    else:
        print("Liczba nie jest pierwsza.")
