# 백준 10157
# 자리 배정

C, R = map(int, input().split(" "))
K = int(input())

# 탐색 방향
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visit = [[False for _ in range(C)] for _ in range(R)]

cnt = 1  # 대기번호 1번 부터 시작
x, y = 0, 0
way = 0     # 방향 인덱스
while True:
    if K > C * R:   # K의 대기번호표가 공연장 인원 초과일 때
        print(0)
        break
    if cnt == K:
        print(y+1, x+1)
        break
    visit[x][y] = True

    # 네가지 방향을 탐색하는 것이 아니라 한가지 방향을 설정하고 끝까지 가기....
    dx, dy = delta[way]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < R and 0 <= ny < C:
        if not visit[nx][ny]:
            x = nx
            y = ny
            cnt += 1
        else:
            way = (way + 1) % 4
    else:
        way = (way+1) % 4

