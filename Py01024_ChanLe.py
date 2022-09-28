def sum10(s):
    n = len(s)
    sum = 0
    for i in range(0, ns):
        sum += (ord(s[i]) - 48)
    if sum % 10 == 0:
        return 1
    return 0

test = int(input())
for t in range(test):
    s = input()
    ns = len(s)
    if sum10(s):
        ok = 0
        for i in range(1, ns):
            ans = abs(ord(s[i]) - ord(s[i - 1]))
            if ans != 2:
                ok = 1
                print("NO")
                break
        if ok == 0:
            print("YES")
    else:
        print("NO")