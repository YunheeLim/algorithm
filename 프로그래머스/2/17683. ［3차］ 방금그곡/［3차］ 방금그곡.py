def calculate_duration(start, end):
    """재생 시간 계산"""
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))
    return (end_h - start_h) * 60 + (end_m - start_m)


def convert_sharps(melody):
    """# 포함된 음을 변환"""
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")
    melody = melody.replace("B#", "b")

    return melody


def solution(m, musicinfos):
    m = convert_sharps(m)  # 네오의 기억한 멜로디 변환
    answer = "(None)"
    max_duration = 0

    for info in musicinfos:
        start, end, title, sheet = info.split(",")
        duration = calculate_duration(start, end)  # 재생 시간 계산
        sheet = convert_sharps(sheet)  # 악보 변환

        # 재생된 멜로디 생성
        played = (sheet * (duration // len(sheet))) + sheet[:duration % len(sheet)]

        # 멜로디 포함 여부 확인
        if m in played:
            if duration > max_duration:  # 재생 시간이 더 길 경우
                answer = title
                max_duration = duration

    return answer
