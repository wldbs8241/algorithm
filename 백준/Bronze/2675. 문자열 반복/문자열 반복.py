# 백준 2627
# 문자열 반복
for t in range(int(input())):
    res = ''
    num, word = input().split()

    for i in word:
        for j in range(int(num)):
            res += i
    print(res)