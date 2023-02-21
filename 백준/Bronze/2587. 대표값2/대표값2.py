# 평균과 중앙값을 구해보자
num = []
n_sum = 0
for _ in range(5):
    num.append(int(input()))

for i in num:
    n_sum = n_sum + i

for i in range(len(num)-1, 0, -1):
    for j in range(i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

avg = int(n_sum / len(num))
mid = (len(num)//2)

print(avg)
print(num[mid])