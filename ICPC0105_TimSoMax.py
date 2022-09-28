for i in range(int(input())) :
    s = input()
    s = s + 'z'
    ans = -10 ** 20
    sum = 0
    for i in range(len(s)) :
        if s[i].isalpha() :
            if i != 0 and s[i - 1].isdigit() : 
                ans = max(ans, sum)
            sum = 0
        else : 
            sum = sum * 10 + int(s[i])
    print(ans)