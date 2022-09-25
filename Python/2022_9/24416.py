#골드1 피보나치수, 다이나믹 프로그래밍 연습, pypy로 통과
def fib(n): #다이나믹 프로그래밍
    fibo=[]
    cnt=0
    cnt_2=0
    while cnt<=n:
        if cnt==0:
            fibo.append(0)
        elif cnt==1:
            fibo.append(1)
        else:
            temp=fibo[cnt-1]+fibo[cnt-2]
            cnt_2+=1
            fibo.append(temp)
        cnt+=1
    print(cnt_2-1)
    return fibo[-1]
def fib_1(n): #단순 
    if n==1 :
        return 1
    elif n==2:
        return 1
    else:
        return fib_1(n-1)+fib_1(n-2)
n=int(input())
print( fib_1(n), end=' ')
fib(n)
