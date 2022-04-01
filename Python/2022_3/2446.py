#별찍기9
a=int(input())
for i in range(1,a):
    print(" "*(i-1)+"*"*(2*(a-i)+1))
for i in range(a,0,-1):
    print(" "*(i-1)+"*"*(2*(a-i)+1))
