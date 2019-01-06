

def statystyka(nazwa_pliku):
    with open(nazwa_pliku) as file:
        tekst = file.read()
        liczba_znakow = len(tekst)
        slowa = tekst.split(' ')
        liczba_slow = len(slowa)
        liczba_zdan = len([character for character in tekst if character in '.?!'])

    return liczba_znakow, liczba_slow, liczba_zdan


print(statystyka('re'))