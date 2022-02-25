#숫자
num1,num2=list(map(int,input().split())) #아래 min,max와 같은 변수 쓰면 오류남.
n1=min(num1,num2)
n2=max(num1,num2)

if(n1==n2 or n1+1==n2):
    print("0")
else:
    print(n2-n1-1)
    for i in range(n1+1,n2):
        print(i, end=" ")
