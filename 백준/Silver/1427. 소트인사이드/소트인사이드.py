n = int(input())
res = []
for i in str(n):
    res.append(i)
res = sorted(res, reverse = True)

for i in res:
    print(i, end="")