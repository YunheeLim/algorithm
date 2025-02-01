def solution(dartResult):
    answer = 0
    scores = []
    cnt = 0
    s = ""
    for c in dartResult:
        if c in ['S', 'D', 'T']:
            if c == 'S':
                scores.append(int(s))
            elif c == 'D':
                scores.append(int(s)**2)
            else:
                scores.append(int(s)**3)
            s = ""
            cnt += 1
        elif c in ['*', '#']:
            if c == "*":
                if cnt - 2 >= 0:
                    scores[cnt - 2] += scores[cnt - 2]
                if cnt - 1 >= 0:
                    scores[cnt - 1] += scores[cnt - 1]
            else:
                scores[cnt - 1] = -scores[cnt - 1]

        else:
            s += c
    
    return sum(scores)