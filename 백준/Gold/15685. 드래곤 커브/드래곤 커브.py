import sys
input = sys.stdin.readline

n = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

arr = [[False] * 101 for _ in range(101)]

for i in range(n):
    lst = []
    y, x, d, g = map(int, input().split())
    arr[x][y] = True
    lst.append(d)
    cur_d = d
    for gen in range(1, g + 1):
        next = []
        for dir in list(reversed(lst)):
            next.append((dir+1)%4)
        lst.extend(next)
    for dir in lst:
        x += dx[dir]
        y += dy[dir]
        arr[x][y] = True

def check():
    ans = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
                ans += 1
    return ans
print(check())