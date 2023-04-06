# 2606 바이러스
def dfs(graph, v, visit):
    global cnt
    visit[v] = True

    for j in graph[v]:
        if not visit[j]:
            cnt += 1
            dfs(graph, j, visit)


num = int(input())
E = int(input())
graph = [[] for _ in range(num+1)]
for i in range(E):
    a, b = map(int, input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향

visit = [False]*(num+1)
cnt = 0
dfs(graph, 1, visit)

print(cnt)