def piramida(n):
    for i in range(n):                               #range n to jest od 0 do n-1 !!!
        print(" " * (n-i) + "#" * (2 * i + 1))

piramida(5)
