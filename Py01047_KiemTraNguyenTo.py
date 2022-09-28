import math

def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

test = int(input())
for t in range(test):
    s = input()
    n = len(s)
    second = s[n - 4] + s[n - 3] + s[n - 2] + s[n - 1]
    if prime(int(second)):
        print("YES")
    else:
        print("NO")
