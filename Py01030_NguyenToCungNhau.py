import math

n, k = [int(x) for x in input().split()]
cnt = 0
if k == 2:
    for i in range(10, 100):
        if math.gcd(i, n) == 1:
            cnt += 1
            print(i, end = " ")
            if cnt % 10 == 0:
                print()
elif k == 3:
    for i in range(100, 1000):
        if math.gcd(i, n) == 1:
            cnt += 1
            print(i, end = " ")
            if cnt % 10 == 0:
                print()

elif k == 4:
    for i in range(1000, 10000):
        if math.gcd(i, n) == 1:
            cnt += 1
            print(i, end = " ")
            if cnt % 10 == 0:
                print()

elif k == 5:
    for i in range(10000, 100000): 
        if math.gcd(i, n) == 1:
            cnt += 1
            print(i, end = " ")
            if cnt % 10 == 0:
                print()      