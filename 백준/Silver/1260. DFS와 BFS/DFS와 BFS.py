from collections import deque

# Read input
n, m, v = map(int, input().split())

# Initialize adjacency list
graph = [[] for _ in range(n + 1)]

# Build the graph
for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

# Sort adjacency list for each node to ensure correct DFS/BFS order
for neighbors in graph:
    neighbors.sort()

# Initialize visited list
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

# Perform DFS
dfs(v)
print()

# Reset visited list for BFS
visited = [False] * (n + 1)

# Perform BFS
bfs(v)
