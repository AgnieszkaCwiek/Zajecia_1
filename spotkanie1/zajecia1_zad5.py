class NotListError(Exception):
    print("Podany argument nie jest listą")
    pass

def vat_faktura(lista):
    if type(lista) != type([]):
        raise NotListError()

    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23 * suma, 2)
    return vat

#zakupy = [0.2, 0.5, 4.59, 6]
#print(vat_faktura(zakupy))

"""def vat_paragon(lista):
    vat = 0
    for element in lista:
        vat = round(vat + element * 0.23, 2)

    return vat"""


vat_faktura("ww")
