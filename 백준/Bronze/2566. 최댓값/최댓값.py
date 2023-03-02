arr = [list(map(int, input().split())) for _ in range(9)]
max_n = 0
res = []
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_n:
            max_n = arr[i][j]
            res.append([i+1, j+1])

print(max_n)
print(*res[-1])