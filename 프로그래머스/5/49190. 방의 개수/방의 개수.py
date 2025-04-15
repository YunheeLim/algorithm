def solution(arrows):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    x, y = 0, 0
    visited_nodes = set()
    visited_edges = set() # 같은 길 왕복하는 경우도 있을 수 있으므로 간선까지 고려
    visited_nodes.add((x, y))
    for d in arrows:
        for _ in range(2): # 대각선 교차 고려해서 0.5 길이씩 두 번
            nx = x + dx[d]
            ny = y + dy[d]
            # 새로운 경로로 노드 다시 방문한 경우
            if ((x, y), (nx, ny)) not in visited_edges:
                if (nx, ny) in visited_nodes:
                    answer += 1
            visited_nodes.add((nx, ny))
            visited_edges.add(((x, y), (nx, ny)))
            visited_edges.add(((nx, ny), (x, y)))
            x, y = nx, ny
    
    return answer