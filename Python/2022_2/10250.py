#ACM호텔
n=int(input())
for i in range(n):
    
    h,w,room=map(int,input().split())
    if(room%h==0):
        result=(100*h+room//h)
        #room==(100*h)
    else:
        result=(100*(room%h)+room//h+1)
        #print(room%h)
        #print(room//h)
    print(result)
