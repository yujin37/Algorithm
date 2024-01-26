import sys
from collections import deque
input = sys.stdin.readline
n, w, L = map(int,input().split())

trucks = deque(map(int,input().split()))

bridge = deque([0 for _ in range(w)])
now = 0
time = 0

while trucks or sum(bridge) != 0: 
    time += 1 #걸린 시간 기록
    bridge.popleft() #기존 값 빼주고
    #다리 위에 있는 트럭 수가 적고 무게도 이하라면 
    if trucks and sum(bridge) + trucks[0]  <= L:
        bridge.append(trucks.popleft()) #트럭을 올린다.
        #now += 1 #지나간 트럭 인덱스도 기록해주고
    else:
        bridge.append(0) #넣지못하면 빈 값으로 넣어준다.

print(time)