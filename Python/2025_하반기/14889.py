import sys
input = sys.stdin.readline
from itertools import combinations, permutations
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
members = [i for i in range(n)]
teams = list(combinations(members, n//2))
final_result = 100
for i in range(len(teams)):
    team1 = list(teams[i])
    team2 = [x for x in members if x not in team1]
    
    #각 팀의 능력치 확인하기
    #스타트팀 team1
    energy1 = list(permutations(team1, 2))
    energy2 = list(permutations(team2, 2))
    result_energy1 = 0
    result_energy2 = 0
    for i in range(len(energy1)):
        result_energy1 += board[energy1[i][0]][energy1[i][1]]
        result_energy2 += board[energy2[i][0]][energy2[i][1]]
        
        #print(abs(result_energy1-result_energy2))
    final_result = min(final_result, abs(result_energy1-result_energy2))
print(final_result)