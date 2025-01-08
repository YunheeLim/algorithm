def solution(users, emoticons):
    answer = [0, 0]
    discounts = []
    percentage = [10, 20, 30, 40]
    
    # 이모티콘 할인율 조합
    def dfs(arr, depth):
         # 모든 이모티콘에 대해 할인율 정해졌을 때 종료
        if depth == len(emoticons):
            discounts.append(arr[:])
            return
        
        for per in percentage:
            arr[depth] += per
            dfs(arr, depth + 1)
            arr[depth] -= per # 백트래킹
        
    dfs([0] * len(emoticons), 0)
    
    for combi_idx in range(len(discounts)):
        plus_user = 0
        profit = 0
        
        for user in users:
            emo_sum = 0 # 사용자 별 구매한 이모티콘 총 가격
            for emo_idx in range(len(emoticons)):
                if discounts[combi_idx][emo_idx] >= user[0]:
                    emo_sum += emoticons[emo_idx] * ((100 - discounts[combi_idx][emo_idx]) / 100)
            if emo_sum >= user[1]:
                plus_user += 1
            else:
                profit += emo_sum
                
        if plus_user > answer[0]:
            answer = [plus_user, int(profit)]
        elif plus_user == answer[0]:
            if profit > answer[1]:
                answer = [plus_user, int(profit)]
            
    return answer