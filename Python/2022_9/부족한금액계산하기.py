def solution(price, money, count):
    sum_money=0
    cnt=1
    while cnt<=count:
        rent=price*cnt
        sum_money+=rent
        cnt+=1
    if sum_money>money:
        return sum_money-money
    else:
        return 0
