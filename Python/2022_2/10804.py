#카드재배치
card=[]
for i in range(1,21):
    card.append(i)
for i in range(10):
    a,b=map(int,input().split())
    temp=card[a-1:b]
    temp=reversed(temp)
    card[a-1:b]=temp
for i in range(20): print(card[i], end=' ')#임시작업
   
