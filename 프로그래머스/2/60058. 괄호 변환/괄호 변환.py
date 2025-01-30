def change(p):
    # 1단계
    if p == "":
        return p
    # 2단계
    s = 0
    idx = 0 # u, v 분리 지점
    for i in range(len(p)):
        if p[i] == "(":
            s -= 1
        else:
            s += 1
        if s == 0:
            idx = i + 1
            break
    u = p[:idx]
    v = p[idx:] if idx < len(p) else ""
    # 3단계
    if u[0] == "(":
        return u + change(v)
    else:
        temp = "(" + change(v) + ")"
        u = u[1:-1].replace('(', '|')
        u = u.replace(')', '(')
        u = u.replace('|', ')')
        temp += u
        return temp
        
        
def solution(p):
    answer = change(p)
    return answer