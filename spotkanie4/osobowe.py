class Osoba:

    def __init__(self, imie, nazwisko, masa, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.masa = masa
        self.wzrost = wzrost

    def __str__(self):
        return self.__class__.__name__ + ": " + self.imie + " " + self.nazwisko

    def bmi(self):
        return self.masa // self.wzrost ** 2

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja, masa, wzrost):
        Osoba.__init__(self, imie, nazwisko, masa, wzrost)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2

class Kierownik(Pracownik):
    """
    def __init__(self, imie, nazwisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, pensja)
    """

    def wyplata(self):
        return super().wyplata() + 1200.0


o = Osoba("Jan",  "Kowalski", 70, 1.80)
print(o)

p = Pracownik("Jan", "Nowak", 2250, 55, 1.60)

print("{0} wypłata {1}".format(p, p.wyplata()))

k = Kierownik("Anna", "", 5000, 80, 1.70)
print(k.wyplata())

pr = Kierownik("Jan", "Kowalski", 2250, 90, 1.80)

print(pr.bmi())
print(o.bmi())

