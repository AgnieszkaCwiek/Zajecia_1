# sortowanie listy


def sortowanie(lista):
    return sorted(lista)


lista_imion = ["Agnieszka", "Robert", "Emilia", "Artur", "Beata"]


if __name__ == '__main__':
    print(sortowanie(lista_imion))

# liczba imion konczacych sie na litere "a"

def imiona_a(lista):
    ilosc = 0
    for imie in lista:
        if imie[-1] == 'a':  # jest tez funkcja imie.endswith("a") i ona tez by byla ok
            ilosc += 1
    return ilosc

print(imiona_a(lista_imion))

