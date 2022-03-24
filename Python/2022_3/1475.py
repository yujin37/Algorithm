#방번호
n=input()
num=[0]*10
mix=0

for i in n:
    if(i=='6' or i=='9'):
        mix+=1
    else:
        num[int(i)]+=1

if(mix%2==0):
    mix=mix//2
else:
    mix=mix//2+1
num[6]=mix
print(max(num))
