def check(s):
    n = len(s)
    sum = 0
    for i in range(0, n):
        sum += int(s[i])
    return sum

def check2(s):
    n = len(s)
    ok = 0
    for i in range(0, int(n/2) + 1):
        ans = (s[i] != s[n - i - 1])
        if ans == True:
            ok = 1
            return 0
    if ok == 0:
        return 1
        
test = int(input())
for t in range(test):
    s = input()
    n = len(str(check(s)))
    if n == 1:
        print("NO")
    else:
        if check2(str(check(s))):
            print("YES")
        else:
            print("NO")
        