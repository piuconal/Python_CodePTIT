def check(n):
    n = str(n)
    x = n
    x = x[::-1]
    if (x != n):            return False
    if(len(n) % 2 == 1):    return False
    for i in n: 
        if (i !='0' and i!='2' and i!='4' and i!='6' and i!='8'):
            return False
    return True

a = int(input())
test = 0
while(test < a):
    test += 1
    n = int(input())
    for i in range(22, n):
        if check(i):
            print(i, end = " ")
    print()