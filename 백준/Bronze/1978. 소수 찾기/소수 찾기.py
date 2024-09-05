import sys
sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

result = 0

for num in lst:
    isPrime = False
    if num == 2:
        result += 1
    for i in range(2, num):
        if num % i == 0:
            break
        if num % i != 0 and i == num -1:
            isPrime = True
    if isPrime:
        result += 1

print(result)