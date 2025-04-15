import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
previous = [-1] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b노드로 가는 비용이 c
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                previous[i[0]] = now # 최단 경로 저장
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])
# print(previous)

path = []
current_node = end
while current_node != -1:
    path.append(current_node)
    current_node = previous[current_node]

path.reverse()

print(len(path))
print(' '.join(map(str, path)))


# # 출발 노드에서 모든 노드들까지 최소거리 출력
# for i in range(1, n+1):
#     if distance[i] == INF: #도달할 수 없는 경우 무한
#         print("INFINITY")
#     else:
#         print(distance[i])