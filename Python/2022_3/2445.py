#별찍기8
a=int(input())
for i in range(1,a):
    print("*"*i+" "*(2*(a-i))+"*"*i)
for i in range(a,0,-1):
    print("*"*i+" "*(2*(a-i))+"*"*i)
