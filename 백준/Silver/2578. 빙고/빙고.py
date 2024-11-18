arr = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]

def checkX(num):
    for i in range(5):
        for j in range(5):
            if (arr[i][j] == num):
                arr[i][j] = 0

def checkBingo():
    lines = 0

    # 가로 체크
    for i in range(5):
        temp = 0
        for j in range(5):
            if(arr[i][j] == 0):
                temp += 1
            else:
                break
        if(temp == 5):
            lines += 1

    # 세로 체크
    for j in range(5):
        temp = 0
        for i in range(5):
            if(arr[i][j] == 0):
                temp += 1
            else:
                break
        if(temp == 5):
            lines += 1

    # 오른쪽 아래 대각선 체크
    temp = 0
    for i in range(5):
        if(arr[i][i] == 0):
            temp += 1
    if(temp == 5):
        lines += 1

    # 오른쪽 위 대각선 체크
    temp = 0
    for i in range(5):
        if(arr[4-i][i] == 0):
            temp += 1
    if(temp == 5):
        lines += 1

    return lines
            
result = 0


for i in range(5):
    for j in range(5):
        result += 1
        checkX(nums[i][j])

        if(checkBingo() >= 3):
            print(result)
            exit()