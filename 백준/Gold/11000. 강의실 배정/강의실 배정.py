import sys
import heapq
input = sys.stdin.readline

n = int(input())
course = [list(map(int, input().split())) for _ in range(n)]
course.sort()
q = [course[0][1]]
for i in range(1, n):
    if course[i][0] >= q[0]: # 회의실 추가 개설
        heapq.heappop(q)
    heapq.heappush(q, course[i][1])

print(len(q))