n = int(input())
test = 0
while(test < n):
    test += 1
    x = input()
    cnt = 0
    for i in x:
        if i == '4' or i == '7':
            cnt += 1
    if cnt == len(x):
        print("YES")
    else:
        print("NO")