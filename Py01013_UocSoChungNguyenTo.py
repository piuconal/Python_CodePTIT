import math
def prime(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True 

t = int(input())
for i in range(t) :
    a, b = [int(x) for x in input().split()]
    ans = math.gcd(a, b)
    s = 0
    while ans > 0 :
        s += ans % 10
        ans = int(ans / 10)
    if prime(s) == True :   print("YES")
    else :                  print("NO")