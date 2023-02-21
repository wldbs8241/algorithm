# 나이순 정렬
arr = []

N = int(input())
for _ in range(N):
    age, name = list(map(str, input().split()))
    arr.append([int(age), name])

arr.sort(key = lambda x : x[0])
for i in range(N):
    print(arr[i][0], arr[i][1])