class NotIntErr(Exception):
    pass

def silnia(n):
    if type(n) != type(1):
        raise NotIntErr()
    if n < 2:
        return 1
    return n * silnia(n-1)
