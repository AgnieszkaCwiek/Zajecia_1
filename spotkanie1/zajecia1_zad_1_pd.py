def bmi(masa, wzrost):
   bmi = masa/wzrost**2
   return bmi



def komentarz(bmi):
    if bmi < 18.5:
        print("Masz niedowagę")
    elif bmi <= 24.99:
        print("Twoja waga jest w normie")
    else:
        print("Masz nadwagę")

print(bmi(65, 1.70))
komentarz(bmi(65, 1.7))

