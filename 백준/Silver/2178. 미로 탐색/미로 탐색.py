
# 미로
# 1 : 이동가능한 길

# bfs 함수 생성
def bfs(i, j):          # 인덱스 좌표를 인자로 받는 bfs
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = [[i, j]]        # 받아온 인자를 큐에 삽입한 상태로 큐 생성(따로 만들기 가능)

    while queue:                # 큐가 차있는 동안
        i, j = queue.pop(0)     # i,j 세트로-> 디큐
        for x, y in delta:      # 델타 탐색
            dx = i + x
            dy = j + y
            if 0 <= dx < N and 0 <= dy < M:     # 배열 범위를 넘지 않는 범위 내에서
                if maze[dx][dy] == 1:           # 현재 위치를 기준으로 델타 탐색하면서 1을 만나게 되면
                    maze[dx][dy] = maze[i][j]+1     # 현재 위치의 값 +1(나중에 최단거리 구하는데 사용) 
                    queue.append([dx, dy])          # 탐색에 성공한 좌표-> 인큐
                else:
                    continue
            else:
                continue

    return maze[N-1][M-1]       # 큐가 비었을 때 while문이 종료됨으로 그때의 탈출좌표 반환

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

print(bfs(0,0))     # 시작점 넣은 상태로 시작
