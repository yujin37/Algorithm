a_1, a_0 = map(int,input().split())
c = int(input())
n = int(input())

f_n = a_1 * n + a_0
g_n = c * n

if f_n <= g_n and a_1 <= c:
    print(1)
else:
    print(0)