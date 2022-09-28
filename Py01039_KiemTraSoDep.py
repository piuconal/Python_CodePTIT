test = int(input())
for t in range(test):
    s = input()
    ok = 0
    ns = len(s)
    for i in range(2, ns):
        ans = (s[i - 2] != s[i])
        if ans == True:
            ok = 1
            print("NO")
            break
    if ok == 0:
        print("YES")
    