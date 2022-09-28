import math

nt=[1]*(2*10**6 + 1)
def prime():
    for i in range(1, 2000000+1):
        nt[i] = i
    for i in range(2, math.isqrt(2000000)+1):
        if(nt[i] == i):
            for j in range(i*i, 2000000+1, i):
                if(nt[j] == j):
                    nt[j] = i
prime()
sum = 0
for t in range(int(input())):
    t -= 1
    n = int(input())
    while(n != 1):
        tmp = nt[n]
        while n % tmp == 0:
            sum += tmp
            n //= tmp
print(sum)
