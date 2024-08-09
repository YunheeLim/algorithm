from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

for neighbors in graph:
    neighbors.sort()

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        val = queue.popleft()
        print(val, end=' ')

        for neighbor in graph[val]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                


dfs(v)
print()

visited = [False] * (n + 1)

bfs(v)
