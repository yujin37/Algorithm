import sys 
input = sys.stdin.readline
n, attack = map(int,input().split())
def solution(n,attack):
    current_life = 0
    damage = 0
    max_life = 0
    for i in range(n):
        t, a, h = map(int,input().split())
        if t == 1:
            #용사의 공격력 만큼 몬스터의 생명력 깎기
            get = h%attack 
            if get == 0 : #만약 나누어 떨어지면
                damage = -(a*(h//attack-1)) #몬스터 공격력 * (생명력/ 공격력-1)
            else:
                damage = -(a*(h//attack)) #몬스터 공격력 * (생명력/ 공격력)
        else: #2가 입력될때
            attack += a #공격력 증가시키고
            damage = h #데미지를 회복시킨다.
        current_life += damage #현재 생명에다가 데미지를 증가시키는데
        if current_life > 0: #0보다 크면 필요없기 때문에
            current_life = 0
        max_life = max(max_life, -1* current_life)
    return max_life+1
 
print(solution(n, attack))