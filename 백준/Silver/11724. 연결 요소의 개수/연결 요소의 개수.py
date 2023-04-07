# 백준_연결요소개수
# 무방향 그래프 == 양방향 그래프
def dfs(v):
    visit[v] = True

    for j in graph[v]:
        if not visit[j]:
            dfs(j)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visit = [False]*(N+1)

for i in range(1, N+1):
    if not visit[i]:
        dfs(i)
        cnt += 1

print(cnt)



