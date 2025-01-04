def solution(edges):
    answer = [0, 0, 0, 0]
    
    exchanges = {}
    
    for a, b in edges:
        if not exchanges.get(a):
            exchanges[a] = [0, 0]
        if not exchanges.get(b):
            exchanges[b] = [0, 0]
            
        exchanges[a][0] += 1
        exchanges[b][1] += 1
        
    for key, exchange in exchanges.items():
        # 생성된 정점
        if exchange[0] >= 2 and exchange[1] == 0:
            answer[0] = key
        # 막대 그래프
        if exchange[0] == 0 and exchange[1] >= 1:
            answer[2] += 1
        # 8자 그래프
        if exchange[0] == 2 and exchange[1] >= 2:
            answer[3] += 1
    answer[1] = exchanges[answer[0]][0] - answer[2] - answer[3]
    
    return answer