import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [[[] for _ in range(n)] for _ in range(n)]
A = [[5] * n for _ in range(n)]
origin_A = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    tree[x][y].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    # 봄: 어린 나무부터 양분 섭취, 못 먹으면 죽음
    dead = []
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                new_tree = []
                tree[i][j].sort()
                for tree_idx, age in enumerate(tree[i][j]):
                    if A[i][j] >= age:
                        A[i][j] -= age
                        tree[i][j][tree_idx] += 1
                    else:
                        for _ in range(tree_idx, len(tree[i][j])):
                            dead.append((i, j, tree[i][j].pop()))  # 죽은 나무 저장
                        break

    # 여름: 죽은 나무가 양분이 됨
    for i, j, val in dead:
        A[i][j] += val // 2

    # 가을: 번식 (나이가 5의 배수인 나무만)
    for i in range(n):
        for j in range(n):
            for age in tree[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].append(1) # 번식한 나무 추가
            A[i][j] += origin_A[i][j] # 겨울

# 살아남은 나무 개수 출력
ans = sum(len(tree[i][j]) for i in range(n) for j in range(n))
print(ans)
