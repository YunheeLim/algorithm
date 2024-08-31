import heapq
import sys
sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())

graph = [[] for _ in range(100001)]
distance = [INF] * 100001

graph[0].append((1, 1))
graph[100000].append((99999, 1))

for i in range(1, 100000):
    graph[i].append((i - 1, 1))
    graph[i].append((i + 1, 1))

    if 2 * i <= 100000:
        graph[i].append((2 * i, 0))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(n)

print(distance[k])