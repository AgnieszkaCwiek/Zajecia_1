

a = [x * x for x in range(4)]
b = [x * x * x for x in range(4) if x * x % 3 == 0]
c = [x.lower() for x in "LOREM IPSUM DOLOR".split()]
d = sum([x * x * 4 for x in range(4) if x * x % 3 == 0])

print(a)
print(b)
print(c)
print(d)