a = int(input())
test = 0
while (test < a):
    test += 1
    n = input()
    ans = str(n)
    if ans[len(ans) - 2] == '8' and ans[len(ans) - 1] == '6':
        print("YES")
    else:
        print("NO")