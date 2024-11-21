import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0

def dfs(x):
    global ans
    visited[x] = ans

    for i in graph[x]:
        if not visited[i]:
            dfs(i)

for i in range(1, n + 1):
    if not visited[i]:
        ans += 1
        dfs(i)
        
print(ans)