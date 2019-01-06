from Robione_na_zajeciach import zapalki_komputer_zajecia

stan_gry = 10

gracz = 0

def ruch_gracza(stan_gry):
    print(f"Na stole jest {stan_gry} zapałek")
    ruch = int(input("Podaj liczbę zapałek "))
    return ruch

print(f"Zaczynamy. Jest {stan_gry} zapałek")
while stan_gry > 0:
    if gracz == 0:
        ruch = zapalki_komputer_zajecia.strategia(stan_gry)
    else:
        ruch = ruch_gracza(stan_gry)
    stan_gry -= ruch
    print(f"Wzięto {ruch} zapałek. Zostało {stan_gry}")
    gracz = 1 - gracz


