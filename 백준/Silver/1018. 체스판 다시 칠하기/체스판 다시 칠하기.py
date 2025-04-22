import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
answer = int(1e9)

def calculate_min(arr):
    ans1, ans2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0: # 짝수
                if arr[i][j] != 'W':
                    ans1 += 1
                else:
                    ans2 += 1
            else: # 홀수
                if arr[i][j] != 'B':
                    ans1 += 1
                else:
                    ans2 += 1
    return min(ans1, ans2)

for i in range(n - 7):
    for j in range(m - 7):
        sliced = []
        for x in range(i, i + 8):
            row = ""
            for y in range(j, j + 8):
                row += board[x][y]
            sliced.append(row)
        answer = min(answer, calculate_min(sliced))

print(answer)
