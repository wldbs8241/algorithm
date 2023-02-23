std = []
for i in range(1, 31):
    std.append(i)

arr = []
for _ in range(28):
    arr.append(int(input()))

for num in arr:
    if num in std:
        std.remove(num)

print(*std, sep='\n')