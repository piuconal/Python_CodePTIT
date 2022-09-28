def multi(s):
    n = len(s)
    mul = 1
    for i in range(0, n):
        if int(s[i]) != 0:
            mul *= int(s[i])
    return mul
test = int(input())
for t in range(test):
    s = input()
    print(multi(s))