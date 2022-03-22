#bronze1
N=int(input())
Num=list(map(int,input().split()))
max=Num[0]
total=0
for i in range(N):
    if(max<Num[i]):
        max=Num[i]
for i in range(N):
    Num[i]=(Num[i]/max*100)
    total+=Num[i]
print(total/N)
