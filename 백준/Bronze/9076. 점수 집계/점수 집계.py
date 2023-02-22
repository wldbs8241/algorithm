import sys
T = int(input())

for t in range(T):
    score = list(map(int, sys.stdin.readline().split()))
    score.sort()
    score.pop(0)
    score.pop()
    if (score[-1] - score[0]) >= 4:
        print('KIN')
    else:
        print(sum(score))