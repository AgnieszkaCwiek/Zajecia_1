class Wyrazenie:
    pass


class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return stan[self.nazwa]


class Dodawanie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " + " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) + self.prawy.oblicz(stan)

    def uprosc(self):
        if isinstance(self.lewy, Stala) and isinstance(self.prawy, Stala):
            return self.oblicz(None)


class Mnozenie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " * " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) * self.prawy.oblicz(stan)


class Stala(Wyrazenie):

    def __init__(self, stala):
        self.stala = stala

    def __str__(self):
        return self.stala

    def oblicz(self, stan):
        return self.stala






wyrazenie = Dodawanie(Dodawanie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
print(wyrazenie)
stan = {'x': 1, 'y': 2, 'z': 3}
print(wyrazenie.oblicz(stan))
print("{0} = {1}".format(wyrazenie, wyrazenie.oblicz(stan)))

w = Dodawanie(Stala(4), Stala(6))
nowe = w.uprosc()
print(nowe)