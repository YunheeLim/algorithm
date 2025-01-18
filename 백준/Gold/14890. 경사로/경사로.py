import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def can_place_slope(line):
    slopes = [False] * n  # 경사로가 설치된 위치

    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue

        if abs(line[i] - line[i + 1]) > 1:
            return False
        
        if line[i] > line[i + 1]:
            for j in range(i + 1, i + 1 + l):
                if j >= n or line[j] != line[i + 1] or slopes[j]:
                    return False
                slopes[j] = True 
        else:
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != line[i] or slopes[j]:
                    return False
                slopes[j] = True
    return True

for i in range(n):
    if can_place_slope(arr[i]):
        ans += 1

for j in range(n):
    column = [arr[i][j] for i in range(n)]
    if can_place_slope(column):
        ans += 1
            
print(ans)