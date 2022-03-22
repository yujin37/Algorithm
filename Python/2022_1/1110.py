#bronze1
N=int(input())
num=N
count=0
while True:
    num1=num//10
    num2=num%10
    num3=(num1+num2)%10
    num=num2*10+num3
    count+=1
    if(num==N):
        break
print(count)

