N = int(input())
room = [list(map(str, input())) for _ in range(N)]

row = 0
col = 0

# 가로로 누울 수 있는 자리 계산
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == ".":
            cnt += 1
        else:
            if cnt > 1:
                row += 1
            cnt = 0
    if cnt > 1:  # 각 행에 대한 마지막 체크
        row += 1

# 세로로 누울 수 있는 자리 계산
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == ".":
            cnt += 1
        else:
            if cnt > 1:
                col += 1
            cnt = 0
    if cnt > 1:  # 각 열에 대한 마지막 체크
        col += 1

print(row, col)
