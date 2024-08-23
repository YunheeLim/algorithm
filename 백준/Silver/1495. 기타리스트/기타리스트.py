N, S, M = map(int, input().split())
V = list(map(int, input().split()))

A = [0 for _ in range(M+1)]

A[S] = 1

for i in range(len(V)):
    temp = set()
    for ind, data in enumerate(A):
        if data:
            if ind + V[i] <= M:
                temp.add(ind+V[i])
            if ind - V[i] >= 0:
                temp.add(ind-V[i])
    A = [1 if x in temp else 0 for x in range(M+1)]

if A.count(1) == 0:
    print(-1)
else:
    A.reverse()
    print(M-A.index(1))
