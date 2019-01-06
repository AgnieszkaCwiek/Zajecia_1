
def zakupy(cennik, lista):
    suma = 0
    for towar in lista:
        if towar in cennik:
            kwota = lista[towar] * cennik[towar]
            suma += kwota
        return suma


cennik = {
    'kawa' : 14.99,
    'pomarancze' : 3.49,
    'olej' : 4.99
}

lista = {'olej' : 2, "kawa" : 1}
print(zakupy(cennik, lista))