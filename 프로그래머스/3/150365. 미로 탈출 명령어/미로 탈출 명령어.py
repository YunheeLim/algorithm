import sys
sys.setrecursionlimit(10**5)

def solution(n, m, x, y, r, c, k):
    answer = "z"
    
    # 문자열 사전 순으로 빠른 순서
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    dAlpha = ['d', 'l', 'r', 'u']
    
    def dfs(cx, cy, cnt, string):
        nonlocal answer
        if k < cnt + abs(cx - r + 1) + abs(cy - c + 1):
            return
        
        if cnt == k and cx == r-1 and cy == c-1:
            answer = string
            return
            
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if string < answer:
                    dfs(nx, ny, cnt+1, string+dAlpha[i])
    
    dist = abs(x-r) + abs(y-c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"        
    dfs(x-1, y-1, 0, "")
    
    return answer
