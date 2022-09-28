a = int(input())
test = 0
while(test < a):
    test += 1
    s = input()
    s1 = ""
    s2 = ""
    s1 = s[0] + s[1]
    s2 = s[len(s) - 2] + s[len(s) - 1]
    if(s1 == s2):
        print("YES")
    else:
        print("NO")