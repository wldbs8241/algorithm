# 마그네틱
# 뻘강 : 1, 파랑: 2

for t in range(1, 11):
    int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if arr[j][i] == 1:  # 빨간색(0)을 만나면
                stack.append(arr[j][i])

            elif arr[j][i] == 2 and stack:       # 파란색(1)을 만나면 스택이 차있는지 확인
                stack = []
                cnt += 1


    print(f'#{t} {cnt}')
