def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        skill_lst = list(skill)
        for s in tree:
            if s in skill_lst:
                temp = skill_lst[skill_lst.index(s) + 1:]
                if -1 not in temp:
                    skill_lst[skill_lst.index(s)] = -1
        flag = True            
        for idx in range(len(skill_lst) - 1):
            if skill_lst[idx] != -1 and skill_lst[idx + 1] == -1:
                flag = False
                break
        print(skill_lst)
        if flag:
            answer += 1
    return answer