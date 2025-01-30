def compress(s, size):
    compressed = ""
    prev = s[:size]  # 첫 번째 덩어리
    cnt = 1
    
    for i in range(size, len(s), size):
        cur = s[i:i+size]  # 현재 덩어리
        if cur == prev:  
            cnt += 1  # 같은 경우 카운트 증가
        else:
            compressed += (str(cnt) + prev) if cnt > 1 else prev
            prev = cur
            cnt = 1  # 카운트 초기화
    
    compressed += (str(cnt) + prev) if cnt > 1 else prev  # 마지막 부분 처리
    return len(compressed)  # 압축된 문자열 길이 반환


def solution(s):
    answer = len(s)

    for size in range(1, len(s)):
        answer = min(answer, compress(s, size))
        
    return answer