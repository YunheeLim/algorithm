n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int,input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

# 주사위 굴리기
def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for dir in directions:
    nx = x + dx[dir - 1]
    ny = y + dy[dir - 1]
    
    # 범위 체크
    if 0 <= nx < n and 0 <= ny < m:
        turn(dir)
        
        if arr[nx][ny] == 0: # 칸 수가 0일 때
            arr[nx][ny] = dice[5]
        else: # 칸 수가 0이 아닐 때
            num = arr[nx][ny]
            dice[5] = num
            arr[nx][ny] = 0

        # 주사위 위치 갱신
        x, y = nx, ny
        print(dice[0])