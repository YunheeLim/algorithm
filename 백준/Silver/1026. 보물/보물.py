import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for i, j in zip(A, B):
    answer += i*j

print(answer)