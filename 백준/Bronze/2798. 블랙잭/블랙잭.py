# 백준 블랙잭
# N장의 카드중 3장의 합이 M을 넘지 않는다.

N, M = map(int, input().split())
num = list(map(int, input().split()))
res = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum3 = num[i]+num[j]+num[k]
            if sum3 <= M:
                res.append(sum3)

print(max(res))