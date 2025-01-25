import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
arr = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1 
answer = 4

def check():

    for num in range(n):
        x, y = 0, num
        while x < h:
            if arr[x][y]:
                y += 1
            elif y > 0 and arr[x][y - 1]:
                y -= 1
            x += 1
        if num != y:
            return False
    return True

def dfs(cnt, x, y):
    global answer
    
    if check():
        answer = min(answer, cnt)
        return
    
    elif cnt == 3 or answer <= cnt:
        return
    
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
        
        for j in range(now, n - 1):
            if not arr[i][j] and not arr[i][j + 1]: # 오른쪽에 사다리가 없는 경우
                if j > 0 and arr[i][j - 1]: # 왼쪽에 사다리가 있으면 패스
                    continue
                arr[i][j] = 1
                dfs(cnt + 1, i, j + 2) # 사다리 겹치지 않도록 j+2
                arr[i][j] = 0
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
