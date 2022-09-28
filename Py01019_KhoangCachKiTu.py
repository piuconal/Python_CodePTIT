test = int(input())
for t in range(test):
    s1 = input()
    s2 = s1[::-1]
    ns1 = len(s1)
    ok = 0
    for i in range(1, ns1):
        n1 = abs(ord(s1[i]) - ord(s1[i - 1]))
        n2 = abs(ord(s2[i]) - ord(s2[i - 1]))
        if n1 != n2:
            ok = 1
            print("NO")
            break
    if ok == 0: 
        print("YES")