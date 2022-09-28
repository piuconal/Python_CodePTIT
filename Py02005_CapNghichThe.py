n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if i < j and a[i] > a[j]:
            cnt += 1
print(cnt)