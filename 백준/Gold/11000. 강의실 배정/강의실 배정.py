import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
arr = []

for _ in range(N):
    s,e = map(int,input().rstrip().split())
    arr.append((s,e))

arr.sort()
q = [arr[0][1]] # 가장 먼저 끝나는 회의실에 큐를 넣음.

for idx in range(1,N):
    if arr[idx][0] < q[0]: # 다음 회의 시작 시간이 직전 회의 마무리 시간보다 빠르면?
        heapq.heappush(q,arr[idx][1])

    else:
        heapq.heappop(q)
        heapq.heappush(q, arr[idx][1])

print(len(q))