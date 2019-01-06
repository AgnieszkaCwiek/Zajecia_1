def podatek(kwota):

    if kwota <= 44490:
        podatek_kwota = 0.19 * kwota
    elif kwota <= 85528:
        podatek_kwota = 0.19 * 44490 + (kwota - 44490) * 0.3
    else:
        podatek_kwota = 0.19 * 44490 + 0.3 * (kwota - 44490 - (kwota - 85528)) + 0.4 * (kwota - 85528)
    return podatek_kwota

print(round(podatek(100000)))
