import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jew = []
for _ in range(n):
    heapq.heappush(jew, tuple(map(int, input().split())))
# jew = [tuple(map(int, input().split())) for _ in range(n)]

bags = [int(input()) for _ in range(k)]

bags.sort()

# print(jew)
# print(bags)

temp_jew = []
ans = 0

for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(temp_jew, -heapq.heappop(jew)[1])
    if temp_jew:
        ans -= heapq.heappop(temp_jew)
    elif not jew:
        break

print(ans)