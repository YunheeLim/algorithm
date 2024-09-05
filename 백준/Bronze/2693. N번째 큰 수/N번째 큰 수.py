import sys
sys.stdin.readline

t = int(input())

array = []

for _ in range(t):
    array = list(map(int, input().split()))
    array.sort()
    print(array[-3])