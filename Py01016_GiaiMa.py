t = int(input())
for i in range(t) :
    s = input()
    n = len(s)
    for i in range(0, n, 2):
        for j in range(1, int(s[i + 1]) + 1):
            print(s[i], end="")
    print()