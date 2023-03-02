N, K = map(int, input().split())
temp = list(map(int, input().split()))

res = []
res.append(sum(temp[:K]))

for i in range(N-K):
    res.append(res[i] - temp[i] + temp[i+K])

print(max(res))