def solution(rows, columns, queries):
    answer = []
    arr = [[(i - 1) * columns + j for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    
    for x1, y1, x2, y2 in queries:
        # 1-based index -> 0-based index 변환
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        left_top = arr[x1][y1]  # 회전 시작 위치 값 저장
        min_val = left_top

        # 1️⃣ 왼쪽 세로 이동
        for i in range(x1, x2):
            arr[i][y1] = arr[i + 1][y1]
            min_val = min(min_val, arr[i][y1])

        # 2️⃣ 아래쪽 가로 이동
        for j in range(y1, y2):
            arr[x2][j] = arr[x2][j + 1]
            min_val = min(min_val, arr[x2][j])

        # 3️⃣ 오른쪽 세로 이동
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i - 1][y2]
            min_val = min(min_val, arr[i][y2])

        # 4️⃣ 위쪽 가로 이동
        for j in range(y2, y1, -1):
            arr[x1][j] = arr[x1][j - 1]
            min_val = min(min_val, arr[x1][j])

        arr[x1][y1 + 1] = left_top  # 저장한 값 복사

        answer.append(min_val)  # 최솟값 저장

    return answer
