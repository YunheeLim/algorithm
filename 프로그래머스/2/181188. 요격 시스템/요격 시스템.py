def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])
    s = targets[0][0]
    e = targets[0][1]
    
    for i in range(1, len(targets)):
        if targets[i][0] >= e:
            answer += 1
            e = targets[i][1]
        
    return answer