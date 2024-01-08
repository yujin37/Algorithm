t = int(input())

for s in range(t):
    n = int(input())
    stocks = list(map(int,input().split()))

    max_num = 0 
    profit = 0
    for i in range(n-1, -1, -1):
        if stocks[i] > max_num:
            max_num = stocks[i]
        else:
            profit += (max_num - stocks[i])
    print(profit)