# 백준 1912
# 연속합

# 10
# 10 -4 3 1 5 6 -35 12 21 -1
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
print(max(dp))