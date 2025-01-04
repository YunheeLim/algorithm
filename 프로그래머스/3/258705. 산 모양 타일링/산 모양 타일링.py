def solution(n, tops):
    MOD = 10007

    a = [0] * n
    b = [0] * n
    
    a[0] = 1
    b[0] = 3 if tops[0] else 2
    
    for k in range(1, n):
        if tops[k]:
            a[k] = a[k - 1] + b[k - 1]
            b[k] = 2 * a[k - 1] + 3 * b[k - 1]
        else:
            a[k] = a[k - 1] + b[k - 1]
            b[k] = a[k - 1] + 2 * b[k - 1]
        
        a[k] %= MOD
        b[k] %= MOD
    
    return (a[-1] + b[-1]) % MOD