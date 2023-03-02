N = int(input())
num = list(map(int, input().split()))
res = [1]    # 각 증감의 길이 저장 공간
cnt = 1     # 각 증감을 셀 변수
for i in range(N-1):            # 두개씩 비교를 위해 범위 조정(-1)
    if num[i] <= num[i+1]:      # 만약 다음 인덱스 값이 같거나 크다면
        cnt += 1                # 카운트 1 증가
    else:                       # 아니라면  
        cnt = 1                 # cnt는 새롭게 새야하기때문에 초기화(중요)
    res.append(cnt)
cnt = 1
for i in range(N-1):
    if num[i] >= num[i+1]:
        cnt += 1
    else:
        cnt = 1
    res.append(cnt)

print(max(res))