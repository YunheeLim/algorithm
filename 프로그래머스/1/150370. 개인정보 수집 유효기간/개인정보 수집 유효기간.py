def solution(today, terms, privacies):
    answer = []
    today_dic = {}
    
    # 오늘 날짜 딕셔너리
    today_dic['year'], today_dic['month'], today_dic['day'] = map(int, today.split('.'))

    # 약관 딕셔너리
    dic = {}
    for term in terms:
        kind, period = term.split()
        dic[kind] = period   

    # 개인정보
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        y, m, d = map(int, date.split('.'))
                
        # 첫 날
        if d == 1:
            d = 28
            m -= 1
        else:
            d -= 1
        
        # 달 추가
        m += int(dic[term])

        # 마지막 달
        if  m > 12:
            if (m % 12): # 달이 0이 아닐때
                y += (m // 12)
                m %= 12
            else:
                y += (m // 12 - 1)
                m = 12
        
        print(y, m, d)
        
        # 파기 판단
        if y > today_dic['year']: # 연도 안지남
            continue
        elif y == today_dic['year']: # 동년
            if m > today_dic['month']: # 월 안지남
                continue
            elif m == today_dic['month']: # 동년, 동월
                if d >= today_dic['day']: # 일 안지남
                    continue
                else: 
                    answer.append(idx + 1)
            else: # 월 지남
                answer.append(idx + 1)
        else: # 연도 지남
            answer.append(idx + 1)
                        
    answer.sort()
                  
    return answer