#실버3 피보나치수, 어려움ㅠㅠ
fibo_0=[1,0]
fibo_1=[0,1]
cnt=int(input())
for i in range(cnt):#반복 출력
    n=int(input())#먼저 숫자를 받고
    if(n>1):
        for i in range(n-1):#여기서는 각각 앞에 값을 추가를 해주는 형태
            fibo_0.append(fibo_0[-1]+fibo_0[-2])
            fibo_1.append(fibo_1[-1]+fibo_1[-2])
    print(fibo_0[n],fibo_1[n])

