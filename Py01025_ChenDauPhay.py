s = input()
n = len(s)
ans = ""
if n % 3 == 1:
    ans += s[0] + ","
    for i in range(1, n):
        if i % 3 == 0:
            ans += s[i] + ","
        else:
            ans += s[i]
elif n % 3 == 2:
    ans += s[0] + s[1] + ","
    for i in range(2, n):
        if i % 3 == 1:
            ans += s[i] + ","
        else:
            ans += s[i]
else:
    ans += s[0] + s[1] + s[2] + ","
    for i in range(3, n):
        if i % 3 == 2:
            ans += s[i] + ","
        else:
            ans += s[i]
for i in range(0, len(ans) - 1):
    print(ans[i], end = "")
