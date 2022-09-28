for t in range(int(input())):
    s = input()
    n = len(s)
    ok = 0
    for i in range(0, n):
        if s[i] != '2' and s[i] != '1' and s[i] != '0':
            ok = 1
            print("NO")
            break
    if ok == 0:
        print("YES")
        