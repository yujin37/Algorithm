cash = int(input())

stocks = list(map(int,input().split()))

jun =[cash, 0]
min = [cash, 0]
min_stat = [0, 0] #up 1, down 0
for i in range(14):
    #오늘의 가격
    today_price = stocks[i]
    #준현이의 자산 계산
    #만약 오늘의 가격이 가지고 있는 현금보다 작다면
    if jun[0] >= today_price:
        # 가지고 있는 주식 수 업데이트
        buy = jun[0] // today_price
        jun[1] += buy
        #가지고 있는 현금 업데이트
        jun[0] = jun[0] % today_price
    #성민이의 자산 계산
    
    if i == 0:
        pass
    if stocks[i] < stocks[i-1]:
        #하락장
        if min_stat[0] == 1: #상승장이었으면
            min_stat[0] = 0 #하락장이라고 해주고
            min_stat[1] = 1 #일수도 초기화
        else: #하락장이었으면
            min_stat[1] += 1 #반복일수 올리고
            if min_stat[1] >= 3 and min[0] >= stocks[i]: #3일이라면
                #매수 진행 
                min[1] += min[0] // stocks[i]
                min[0] = min[0] % stocks[i] 
                
    elif stocks[i] > stocks[i-1]:
        if min_stat[0] == 0: #하락장이었으면
            min_stat[0] = 1 #상승장으로 변경
            min_stat[1] = 1 
        else: #상승장이었으면
            min_stat[1] += 1
            if min_stat[1] == 3 and min[1] > 0: #3일이라면
                #매도 진행
                min[0] = stocks[i] * min[1] #현금 업데이트
                
                min[1] = 0 #개수 업데이트
                
    else:
        min_stat[1] = 0            
            
total_jun = jun[0] + stocks[13] * jun[1]
total_min = min[0] + stocks[13] * min[1]

if total_jun > total_min:
    print('BNP')
elif total_jun < total_min:
    print('TIMING')
else:
    print('SAMESAME')