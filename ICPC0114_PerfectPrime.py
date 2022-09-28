import math

def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    n = len(s)
    s1 = s[::-1]
    sum = 0
    for i in range(0, n):
        sum += int(s[i])
    ok = 0
    if prime(int(s)) and prime(int(s1)) and prime(sum):
        for i in range(0, n):
            if prime(int(s[i])) == 0:
                ok = 1
                return 0
        if ok == 0:
            return 1
for t in range(int(input())):
    s = input()
    if check(s):
        print("Yes")
    else:
        print("No")
