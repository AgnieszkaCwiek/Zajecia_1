import csv


def wartosc_akcji():
    posiadane_akcje = {
        'Agora SA': 5,
        'Alchemia SA': 155
    }
    kwota = 0
    with open('spolki.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] in posiadane_akcje:
                kwota += float(row[1]) * posiadane_akcje[row[0]]
    return kwota


print(wartosc_akcji())