def solution(new_id):
    answer = ''
    new_id = list(new_id)
    start_dot_idx = 1001
    # 1-2단계
    for idx, c in enumerate(new_id):
        if 65 <= ord(c) <= 90:
            new_id[idx] = chr(ord(c) + 32)
    for idx, c in enumerate(new_id):     
        if (ord(c) < 97 or ord(c) > 122) and (ord(c) < 48 or ord(c) > 57) and c not in ['-', '_', '.']:
            new_id[idx] = ''
    new_id = list(''.join(new_id))
    # 3단계        
    for idx, c in enumerate(new_id):        
        if c == '.':
            if idx == start_dot_idx + 1:
                new_id[idx] = ''
                start_dot_idx += 1
            else:
                start_dot_idx = idx
    new_id = list(''.join(new_id))
    # 4단계            
    if new_id[0] == '.':
        new_id[0] = ''
    if new_id[-1] == '.':
        new_id[-1] = ''
    # 5단계
    if ''.join(new_id) == "":
        new_id = "a"
    
    # 6단계
    new_id = list(''.join(new_id))
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id[-1] = ''
    
    new_id = list(''.join(new_id))
    # 7단계
    if 0 < len(new_id) <= 2:
        last = new_id[-1]
        while len(new_id) < 3:
            new_id.append(last)
    
    answer = ''.join(new_id)

    return answer