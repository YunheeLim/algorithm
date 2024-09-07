n = int(input())

answer = 0
row = [0] * n

# x: 행
def is_promising(x):
    for i in range(x):
        if row[i] == row[x]:
            return False
        if abs(x - i) == abs(row[x] - row[i]):
            return False
    return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(answer)