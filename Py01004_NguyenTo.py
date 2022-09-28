import math

def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

def solve(a, b):
    cnt = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            cnt += 1
    if cnt == 1:
        return 1
    return 0

a = int(input())
test = 0
while(test < a):
    test += 1
    n = int(input())
    cnt = 0
    for i in range(1, n, 1):
        if solve(i, n) == 1:
            cnt += 1
    if prime(cnt) == 1:
        print("YES")
    else:
        print("NO")
