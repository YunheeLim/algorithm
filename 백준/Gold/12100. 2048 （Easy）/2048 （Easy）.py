import copy

n = int(input())
initial_arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
cnt = 5

def left(board):
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 # 옮길 예정이므로 0으로 변경
                
                if board[i][cursor] == 0: # 빈 칸이면
                    board[i][cursor] = tmp # 이동
                elif board[i][cursor] == tmp: # 같은 값이면
                    board[i][cursor] *= 2 # 합치기
                    cursor += 1 # 합쳐진 칸에 다음 숫자 배치되는 것 방지
                else: # 다른 값이면
                    cursor += 1 # 다음으로 넘어가기
                    board[i][cursor] = tmp
    return board

def right(board):
    for i in range(n):
        cursor = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up(board):
    for j in range(n):
        cursor = 0
        for i in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(n):
        cursor = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
            
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def dfs(cnt, arr):
    global ans

    # 5번 움직였을 때
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return
    
    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(cnt + 1, left(copy_arr))
        elif i == 1:
            dfs(cnt + 1, right(copy_arr))
        elif i == 2:
            dfs(cnt + 1, up(copy_arr))
        else:
            dfs(cnt + 1, down(copy_arr))
            
dfs(0, initial_arr)
print(ans)