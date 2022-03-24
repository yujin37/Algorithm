#휴대폰요금
N=int(input())
phone=list(map(int,input().split()))
Y=0
M=0
for i in phone:
    Y+=i//30*10+10
    M+=i//60*15+15
if Y<M:
    print("Y %d" %Y)
elif Y>M:
    print("M %d" %M)
else:
    print("Y M %d" %Y)
