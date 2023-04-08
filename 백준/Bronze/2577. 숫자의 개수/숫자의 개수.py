# 백준 2577

A = int(input())
B = int(input())
C = int(input())
n = A*B*C

cnt = [0 for _ in range(10)]

for i in str(n):
    cnt[int(i)] += 1

for j in cnt:
    print(j)