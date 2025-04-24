def solution(n, computers):
    global answer
    answer = 0
    
    def dfs(com):
        visited[com] = True
        for i in range(n):
            if computers[com][i] == 1 and not visited[i]:
                dfs(i)
    
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer