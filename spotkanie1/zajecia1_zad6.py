def suma_dzielnikow(n):
    suma = 0
    for k in range(1, n):
        modulo = n % k
        if modulo == 0:
            suma = suma + k
    return suma


if __name__ == '__main__':
    print(suma_dzielnikow(28))
