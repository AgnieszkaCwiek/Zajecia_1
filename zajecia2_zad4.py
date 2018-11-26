#zad 3

def lista_dzielnikow(n):  #zrobic tu odwolanie do sumy dzielnikow!!! a nie wykorzystac ja 
    dzielniki = []
    suma = 0
    for k in range(1, n):
        modulo = n % k
        if modulo == 0:
            suma = suma + k
            dzielniki.append(k)
    return dzielniki

print(lista_dzielnikow(32))

#zad 4

def pierwsza(n):

        dzielniki = []
        suma = 0
        for k in range(1, n):
            modulo = n % k
            if modulo == 0:
                suma = suma + k
                dzielniki.append(k)

        if dzielniki == [1]:
            print("Liczba jest pierwsza.")
        else:
            print("Liczba nie jest pierwsza.")

pierwsza(23)

#zad 5

def dzielniki_pierwsze(n):

