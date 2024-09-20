import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for linked in graph:
    linked.sort()

visited = [0] * (n + 1)

def dfs(start):
    visited[start] = 1
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)
