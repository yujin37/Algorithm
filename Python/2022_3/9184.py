#실버2, 신나는 함수 실행. 
def w(a,b,c):
    #if (a>50&a<-50&b>50&b<-50&c>50&c<-50):
    #    return #이건 필요가 없네... 혹시나 했는데
    if(a<=0 or b<=0 or c<=0):
        return 1 #이건 기준 따라서 하는 것 
    if(a>20 or b>20 or c>20):
        return w(20,20,20)#이렇게 재귀로 해줘야 한다.
    if total[a][b][c]:
        return total[a][b][c]#이건 왜인지 잘 모르겠음. 모양 되면 되는 건가? 동적 계획으로 나온 값이 있다면 재귀로 하지 않도록 저장하는 것이라고 함.
    if(a<b and b<c):#이건 기준에 있는거고
        total[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        #return total[a][b][c]
    else:#이것 역시 기준에 있는 것
        total[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return total[a][b][c]
total=[[[0]*21 for _ in range(21)] for _ in range(21)]#모양 자체가 3차운이어야 하는데 21개로 이루어져야 하니까
while True:
    a,b,c=map(int,input().split())#입력을 받아서
    if(a==-1&b==-1&c==-1):#이 경우에는 break
        break
    
    print("w(%d, %d, %d) = %d" %(a,b,c,w(a,b,c)))#출력방식은 지정되어 있음.
