n = int(input())

# 입력 처리
rectangles = []
for _ in range(n):
    a, b, c, d = map(float, input().split())
    a, b, c, d = int(a * 10), int(b * 10), int(c * 10), int(d * 10)  # 0.1 단위 정수화
    rectangles.append((a, b, a + c, b + d))  # (x1, y1, x2, y2)

# 이벤트 리스트 생성: (x좌표, 시작/끝 구분, y1, y2)
events = []
for x1, y1, x2, y2 in rectangles:
    events.append((x1, 1, y1, y2))  # 1: 사각형 진입
    events.append((x2, -1, y1, y2)) # -1: 사각형 종료

# x 좌표 기준으로 정렬
events.sort()

# 현재 열려 있는 y구간들
active = []
prev_x = events[0][0]  # 직전 x좌표
area = 0

# 이벤트 순회
for x, typ, y1, y2 in events:
    dx = x - prev_x  # 현재 x와 이전 x 사이의 너비
    if dx > 0:
        # 현재 활성 y구간들을 정렬하고 병합
        active.sort()
        merged = []
        for s, e in active:
            if not merged or merged[-1][1] < s:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        
        # 병합된 y구간의 총 길이 계산
        total_y = sum(e - s for s, e in merged)
        
        # 넓이 = 너비 * 높이
        area += dx * total_y

    # 현재 이벤트 처리
    if typ == 1:
        active.append((y1, y2))  # 사각형 진입 → y구간 추가
    else:
        active.remove((y1, y2))  # 사각형 종료 → y구간 제거

    prev_x = x  # x 갱신

# 출력 처리 (넓이는 100으로 나눠서 원래 단위로)
if area % 100 == 0:
    print(area // 100)
else:
    print(area / 100)
