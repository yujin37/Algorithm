n, w = map(int,input().split())

stocks = []
amount = 0
for i in range(n):
    stocks.append(int(input()))

for i in range(n-1):
    if stocks[i] < stocks[i+1]: #만약 다음 것보다 현재 값이 작으면
        
        if w // stocks[i] > 0: #최대한 매수
            amount = w // stocks[i] #양을 계산하고
            w = w - amount * stocks[i] #금액을 지불한다.
    
    #만약 값이 이전보다 오르고 가지고 있는 양이 0보다 크면
    elif stocks[i] > stocks[i-1] and amount > 0:
        w = w + amount * stocks[i] #팔고 수익을 가져온다.
        amount = 0 #양도 초기화하고
if amount > 0:
    w = w + amount * stocks[-1]
print(w)
            