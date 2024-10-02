import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001

n, k = map(int, input().split())
time = [ 0 ] * MAX
order = [ 0 ] * MAX

def print_order(k):
    result = []
    temp = k
    for _ in range(time[k] + 1):
        result.append(temp)
        temp = order[temp]

    print(' '.join(map(str, result[::-1])))

def bfs(cur, k):
    q = deque([cur])

    while q:
        cur = q.popleft()

        if cur == k:
            print(time[k])
            print_order(k)
            return

        for i in [cur - 1, cur + 1, cur * 2]:
            if 0 <= i < MAX and time[i] == 0:
                time[i] = time[cur] + 1
                q.append(i)
                order[i] = cur

bfs(n, k)