import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

parent = [i for i in range(v + 1)]

edges.sort()

def find_parent(x):
    if x != parent[x]:
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

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost

print(answer)