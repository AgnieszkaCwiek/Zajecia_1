import random

def strategia(stan_gry):
    """To jest prosta strategia"""
    ruch = min(stan_gry, random.randint(1, 3))
    return ruch

# jak sobie w konsoli zaimportuje ten plik pythonowy i potem dam help(zajecia_komputer_zajecia.strategia) to mi to wyrzuci