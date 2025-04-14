answer = 0
# 가능한 던전 조합 생성
def dfs(dungeons, k, visited, cnt):
    global answer
    if k < 0:
        return
    if cnt > answer:
        answer = cnt
    for idx in range(len(dungeons)):
        if k >= dungeons[idx][0] and visited[idx] == False:
            visited[idx] = True
            dfs(dungeons, k - dungeons[idx][1], visited, cnt + 1)
            visited[idx] = False # 백트래킹

# def max_dungeons(k, dungeon):
#     cnt = 0
#     for need, use in dungeon:
#         if k < need:
#             break
#         cnt += 1
#         k -= use
#     return cnt
    
combi = [] # 던전 조합들

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    dfs(dungeons, k, visited, 0)
    # for c in combi:
    #     max_cnt = max_dungeons(k, c)
    #     if max_dungeons(k, c) > answer:
    #         answer = max_cnt
    
    return answer