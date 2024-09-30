import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(pair):
    a, b = map(int, input().split())
    if a < b:
        graph[a].append(b)
        graph[b].append(a)
    else:
        graph[b].append(a)
        graph[a].append(b)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(visited.count(True) - 1)