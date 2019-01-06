from spotkanie2.zajecia2_zad4 import pierwsza
from spotkanie2.zajecia2_zad3 import lista_dzielnikow
from spotkanie1.zajecia1_zad6 import suma_dzielnikow

# dzielniki pierwsze

def dzielniki_pierwsze(n):
    dzielniki_pierwsze_lista = []
    for i in lista_dzielnikow(n):
        if pierwsza(i):
            dzielniki_pierwsze_lista.append(i)
    return dzielniki_pierwsze_lista


print(dzielniki_pierwsze(88))


def dzielniki_pierwsze_filter(n):
    # filter "filtruje" listę - zostawia te elementy dla których funkcja zwraca True
    # przyjmuje 2 argumenty - (funkcja, lista)
    return list(filter(pierwsza, lista_dzielnikow(n)))


def dzielniki_pierwsze_list_comprehension(n):
    return [x for x in lista_dzielnikow(n) if pierwsza(x)]


# liczby doskonale

def doskonala(n):
    return n == suma_dzielnikow(n)


if __name__ == '__main__':
    ilosc_doskonalych = 0
    i = 2
    while ilosc_doskonalych != 4:
        if doskonala(i):
            ilosc_doskonalych += 1
            print(i)
        i += 1