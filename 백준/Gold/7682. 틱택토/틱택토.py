# # 말이 홀수라면 X > O
# # 말이 짝수라면 X = O
# # 3개 완성했는지
# # 모두 아니면 꽉 찾는지

# def check_pairs(board):
#     circle_cnt = sum([row.count('O') for row in board])
#     scissor_cnt = sum([row.count('X') for row in board])
#     if (circle_cnt + scissor_cnt) % 2 == 0: # 짝수
#         if circle_cnt == scissor_cnt:
#             return True
#     else:
#         if circle_cnt + 1 == scissor_cnt:
#             return True
#     return False



#     return False

# cnt = 0

# while True:
#     s = input()
#     if s == "end":
#         break
#     board = []
#     for i in range(0, 8, 3):
#         board.append(list(s[i:i+3]))
    
#     cnt += 1
#     print(f"====={cnt}=====")
#     for e in board:
#         print(e)
#     # 짝 안 맞으면 바로 틀림
#     if check_pairs(board) == False:
#         print("invalid")
#         continue
    
#     # 한 줄 완성
#     if check_line(board, 'X') or check_line(board, 'O'):
#         print("valid")
    
#     # 짝도 맞고 한 줄 완성도 안했는데 말 더 안 놓음

 
#     # for e in board:
#     #     print(e)
    
board = [['.'] * 3 for _ in range(3)]


def check_line(c):
    # 가위표
    # 가로 체크
    for row in board:
        if row.count(c) == 3:
            return True
    transform_board = [list(row) for row in zip(*board)]
    transform_board = tuple(map(tuple, transform_board))
    # 세로 체크
    for row in transform_board:
        if row.count(c) == 3:
            return True
    # 대각선 체크
    for i, j in zip(range(3), range(3)):
        if board[i][j] != c:
            break
    else:
        return True
    # 반대쪽 대각선 체크
    for i, j in zip(range(3), range(2, -1, -1)):
        if board[i][j] != c:
            break
    else:
        return True

def dfs(turn):
    # 라인 체크
    if check_line('O') or check_line('X'):
        # for e in board:
        #     print(e)
        # print()
        forms.add(tuple(map(tuple, board)))
        return
    # 꽉채움
    if turn == 10:
        # for e in board:
        #     print(e)
        # print()
        forms.add(tuple(map(tuple, board)))
        return
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X' if turn % 2 == 1 else 'O'
                dfs(turn + 1)
                board[i][j] = '.'

forms = set()

dfs(1)

while True:
    s = input()
    if s == "end":
        break

    arr = []
    for i in range(0, 8, 3):
        arr.append(list(s[i:i+3]))
    
    arr = tuple(map(tuple, arr))
    if arr not in forms:
        print("invalid")
    else:
        print("valid")

    