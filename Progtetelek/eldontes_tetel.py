import math

print("\nszám: ")
n = input()
prim = bool
if (n < 2):
    prim = False
else:
    i = 2
    while(i <= math.sqrt(n) and n % i != 0):
        i += 1
    prim = i > math.sqrt(n)
