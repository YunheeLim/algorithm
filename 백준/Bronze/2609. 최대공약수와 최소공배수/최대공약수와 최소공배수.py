import sys
sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
        
print(gcd(a, b))
print(lcm(a, b))