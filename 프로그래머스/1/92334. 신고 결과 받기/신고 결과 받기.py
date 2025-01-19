def solution(id_list, report, k):
    answer = []
    arr = [[0] * len(id_list) for _ in range(len(id_list))]
    dic = {}
    
    for idx, userId in enumerate(id_list):
        dic[userId] = idx
            
    for repo in report:
        user, to = repo.split()
        if arr[dic[user]][dic[to]] == 0:
            arr[dic[user]][dic[to]] += 1
    
    s = set()
    for j in range(len(id_list)):
        sum = 0
        for i in range(len(id_list)):
            sum += arr[i][j]
        if sum >= k:
            s.add(j)

    
    for userId in id_list:
        cnt = 0
        for idx, val in enumerate(arr[dic[userId]]):
            if val and (idx in s):
                cnt += 1    
                    
        answer.append(cnt)
        
    return answer