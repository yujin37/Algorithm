import math
def solution(fees, records):
    answer = [] #비용 청구
    parking = [] #주차장
    check_answer = {} #비용 청구 차들
    for i in range(len(records)):
        time, car, status = records[i].split() #시간, 차번호, 상태 분리
        time_h, time_m = time.split(':') #시간 분리
        change_time = int(time_h) * 60 + int(time_m) #시를 분으로 변환
        if status == "IN":
            parking.append([car, change_time])
        elif status == "OUT": #출차
            for i in range(len(parking)):
                if car in parking[i][0]:
                    in_time = parking[i][1] #입차 시간 가져와서
                    result_time = change_time - in_time  #시간 차이 계산

                    if car in check_answer:
                        check_answer[car] += result_time
                    else:
                        check_answer[car] = result_time
                    parking.pop(i)
                    break
    if len(parking):
        for i in range(len(parking)):
            end_time = 23 * 60 + 59
            result_time = end_time - parking[i][1]
            
            if parking[i][0] in check_answer:
                check_answer[parking[i][0]] += result_time
            else:
                check_answer[parking[i][0]] = result_time
    check_answer = sorted(check_answer.items())
    for i in range(len(check_answer)):
        if check_answer[i][1] > fees[0]:
            left = check_answer[i][1] - fees[0]
            left_fee = math.ceil(left/fees[2])*fees[3]
            result = fees[1] + left_fee
        else:
            result = fees[1]
        answer.append(result)
    
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", 
           "23:00 5961 OUT"]
print(solution(fees, records))