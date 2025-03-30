from math import ceil

def solution(progresses, speeds):
    answer = []
    remains = []
    for idx, progress in enumerate(progresses):
        remains.append(ceil((100 - progress) / speeds[idx]))
    print(remains)
    current = remains[0]
    cnt = 1
    
    for day in remains[1:]:
        if day <= current:
            cnt += 1
        else:
            answer.append(cnt)
            current = day
            cnt = 1
            
    answer.append(cnt)
    return answer