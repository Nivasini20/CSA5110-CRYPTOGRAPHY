from math import gcd

n = int(input("Enter n: "))
m = int(input("Enter plaintext block: "))

g = gcd(m, n)

if 1 < g < n:
    print("Factor found:", g)
    print("Other factor:", n // g)
else:
    print("No factor found")