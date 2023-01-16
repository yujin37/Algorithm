t=int(input())
for i in range(t):
    num=int(input())
    test=[1,2,4]
    if num<=3 and num>0:
        print(test[num-1])
    else:
        for j in range(4,num+1):
            result=test[j-4]+test[j-3]+test[j-2]    
            test.append(result)
        print(test[num-1])