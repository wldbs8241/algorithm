# 3개의 수를 입력받아 두번째로 큰 수 구하기
num = list(map(int, input().split()))
num.sort()
print(num[1])