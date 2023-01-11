def check(number):
    if number == 1:
        return False
    for k in range(2,int(number**0.5+1)):
        if number%k==0:
            return False
    else:
        return True

t=int(input())
for i in range(t):
    num=int(input())
    n1,n2=num//2,num//2
    while n1>0:
        if check(n1) and check(n2):
            print(n1,n2)
            break
        else:
            n1-=1
            n2+=1
