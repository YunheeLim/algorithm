def solution(info, edges):
    answer = []
    visited = [False] * len(info)
    
    def dfs(sheeps, wolves):
        if sheeps > wolves:
            answer.append(sheeps)
        else:
            return
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c]:
                    dfs(sheeps, wolves + 1)
                else:
                    dfs(sheeps + 1, wolves)
                visited[c] = False
                
    visited[0] = True
    dfs(1, 0)
        
    return max(answer)