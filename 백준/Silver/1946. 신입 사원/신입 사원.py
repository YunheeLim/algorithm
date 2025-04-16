t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort() # 서류 기준 정렬
    top = arr[0][1] # 면접 최고 순위
    answer = 1 # 1등은 무조건 포함되므로 1로 시작
    for i in range(1, n):
        if arr[i][1] < top: # 현재 면접 등수보다 더 높은 등수가 발생하면 최고 면접 등수 갱신
            top = arr[i][1]
            answer += 1

    print(answer)