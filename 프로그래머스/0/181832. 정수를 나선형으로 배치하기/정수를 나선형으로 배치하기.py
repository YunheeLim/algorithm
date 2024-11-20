def solution(n):
    answer = [[0] * n for _ in range(n)]
    cycle = 0
    cnt = 1
    while(cnt <= n*n):
        for i in range(n):
            if not answer[cycle][i]:
                answer[cycle][i] = cnt
                cnt += 1

        for i in range(n):
            if not answer[i][n-cycle-1]:
                answer[i][n-cycle-1] = cnt
                cnt += 1

        for i in range(n):
            if not answer[n-cycle-1][n-i-1]:
                answer[n-cycle-1][n-i-1] = cnt
                cnt += 1

        for i in range(n):
            if not answer[n-i-1][cycle]:
                answer[n-i-1][cycle] = cnt
                cnt += 1
        cycle += 1
            
    print(answer)
    return answer