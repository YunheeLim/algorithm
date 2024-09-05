import sys
sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

max = -1000000
min = 1000000

for elem in lst:
    if elem > max:
        max = elem
    if elem < min:
        min = elem

print(min, max)