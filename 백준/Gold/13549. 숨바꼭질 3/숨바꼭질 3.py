from collections import deque

MAX = 100001

n, k = map(int, input().split())
time = [ 0 ] * (MAX)
q = deque([n])

# 너비 우선 탐색
def bfs(cur, k):
    q = deque()
    if cur == 0:
        q.append(1)
    else:
        q.append(cur)

    while q:
        cur = q.popleft()

        # 동생을 찾았을 때
        if cur == k:
            return time[cur]
            
        # 3가지 방법 탐색
        for i in [cur * 2, cur - 1, cur + 1]:
            # 범위 안에 있고 방문하지 않았거나 다음 방문이 현재 + 1일 때
            if 0 <= i < MAX and time[i] == 0:
                if i == cur * 2:
                    time[i] = time[cur]
                    q.appendleft(i)
                else:
                    time[i] = time[cur] + 1
                    q.append(i)

# 결과 출력
if n == 0:
    if k == 0:
        print(0)
    else:
        print(bfs(n, k) + 1)
else:
    print(bfs(n, k))
