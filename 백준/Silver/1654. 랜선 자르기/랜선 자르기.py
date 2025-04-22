import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

start, end = 1, max(lines)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        total += line // mid
    if total >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)