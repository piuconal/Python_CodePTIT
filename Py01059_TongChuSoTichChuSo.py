test = int(input())
for t in range(test):
    s = input()
    n = len(s)
    sum_chan = 0
    mul_le = 1
    cnt = 0
    for i in range(0, n):
        if i % 2 == 0:
            sum_chan += int(s[i])
        else:
            if int(s[i]) != 0:
                cnt += 1
                mul_le *= int(s[i])
    print(sum_chan, end = " ")
    if cnt == 0:
        print("0")
    else:
        print(mul_le)