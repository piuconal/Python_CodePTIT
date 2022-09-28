def check(s):
    n = len(s)
    if n % 2 == 0:
        return 0

    tmp = (int(s[0]) == int(s[1]))
    if tmp == True:
        return 0

    ok = 0
    for i in range(2, n + 1, 2):
        tmp2 = (int(s[i]) != int(s[i - 2]))
        if tmp2 == True:
            ok = 1
            return 0
    if ok == 0: 
        return 1

test = int(input())
for t in range(test):
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")