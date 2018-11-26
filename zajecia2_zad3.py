def suma_dzielnikow(n):
    dzielniki = []
    suma = 0
    for k in range(1, n):
        modulo = n % k
        if modulo == 0:
            suma = suma + k
            dzielniki.append(k)
    return dzielniki

print(suma_dzielnikow(32))