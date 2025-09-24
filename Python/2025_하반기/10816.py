import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
cards_dict = dict()
m = int(input())
find = list(map(int,input().split()))

for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1
for i in range(m):
    target = find[i]
    if target in cards_dict.keys():
        print(cards_dict[target], end = ' ')
    else:
        print(0, end=' ')    