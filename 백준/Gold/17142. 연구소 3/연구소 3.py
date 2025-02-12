import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
virus = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(n):
        if row[j] == 2:
            virus.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = int(1e9)

def dfs(idx, cnt, combi):
    global ans
    if cnt == m:
        visited = [[int(1e9)] * n for _ in range(n)]
        max_time = 0
        empty_cells = sum(row.count(0) for row in arr)
        filled = 0
        q = deque()
        # print(combi)
        for x, y in combi:
            visited[x][y] = 0
            q.append((x, y))

        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > visited[x][y] + 1:
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        max_time = max(max_time, visited[nx][ny])
                        filled += 1
                        q.append((nx, ny))
                        
                    elif arr[nx][ny] == 2:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

        # 빈칸 모두 채운 경우에만
        if filled == empty_cells:
            ans = min(ans, max_time)
            return max_time
        
        return int(1e9)
    
    for i in range(idx, len(virus)):
        combi.append(virus[i])
        dfs(i + 1, cnt + 1, combi)
        combi.pop()

dfs(0, 0, [])

# 정답 출력
print(ans if ans != int(1e9) else -1)