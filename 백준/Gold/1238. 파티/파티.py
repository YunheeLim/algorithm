import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [int(1e9)] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

total_distance = [0] * (n + 1)

# 갈때
for i in range(1, n + 1):
    dijkstra(i)
    total_distance[i] += distance[x]
    distance = [int(1e9)] * (n + 1)

# 올 때
for i in range(1, n + 1):
    dijkstra(x)
    total_distance[i] += distance[i]
    distance = [int(1e9)] * (n + 1)

# print(distance)
print(max(total_distance))