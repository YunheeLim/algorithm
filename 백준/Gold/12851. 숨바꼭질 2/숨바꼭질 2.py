from collections import deque

MAX = 100001

n, k = map(int, input().split())

time = [ 0 ] * (MAX)

cnt, result = 0, 0

q = deque([n])

while q:
    cur = q.popleft()

    if cur == k:
        result = time[cur]
        cnt += 1
        continue

    for i in [cur - 1, cur + 1, cur * 2]:
        if 0 <= i < MAX and (time[i] == 0 or time[i] == time[cur] + 1):
            time[i] = time[cur] + 1
            q.append(i)

print(result)
print(cnt)