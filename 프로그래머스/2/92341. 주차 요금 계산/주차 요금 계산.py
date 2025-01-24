import math

def calculate(start, end):
    start_time = int(start[:2]) * 60 + int(start[3:])
    end_time = int(end[:2]) * 60 + int(end[3:])
    duration = end_time - start_time
    return duration

def solution(fees, records):
    money = {}
    parking = {}
    total = {}
    
    for record in records:
        time, car, info = record.split()
        if info == "IN":
            parking[car] = time
        else:
            duration = calculate(parking[car], time)
            total[car] = total.get(car, 0) + duration

            del parking[car]
    
    if parking != {}:
        p_list = list(parking.items())
        for car, time in p_list:
            duration = calculate(parking[car], "23:59")
            total[car] = total.get(car, 0) + duration
    
    sorted_total = list(total.items())
    sorted_total.sort()
    answer = []
    for car, duration in sorted_total:
        basic = duration - fees[0]
        if basic <= 0:
            answer.append(fees[1])
        else:
            extra = math.ceil(basic / fees[2]) * fees[3]
            answer.append(fees[1] + extra)
            
    return answer