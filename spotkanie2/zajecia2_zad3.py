def lista_dzielnikow(n):
    dzielniki = []
    suma = 0
    for k in range(1, n + 1):
        modulo = n % k
        if modulo == 0:
            suma = suma + k
            dzielniki.append(k)
    return dzielniki


# Sprawdzanie czy plik jest importowany czy uruchamiany bezposrednio
# (przy imporcie plik jest uruchamiany przez inny plik - nie uruchomi mi sie tam ten tescik ponizej)
if __name__ == '__main__':
    print(lista_dzielnikow(32))


