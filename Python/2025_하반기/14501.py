n = int(input())
council_days= []
council_cost=[]
result = [0 for _ in range(n+1)]
for i in range(n):
    t, p = map(int,input().split())
    council_days.append(t)
    council_cost.append(p)
for i in range(n-1, -1, -1):
    if council_days[i] + i > n:
        result[i] = result[i+1] #만약 현재 상담날짜 + 소요 기간이 날짜 넘으면 패스
    #그외의 경우를 어떻게 처리할 것인가. 
    else:
        result[i] = max(council_cost[i] + result[i+council_days[i]], result[i+1]) #앞애 입력하기 전 값이랑 지금 현재위치에서의 값을 넣어야 할텐데. 
    
print(result[0])