def first(x, sy, ey, answer):
    global current
    for j in range(sy, ey + 1):
        answer[x][j] = current
        current += 1

def second(y, sx, ex, answer):
    global current
    for i in range(sx, ex + 1):
        answer[i][y] = current
        current += 1
        
def third(x, sy, ey, answer):
    global current
    for j in range(ey, sy - 1, -1):
        answer[x][j] = current
        current += 1
            
def fourth(y, sx, ex, answer):
    global current
    for i in range(ex, sx - 1, -1):
        answer[i][y] = current
        current += 1
        
current = 1

def solution(n):
    answer = [[0] * n for _ in range(n)]
    cycle = 0

    while current <= n * n:
        first(cycle, cycle, n - 1 - cycle, answer)
        second(n - 1 - cycle, cycle + 1, n - 1 - cycle, answer)
        third(n - 1 - cycle, cycle, n - 2 - cycle, answer)
        fourth(cycle, cycle + 1, n - 2 - cycle, answer)
        cycle += 1
    
    for e in answer:
        print(e)
    return answer