from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])
        
    while q:
        p, idx = q.popleft()
        for i in q:
            if i[0] > p:
                q.append([p, idx])
                break
        else: # 실행
            answer += 1
            if idx == location:
                break
    return answer