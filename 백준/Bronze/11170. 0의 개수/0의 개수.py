for t in range(int(input())):
    N, M = map(int, input().split())
    zero = 0

    for i in range(N, M+1):
        for j in str(i):
            if j == '0':
                zero += 1

    print(zero)