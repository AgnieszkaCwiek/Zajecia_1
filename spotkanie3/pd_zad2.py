from collections import Counter
import string

def statystyka(plik):
    with open(plik) as file:
        tekst = file.readlines()
        slowa = []
        for line in tekst:
            slowa.extend(line.replace('\n', '').split(' '))
        # statystyki = {x: slowa.count(x) for x in slowa}
        for index, slowo in enumerate(slowa):
            slowa[index] = slowo.strip('.,?!;:()/-').lower()
        statystyki = Counter(slowa)
        del statystyki['']
        del statystyki['/']
        del statystyki['—']
    return statystyki

print(statystyka('hamlet.txt'))
print(statystyka('krol-lear.txt'))
print('#############################')


def porownanie(plik1, plik2, roznica):
    stats1 = statystyka(plik1)
    stats2 = statystyka(plik2)
    a_bez_b = Counter({x: stats1[x] for x in stats1 if x not in stats2})
    b_bez_a = Counter({x: stats2[x] for x in stats2 if x not in stats1})

    roznice = {x for x in stats1 if abs(stats1[x] - stats2[x]) == roznica}
    roznice = roznice.union({x for x in stats2 if abs(stats1[x] - stats2[x]) == roznica})

    return a_bez_b, b_bez_a, roznice


print('\n'.join([str(x) for x in porownanie('hamlet.txt', 'krol-lear.txt', 170)]))