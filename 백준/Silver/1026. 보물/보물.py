# 1026.보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0

for _ in range(N):
    a, b = min(A), max(B)
    res += a*b
    B.remove(b)
    A.remove(a)

print(res)