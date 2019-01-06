def klasyfikator(napis):
    for slowo in napis.split():
        if len(slowo) <= 5:
            print("+" + " " + slowo)
        else:
            print("-" + " " + slowo)

klasyfikator("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

def klasyfikator1(napis):
    for slowo in napis.split():
        print(slowo)

klasyfikator1("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")