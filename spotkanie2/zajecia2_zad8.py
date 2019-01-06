import random

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    slowa = tekst.replace('.', '').split(' ')
    for slowo in slowa:
        if len(slowo) > dl_slowa:
            slowa.remove(slowo)
    while len(slowa) > liczba_slow:
        slowa.pop(random.randint(0, len(slowa) - 1))

    return ' '.join(slowa).capitalize() + '.'



tekst = "Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej."

print(uprosc_zdanie(tekst, 10, 5))