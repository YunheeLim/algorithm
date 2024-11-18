answer = -1

def dfs(k, arr, visited, cnt):
    global answer
    if answer < cnt:
        answer = cnt
    for i in range(len(arr)):
        if(k >= arr[i][0] and not visited[i]):
            visited[i] = True
            dfs(k-arr[i][1], arr, visited, cnt + 1)
            visited[i] = False # 백트래킹
    

def solution(k, dungeons):
    visited = [ False ] * len(dungeons)
    
    dfs(k, dungeons, visited, 0)
            
    return answer