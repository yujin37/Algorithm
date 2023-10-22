n = int(input())
vote = []
dasom = int(input())
for i in range(n-1):
    vote.append(int(input()))
cnt = 0
i = 0
if n > 1:
    while dasom+cnt <= max(vote):
        tmp = vote.index(max(vote))
        vote[tmp] -= 1
        cnt+=1
    print(cnt)
else:
    print(0)