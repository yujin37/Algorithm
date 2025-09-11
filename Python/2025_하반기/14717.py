from itertools import combinations
a, b = map(int,input().split())

cards = [i for i in range(1,11)] * 2
#영학이가 뽑은 카드는

if a == b:
    my_score = (a, True)  #true는 땡 
else:
    my_score = ((a+b)%10, False) #false는 끗

#영학이가 뽑은 카드 제외
cards.remove(a)
cards.remove(b)
result = 0
#남은 카드로 전체 경우의 수 만들기
for x, y in combinations(cards, 2):
    if x==y:
        opp_score = (x, True)
    else:
        opp_score= ((x+y)%10, False)
    #이제 최종 비교 진행하기
    
    if my_score[1] == True and opp_score[1] == False:
        result += 1
    elif my_score[1] == True and opp_score[1] == True and my_score[0] > opp_score[0]:
        result += 1
    elif my_score[1] == False and opp_score[1] == False and my_score[0] > opp_score[0]:
        result += 1



total = len(list(combinations(cards,2)))

print('%0.3f' % float(float(result)/float(total)))
    