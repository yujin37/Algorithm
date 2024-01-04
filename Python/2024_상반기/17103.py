import sys

input = sys.stdin.readline
def make_primes(n):
    primes = [True] * (n+1)
    primes[0] = False #소수가 아님
    primes[1] = False #소수가 아님
    for i in range(2, int(n**(1/2))+1):
        if primes[i]:
            for j in range(i*i, n+1, i): #i의 제곱부터 n까지의 i배수 제거(소수가 아님)
                primes[j] = False
    return primes

primes = make_primes(1000000) #최대 범위까지 만들어놓음

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    
    for p in range(n//2 + 1): #n의 절반까지만 탐색하면 됨
        if primes[p] and primes[n-p]: #소수인지 확인을 하고 다른 값 하나도 확인해주면
            cnt += 1 #개수를 올린다.
    print(cnt) # 각 값을 출력
    
