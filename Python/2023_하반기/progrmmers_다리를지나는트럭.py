def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_bridge = [] #다리를 건너는 트럭
    end_bridge = [] #다리를 지난 트럭
    total_weight = 0
    total = len(truck_weights)
    flag = 0
    while True: #트럭 무개가 빌때까지 반복
        if len(end_bridge) == total:
            break
        for i in range(len(now_bridge)):
            now_bridge[i][1] += 1
            if now_bridge[i][1] >  bridge_length: #만약 다리길이 도착시
                out = now_bridge[0]
                total_weight -= out[0]
                end_bridge.append(out) #끝난 라인에 추가
                flag = 1
        if flag == 1:
            now_bridge.pop(0)
            flag = 0
        if len(truck_weights)>0 and total_weight + truck_weights[0] <= weight: #만약 새로운 무게가 초과되지 않으면
            now = truck_weights.pop(0)
            now_bridge.append([now,1]) #맨 왼쪽 부분을 뽑아서 현재 넣는다.
            total_weight += now #무게도 추가해준다.
        answer += 1
    return answer
#테스트 케이스 1
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights)) #8
#테스트 케이스 2
bridge_length = 100
weight = 100
truck_weights = [100]
print(solution(bridge_length, weight, truck_weights)) #101
#테스트 케이스 3
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]	
print(solution(bridge_length, weight, truck_weights)) #110