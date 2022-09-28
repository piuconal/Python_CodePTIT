def check(s):
    n = len(s)
    sum = 0
    for i in range(0, n):
        sum += int(s[i])
    if sum % 3 == 0:
        return 1
    return 0
test = int(input())
for t in range(test):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")