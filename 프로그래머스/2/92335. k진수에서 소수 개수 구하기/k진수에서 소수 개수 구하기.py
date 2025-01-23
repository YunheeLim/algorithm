def isPrime(num):
    for i in range(2,int(int(num)**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    # 진수 변환
    num = ""
    while n:
        num = str(n % k) + num
        n //= k
        
    splites = num.split('0')
    
    for s in splites:
        if s == '1':
            continue
        if s and isPrime(int(s)):
            answer += 1
    
    return answer