# 색종이
# 도화지 내의 색종이의 넓이를 구하기(겹치는 부분 제외)
# 한 구역의 넓이는 == 1 즉 색칠된 위치 개수 cnt해줘도 넓이 구하기 가능

N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for i in range(N):
    x, y = map(int, input().split())
    for xx in range(10):
        for yy in range(10):
            arr[x+xx][y+yy] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)