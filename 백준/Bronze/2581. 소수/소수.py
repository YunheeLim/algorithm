import sys
sys.stdin.readline

m = int(input())
n = int(input())

lst = []
for num in range(m, n + 1):
    if num == 2:
        lst.append(num)
    for i in range(2, num):
        if num % i == 0:
            break
        if num % i != 0 and i == num - 1:
            lst.append(num)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))