import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))
operatorSet = []
op = ['+', '-', '*', '/']
for i in range(4):
    for j in range(operator[i]):
        operatorSet.append(op[i])

order_op = list(permutations(operatorSet,n-1))

min_result = 10**9
max_result = -10**9 

for i in range(len(order_op)):
    now = nums[0]
    for j in range(1, n):
        if order_op[i][j-1] == '+':
            now += nums[j]
        elif order_op[i][j-1] == '-':
            now -= nums[j]
        elif order_op[i][j-1] == '*':
            now *= nums[j]
        elif order_op[i][j-1] == '/':
            if now < 0:
                now = abs(now) // nums[j] * (-1)
            else:
                now = now // nums[j]
    min_result = min(min_result, now)
    max_result = max(max_result, now)
print(max_result)
print(min_result)