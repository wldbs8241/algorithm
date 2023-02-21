num = []
for _ in range(5):
    num.append(int(input()))
avg = int(sum(num)/len(num))

num.sort()

print(avg)
print(num[2])