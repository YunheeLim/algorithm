import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

distance = [int(1e9)] * (n + 1)
prev = [0] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                prev[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])

# 최단경로 역추적
path = []
cur = end
while cur != start:
    path.append(cur)
    cur = prev[cur]
path.append(start)
path.reverse()
print(len(path))
answer =  " ".join(map(str,path))
print(answer)