def solution(s):
    arr = s[2:-2].split("},{")
    for idx in range(len(arr)):
        arr[idx] = list(map(int, arr[idx].split(",")))
    arr.sort(key = lambda x: len(x))
    answer = []
    cur = set(arr[0])
    answer.append(list(cur)[0])
    for i in range(1, len(arr)):
        answer.append(list(set(arr[i]) - (cur))[0])
        cur = set(arr[i])
    
    return answer