# 백준_1920
# 수 찾기

# N의 배열과 M의 배열이 주어질 때, M의 요소들이 N에 포함되는지 여부

import sys
input = sys.stdin.readline

N = int(input())
n_num = set(map(int, input().split()))
M = int(input())
m_num = list(map(int, input().split()))

# res = [0 for _ in range(N)]

for i in m_num:
    if i in n_num:
        print(1)
    else:
        print(0)

