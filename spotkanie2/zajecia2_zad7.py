

def zbuduj_zdania(lista):
    zdania = []
    for wyrazy in lista:
        zdanie = ' '.join(wyrazy) + '.'
        zdania.append(zdanie.capitalize())
    return ' '.join(zdania)

zdanka = [["łódź", "się", "obudziła"], ["ogary", "poszły", "w", "las"]]


print(zbuduj_zdania(zdanka))