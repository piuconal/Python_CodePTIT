n = int(input())
a = [int(x) for x in input().split()]

cnt = 0
for i in range(1, n):
    ans = (a[i] != a[i - 1])
    if ans == True:
        cnt += 1
print(cnt, end = "\n")