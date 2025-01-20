import sys
input = sys.stdin.readline

# 톱니바퀴 입력 (4개)
wheels = [list(map(int, str(input().rstrip()))) for _ in range(4)]
k = int(input())  # 회전 횟수
rotate = [list(map(int, input().split())) for _ in range(k)]

# 톱니바퀴 회전 함수 (시계 방향 1, 반시계 방향 -1)
def rotate_wheel(num, dir):
    if dir == 1:  # 시계 방향
        wheels[num] = [wheels[num][-1]] + wheels[num][:-1]
    else:  # 반시계 방향
        wheels[num] = wheels[num][1:] + [wheels[num][0]]

# 회전 전파 함수
def set_rotation(i, dir):
    isRotated = [0] * 4  # 4개의 톱니바퀴 회전 여부 저장
    isRotated[i] = dir  # 현재 톱니바퀴의 회전 방향 설정

    # 왼쪽 방향으로 전파
    for j in range(i, 0, -1):  # i부터 0까지 왼쪽으로 이동
        if wheels[j][6] != wheels[j - 1][2]:  # 서로 다른 극이면 회전
            isRotated[j - 1] = -isRotated[j]
        else:
            break  # 같은 극이면 전파 중단

    # 오른쪽 방향으로 전파
    for j in range(i, 3):  # i부터 3까지 오른쪽으로 이동
        if wheels[j][2] != wheels[j + 1][6]:  # 서로 다른 극이면 회전
            isRotated[j + 1] = -isRotated[j]
        else:
            break  # 같은 극이면 전파 중단

    # 모든 톱니바퀴 회전 적용
    for j in range(4):
        if isRotated[j] != 0:
            rotate_wheel(j, isRotated[j])

# 주어진 회전 명령 수행
for num, dir in rotate:
    set_rotation(num - 1, dir)

# 점수 계산 (12시 방향의 톱니값)
result = wheels[0][0] * 1 + wheels[1][0] * 2 + wheels[2][0] * 4 + wheels[3][0] * 8
print(result)
