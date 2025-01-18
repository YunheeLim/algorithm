import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def can_place_slope(line):
    visited = [False] * n  # 경사로가 설치된 위치

    for i in range(n - 1):
        if line[i] == line[i + 1]:  # 높이가 같으면 계속 진행
            continue
        
        if abs(line[i] - line[i + 1]) > 1:  # 높이 차이가 2 이상이면 불가능
            return False
        
        # 경사로를 내려가는 경우
        if line[i] > line[i + 1]:
            for j in range(i + 1, i + 1 + l):  
                if j >= n or line[j] != line[i + 1] or visited[j]:  # 범위를 벗어나거나 높이가 다르거나 이미 경사로가 있다면 불가능
                    return False
                visited[j] = True  # 경사로 설치
        
        # 경사로를 올라가는 경우
        else:
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != line[i] or visited[j]:  # 범위를 벗어나거나 높이가 다르거나 이미 경사로가 있다면 불가능
                    return False
                visited[j] = True  # 경사로 설치
                
    return True

# 가로줄 확인
for i in range(n):
    if can_place_slope(arr[i]):
        ans += 1

# 세로줄 확인
for j in range(n):
    column = [arr[i][j] for i in range(n)]  # 세로줄 추출
    if can_place_slope(column):
        ans += 1

print(ans)