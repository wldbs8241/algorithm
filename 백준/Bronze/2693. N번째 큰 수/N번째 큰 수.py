# N번째 큰 수
# N은 항상 3으로 고정
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()          # 받아온 배열을 정렬 후 인덱스로 n번째 큰 수에 접근 
    print(arr[-3])      # 3번째로 큰 수는 뒤에서 3번째(= -3)