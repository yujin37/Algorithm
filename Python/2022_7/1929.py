#실버3 1929 소수구하기

#라이브러리 사용 x
import sys
import math
input=sys.stdin.readline

m,n=map(int,input().split())

result='True'
def number(num):
    if num<2:
        return False
    for j in range(2,int(math.sqrt(num)+1)):
        if num%j==0:
            return False
    return True

for i in range(m,n+1):

    result=number(i)
    if result==True:
        print(i)
    else:
        pass

#라이브러리 사용 ver.
import sys
import math
input=sys.stdin.readline

m,n=map(int,input().split())

result='True'
def number(num):
    if num<2:
        return False
    for j in range(2,int(math.sqrt(num)+1)):
        if num%j==0:
            return False
    return True

for i in range(m,n+1):
    result=number(i)
    if result==True:
        print(i)
    else:
        pass
