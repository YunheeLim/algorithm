import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 런타임 에러를 피하기 위해 최대 재귀 깊이 재설정


v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
parent = [i for i in range(v + 1)]
edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost

print(answer)