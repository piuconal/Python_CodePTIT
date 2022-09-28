def solve(y):
    x = [int(i) for i in y]
    for i in range(len(x) - 1, 0, -1):
        if x[i] >= 5:
            x[i - 1] += 1
        x[i] = 0
    for i in x:
        print(i, end="")  

a = int(input())
test = 0
while(test < a):
    test += 1
    x = input()
    solve(x)
    print()
