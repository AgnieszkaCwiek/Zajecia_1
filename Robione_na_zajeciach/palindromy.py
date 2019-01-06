#czytane od przodu sa takie same jak od tylu

def wer1(slowo):
    for i in range(len(slowo)):
        if slowo[i] != slowo[-1 - i]:
            return False
    return True

def wer2(slowo):
    return slowo == slowo[:: -1] # odwracanie slow !!!

# dziala dla list tez
dane = ['kajak', 'kobylamamalybok', 'palindrom', [1, 2, 1], [2, 1, 3]]
wersje = [wer1, wer2]

for funkcja in wersje:
    for slowo in dane:
        print("{0} : {1}".format(slowo, wer1(slowo)))