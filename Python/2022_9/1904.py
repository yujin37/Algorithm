#백준, dp연습
n=int(input())
num=[0]*(n+1)

if n==1: #런타임 에러땜에 넣어야 함, 아무래도 for 문돌리는 것 때문인듯)
    print(1)
    exit()
num[1]=1
num[2]=2

for i in range(3,len(num)):
    num[i]=(num[i-2]+num[i-1])%15746
print(num[-1])

''' 함수구현
n=int(input())


def test(n):
    num=[0]*(n+1)
    if n==1:
        return 1
    num[1]=1
    num[2]=2

    for i in range(3,len(num)):
        num[i]=(num[i-2]+num[i-1])%15746
    return num[-1]
print(test(n))

'''
