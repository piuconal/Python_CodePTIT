import math

test = int(input())
for t in range(test):
    s1 = input()
    s2 = s1[::-1]
    n1 = len(s1)
    ok = 0
    for i in range(1, n1):
        ans1 = abs((ord(s1[i]) - ord(s1[i - 1])))
        ans2 = abs((ord(s2[i]) - ord(s2[i - 1])))
        res = (ans1 == ans2)
        if res == False:
            ok = 1
            print("NO")
            break
    if ok == 0:
        print("YES") 


