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
    ok = 0
    for i in range(0, n):
        if prime(i) == 1:
            if prime(int(s[i])) == 0:
                ok = 1
                print("NO")
                break
        else:
            if prime(int(s[i])) == 1:
                ok = 1
                print("NO")
                break
    if ok == 0:
        print("YES")