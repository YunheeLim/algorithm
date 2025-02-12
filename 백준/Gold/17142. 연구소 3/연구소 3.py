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
            virus.append((i, j))  # 바이러스 위치 저장

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = int(1e9)

def bfs(combi):
    visited = [[-1] * n for _ in range(n)]  # 방문 여부
    q = deque()
    
    for x, y in combi:  # 활성 바이러스 배치
        visited[x][y] = 0
        q.append((x, y))
    
    max_time = 0
    empty_cells = sum(row.count(0) for row in arr)  # 전체 빈 공간 개수
    filled = 0  # 확산된 빈 공간 개수

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:  # 빈 공간
                    visited[nx][ny] = visited[x][y] + 1
                    max_time = max(max_time, visited[nx][ny])
                    filled += 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 2:  # 비활성 바이러스도 확산 가능
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    # 모든 빈 칸을 채웠을 경우만 시간 업데이트
    if filled == empty_cells:
        return max_time
    return int(1e9)

def dfs(idx, cnt, combi):
    global ans
    if cnt == m:
        time = bfs(combi)  # BFS 실행 후 최소 시간 확인
        ans = min(ans, time)
        return
    
    for i in range(idx, len(virus)):
        combi.append(virus[i])
        dfs(i + 1, cnt + 1, combi)
        combi.pop()  # 백트래킹

dfs(0, 0, [])

# 정답 출력
print(ans if ans != int(1e9) else -1)
