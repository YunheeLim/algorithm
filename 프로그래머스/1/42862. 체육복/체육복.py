def solution(n, lost, reserve):
    answer = 0

    arr = [1] * (n)

    for lost_s in lost:
        arr[lost_s - 1] -= 1
        
    for reserve_s in reserve:
        arr[reserve_s - 1] += 1
                
    for i in range(n):
        if arr[i] == 2:
            if i-1 >= 0 and i-1 < n and arr[i-1] == 0:
                arr[i-1] = 1
                arr[i] = 1
            
            if arr[i] == 2:
                if i+1 >= 0 and i+1 < n and arr[i+1] == 0:
                    arr[i+1] = 1
                    arr[i] = 1
                
    for elem in arr:
        if elem > 0:
            answer += 1

    return answer