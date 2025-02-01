def solution(record):
    answer = []
    users = {}
    
    for r in record:
        if len(r.split()) == 3:
            uid, name = r.split()[1], r.split()[2]
            users[uid] = name
    for r in record:
        if r.split()[0] == "Enter":
            uid, name = r.split()[1], r.split()[2]
            answer.append(f'{users[uid]}님이 들어왔습니다.')
        elif r.split()[0] == "Leave":
            answer.append(f'{users[r.split()[1]]}님이 나갔습니다.')
        
            
    return answer