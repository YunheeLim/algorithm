def solution(targets):
    answer = 1
    targets.sort(key=lambda x : x[1])
    end = targets[0][1]
    targets = targets[1:]
    for s, e in targets:       
        if s >= end:           
            answer += 1
            end = e
        # print('기준:', end, s, e)
            
    # for e in targets:
    #     print(e)
        
    return answer