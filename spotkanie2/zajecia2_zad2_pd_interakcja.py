class Error:
    print("Nie podano ruchu")
    pass

def zapalki_uzytkownika():
    zapalki = int(input("Podaj swój ruch: "))
    if zapalki == '':
        raise Error()

    return zapalki
