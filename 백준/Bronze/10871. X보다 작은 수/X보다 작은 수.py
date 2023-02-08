N, X = map(int, input().split())
N_list = list(map(int, input().split()))
result = []
for i in N_list:
    if i < X:
        result.append(i)
print(*result)