test = int(input())
for t in range(test):
    s = input()
    n = len(s)
    sum_le = 0
    mul_chan = 1
    for i in range(0, n):
        if i % 2 == 1:
            sum_le += int(s[i])
        else:
            if int(s[i]) != 0:
                mul_chan *= int(s[i])
    print(mul_chan, end = " ")
    print(sum_le)