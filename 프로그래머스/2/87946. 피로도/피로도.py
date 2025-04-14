# 가능한 던전 조합 생성
def dfs(dungeons, path, visited):
    if len(path) == len(dungeons):
        # print(path)
        combi.append(path)
        return
    for idx in range(len(dungeons)):
        if visited[idx] == False:
            visited[idx] = True
            dfs(dungeons, path + [dungeons[idx]], visited)
            visited[idx] = False # 백트래킹

def max_dungeons(k, dungeon):
    cnt = 0
    for need, use in dungeon:
        if k < need:
            break
        cnt += 1
        k -= use
    return cnt
    
combi = [] # 던전 조합들

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    dfs(dungeons, [], visited)
    for c in combi:
        max_cnt = max_dungeons(k, c)
        # print(c, max_dungeons(k, c))
        if max_dungeons(k, c) > answer:
            answer = max_cnt
    
    return answer