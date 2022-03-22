#bronze3
N,X=map(int,input().split())
Num=list(map(int,input().split())) #리스트 입력 받을때 여러개 변수 입력받는 것을 list()로 감싸주면 된다.
for i in range(N):
    if(Num[i]<X): #이것은 c언어와 비슷
        print(Num[i],end=" ")#파이썬은 그냥 print(num[i])하면 enter가 되는데 이를 방지하기 위해 ',end=" "'라고 해주면 enter없이 space로 해줌
