import datetime

# sprawdzanie czy rok jest przestepny:


def przestepny(rok):
    if rok < 1582:
        return False
    return ((rok % 4 == 0) and rok % 100 != 0) or rok % 400 == 0

# sprawdzanie ktore z nadchodzacych lat beda przestepne

def nadchodzace_lp(n):
    wynik = []
    akt_rok = datetime.datetime.now().year
    while len(wynik) < n:
        if przestepny(akt_rok):
            wynik.append(akt_rok)
        akt_rok = akt_rok + 1

    return wynik


print(nadchodzace_lp(4))
