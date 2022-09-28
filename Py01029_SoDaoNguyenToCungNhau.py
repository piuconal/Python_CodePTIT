import math

test = int(input())
for i in range(test):
    s1 = input()
    s2 = s1[::-1]
    n1 = int(s1)
    n2 = int(s2)
    if math.gcd(n1, n2) == 1:
        print("YES")
    else:
        print("NO")