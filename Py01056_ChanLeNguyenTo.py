import math

def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def sums(s):
    n = len(s)
    sum = 0
    for i in range(0, n):
        sum += int(s[i])
    return sum
    
def check(s):
    n = len(s)
    ok = 0
    for i in range(0, n):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                ok = 1
                return 0
        else:
            if int(s[i]) % 2 != 1:
                ok = 1
                return 0
    if ok == 0 and prime(int(sums(s))): 
        return 1

test = int(input())
for t in range(test):
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")