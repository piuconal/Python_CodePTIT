import math

def prime(a, b):
    if math.gcd(a, b) == 1:
        return 1
    return 0

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        ans = prime(a[i], a[j])
        if ans == True:
            print(a[i], end = " ")
            print(a[j], end = " ")
            print()
