#bronze2/ if we need to fast input, please sys.stdin.readline(). This enter the input area. And add 'import sys', before start.
import sys
T=int(input())
for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
