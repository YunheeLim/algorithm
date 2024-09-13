import sys
sys.stdin.readline

n, m = map(int, input().split())

# lst = []

# for _ in range(m):
#     a, b = map(int, input().split())
#     if a not in lst:
#         lst.append(a)
#     if b not in lst:
#         lst.append(b)
#     if b in lst:

compare = [[] for _ in range(n + 1)]

arr = [0] * (n + 1)
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    compare[a].append(b)
    if arr[a] >= arr[b]:
        arr[b] = arr[a] + 1
    visited[a] = 1
    visited[b] = 1
    if visited[b]:
        for higher in compare[b]:
            if higher != a:
                arr[higher] += 1

for idx, val in enumerate(arr):
    arr[idx] = (val, idx)

# print(arr)

arr.sort()

for i in range(1, len(arr)):
    if i == len(arr) -1:
        print(arr[i][1])
    else:
        print(arr[i][1], end=' ')
