import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    can_make = False
    first = 0
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        if first >= K:
            can_make = True
            break
        second = heapq.heappop(scoville)
        total = first + second * 2
        answer += 1
        heapq.heappush(scoville, total)
        
    if scoville and scoville[0] >= K:
        return answer
    else:
        return -1
        
    return answer