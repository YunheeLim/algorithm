import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

# Collect all house and chicken locations
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

# Precompute distances from each house to all chicken houses
chicken_distances = [[0] * len(chickens) for _ in range(len(houses))]

for h_idx, (hx, hy) in enumerate(houses):
    for c_idx, (cx, cy) in enumerate(chickens):
        chicken_distances[h_idx][c_idx] = abs(hx - cx) + abs(hy - cy)

# Find the minimum city chicken distance
ans = float('inf')

for selected in combinations(range(len(chickens)), m):
    total_distance = 0
    
    # Compute minimum chicken distance for each house
    for h_idx in range(len(houses)):
        min_dist = float('inf')
        for c_idx in selected:
            min_dist = min(min_dist, chicken_distances[h_idx][c_idx])
        total_distance += min_dist

    ans = min(ans, total_distance)

print(ans)
