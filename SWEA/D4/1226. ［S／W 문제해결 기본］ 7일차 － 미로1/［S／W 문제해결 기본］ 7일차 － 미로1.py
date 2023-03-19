# 미로1(16*16)
# DFS로 풀어보기

for t in range(1, 11):
    int(input())                                                    # 따로 사용하지 않을 것이기 때문에 그냥 숫자만 입력받고 저장은 X
    maze = [list(map(int, input())) for _ in range(16)]      # 미로 배열 받아오기
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]      # 상하좌우 탐색할 델타리스트 생성
    visit = [[False] * 16 for _ in range(16)]       # 방문 기록 리스트 생성
    stack = []
    res = 0

    for i in range(16):
        for j in range(16):                 # 전체 배열을 돌면서
            if maze[i][j] == 2:             # 2를 찾았을 때
                stack.append((i, j))        # 시작점 좌표를 스택에 넣어준 상태로 스택을 생성

    while stack:                # 스택이 차있는 동안 반복 (스택이 비어있다면 종료)
        ix, iy = stack.pop()    # 스택의 top을 pop해준후 변수로 저장 -> 새로운 탐색 인덱스 기준 위치로 사용
        for x, y in delta:      # 탐색할 방향 설정
            dx = ix + x
            dy = iy + y
            if 0 <= dx < 16 and 0 <= dy < 16:   # 미로 범위를 벗어나지 않고
                if maze[dx][dy] == 0 and visit[dx][dy] == False:           # 상하좌우 탐색 중에 0을 만나면
                    stack.append((dx, dy))      # 스택에 위치를 추가해주고, 해당 탐색 기준 좌표의 방문 기록 남기기
                    visit[ix][iy] = True
                elif maze[dx][dy] == 3:
                    res = 1                     # 종점(3)을 만나게 되면 바로 종료 -> 미로 거리/이동 거리 등 구하지 않아도 되기 때문에 가능 불가능만 반환
                    break



    print(f'#{t} {res}')


