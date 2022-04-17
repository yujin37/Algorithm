#실버4 카드2
import sys
import collections
n=int(sys.stdin.readline())#정수 주어지기
card=collections.deque([i for i in range(n)])
while(len(card)>1):
    del card[0]
    num=card.popleft()
    card.append(num)
print(card[0]+1)
