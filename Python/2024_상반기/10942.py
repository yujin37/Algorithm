import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def is_Palindrom(check, s, e, dp):
    if s >= e:
        return True
    if dp[s][e] is not None:
        return dp[s][e]
    result = (check[s] == check[e] and is_Palindrom(check,s+1, e-1, dp))
    dp[s][e] = result
    return result
n = int(input())
palindrom = list(map(int,input().split()))
m = int(input())
result = []
dp = [[None] * (n+1) for _ in range(n+1)]
for i in range(m):
    s, e = map(int,input().split())
    if is_Palindrom(palindrom, s-1, e-1, dp):
        result.append(1)
    else:
        result.append(0)
for i in range(m):
    print(result[i])
    
            