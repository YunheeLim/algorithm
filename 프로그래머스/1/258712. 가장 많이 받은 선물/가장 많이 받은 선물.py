def solution(friends, gifts):
    answer = 0
    result = [0] * len(friends)
    
    # 이름 인덱스 매핑
    dict = {}
    
    for i in range(len(friends)):
        dict[friends[i]] = i
          
    # 주고받은 선물 정보
    arr = [[0] * len(friends) for _ in range(len(friends))]
    
    # 선물 지수
    score = [0] * len(friends)
    
    for i in gifts:
        sender, receiver = i.split(" ")
        arr[dict[sender]][dict[receiver]] += 1
        
        score[dict[sender]] += 1
        score[dict[receiver]] -= 1
        
    for sender_idx in range(len(arr)):
        for receiver_idx in range(len(arr[0])):
            # 자기 자신 제외
            if sender_idx == receiver_idx:
                continue
            # 선물 더 많이 준 경우
            if arr[sender_idx][receiver_idx] > arr[receiver_idx][sender_idx]:
                result[sender_idx] += 1
            elif arr[sender_idx][receiver_idx] == arr[receiver_idx][sender_idx]:
                if score[sender_idx] > score[receiver_idx]:
                     result[sender_idx] += 1
                        
    print(result)
        
    return max(result)