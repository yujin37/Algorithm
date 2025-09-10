import sys
from itertools import *
input = sys.stdin.readline

def triangle_sum(n):
    T = []
    #삼각수 공식 
    for i in range(1,n+1):
        now_num = i*(i+1)//2
        if now_num > n:
            break
        T.append(now_num)
    check = list(product(T, repeat=3))
    for numbers in check:
        if sum(numbers) == n:
            return 1
    return 0
   
k = int(input())
for i in range(k):
    num = int(input())
    result = triangle_sum(num)
    print(result)