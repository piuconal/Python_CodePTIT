test = int(input())
for t in range(test):
    n = int(input())
    sum = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            sum += float(1/i)
    else:
        for i in range(1, n + 1, 2):
            sum += float(1/i)
    print("{:.6f}".format(sum))