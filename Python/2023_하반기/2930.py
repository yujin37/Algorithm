r = int(input())
master = list(input())
n = int(input())
result = []

def game(friend):
    score = 0
    for j in range(r):
        if master[j] == 'S' and friend[j] == 'P':
            score += 2
        elif master[j] == 'P' and friend[j] == 'R':
            score += 2
        elif master[j] == 'R' and friend[j] == 'S':
            score += 2
        elif master[j] == friend[j]:
            score += 1
        else:
            score += 0
    return score
def game2(friend):
   
    check = []
    for i in range(r):
        score_s, score_p, score_r = 0,0,0
        for j in friend:
            if j[i] == "S":
                score_s += 1
            elif j[i] == "P":
                score_p += 1
            elif j[i] == "R":
                score_r += 1
        check.append([score_s, score_p, score_r])
    friend_score= 0
    for i in check:
        friend_score += max(i[2] * 2 + i[1] * 1, i[1]* 2 + i[0] * 1 , i[0]*2 + i[2]*1 )  
    print(friend_score)
result2 = []
for i in range(n):
    tmp = list(input())
    result.append(game(tmp))
    result2.append(tmp)
print(sum(result))
game2(result2)

