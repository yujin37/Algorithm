#bronze 3
H,M=map(int,input().split())
#분
if(M>=45):
    M-=45
else:
    if(H-1<0):
        H=24
    H-=1
    M=60-(45-M)
print(H, M)
