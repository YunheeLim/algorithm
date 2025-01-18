def solution(survey, choices):
    answer = ''
    
    score = [[0] * 2 for _ in range(4)]
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for sur, choice in zip(survey, choices):
        if choice != 4:
            disagree = sur[0]
            agree = sur[1]
            if choice > 4:
                dic[agree] += choice-4
            elif choice < 4:
                dic[disagree] += 4-choice
    table = []  
    if dic['R'] == dic['T']:
        answer += min('R', 'T')
    elif dic['R'] > dic['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if dic['C'] == dic['F']:
        answer += min('C', 'F')
    elif dic['C'] > dic['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dic['J'] == dic['M']:
        answer += min('J', 'M')
    elif dic['J'] > dic['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if dic['A'] == dic['N']:
        answer += min('A', 'N')
    elif dic['A'] > dic['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer