# Funkcja Ackermanna

def funkcja_ackermanna(m, n):
    if m == 0:
        acker = n + 1
    elif m > 0 and n == 0:
        acker = funkcja_ackermanna(m - 1, 1)
    elif m > 0 and n > 0:
        acker = funkcja_ackermanna(m - 1, funkcja_ackermanna(m, n - 1))

    return acker

print(funkcja_ackermanna(3, 3))