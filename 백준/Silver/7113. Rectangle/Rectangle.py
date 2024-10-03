import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
remain = max(n, m)
ans = 0

def recursion(w, h, cnt):
    # global ans
    # ans += 1
    if w == h:
        return cnt
    
    if w > h:
        line = h
        remain = w - line

        return recursion(remain, h, cnt + 1)

    else:
        line = w
        remain = h - line
  
        return recursion(w, remain, cnt + 1)

print(recursion(n, m, 1))
