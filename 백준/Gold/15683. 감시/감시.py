import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
cctv = []
mode = [
    [], 
    [[0], [1], [2], [3]], 
    [[0, 2], [1, 3]], 
    [[0, 1], [1, 2], [2, 3], [0, 3]], 
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 
    [[0, 1, 2, 3]]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([arr[i][j], i, j])
    
def fill(arr, mode, x, y):
    for i in mode:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = -1

def dfs(depth, arr):
    global minVal

    if depth == len(cctv):
        cnt = sum([arr[i].count(0) for i in range(n)])
        minVal = min(minVal, cnt)
        return

    cctv_num, row, col = cctv[depth]

    for i in mode[cctv_num]:
        temp = copy.deepcopy(arr)
        fill(temp, i, row, col)
        dfs(depth + 1, temp)

minVal = n * m
dfs(0, arr)
print(minVal)

