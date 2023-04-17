# [백준]1991. 트리순회

N = int(input())        # 노드의 수
E = N - 1               # 간선의 수
# 굳이 트리가 한 리스트 안에 있을 필요는 없다 -> 딕셔너리로 접근
# tree = [list(input().split()) for _ in range(N+1)]
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

# 전위 순회
def pre_order(node):
    if node != ".":
        print(node, end='')
        pre_order(tree[node][0])    # left
        pre_order(tree[node][1])    # right
# 중위 순회
def in_order(node):
    if node != ".":
        in_order(tree[node][0])    # left
        print(node, end='')
        in_order(tree[node][1])    # right
# 후위 순회
def post_order(node):
    if node != ".":
        post_order(tree[node][0])    # left
        post_order(tree[node][1])    # right
        print(node, end='')



pre_order('A')
print()
in_order('A')
print()
post_order('A')