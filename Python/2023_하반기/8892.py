from collections import deque
from itertools import permutations
#----------------------
# 풀이 1
#-----------------------
# 펠린드롬 여부 체크
def check_Palindrome(s):
    s = deque(s)
    while len(s) > 1:
        if s.popleft() != s.pop():
            return False
    return True

 
    
t = int(input()) # 테스트 케이스
for i in range(t):
    k = int(input()) # 공책에 적혀있는 단어의 수
    words = []
    for j in range(k):
        word = input()
        words.append(word)
        
    # 2개만 조합하면 되므로 permutation 라이브러리로 조합 만들어줌
    combine_word_tuple = list(permutations(words, 2))
    combine_word = [''.join(word_tuple) for word_tuple in combine_word_tuple]
    
    Palidrome = []
    for n in range(len(combine_word)):
        result = check_Palindrome(combine_word[n]) #여부 확인해서 가져온다.
        
        if result: #있으면 리스트 담아준다.
            Palidrome.append(combine_word[n])
            
    if Palidrome:
        print(Palidrome[0]) #값이 있으면 첫번째 값 출력해주고
    else:
        print(0) #아니면 0을 출력하도록 한다.
#----------------------
# 풀이 2
#-----------------------
'''
# 펠린드롬 여부 체크
def check_Palindrome(s):
    left, right = len(s)-1,0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -=1
        right += 1
    return s[left+1: right]

 
    
t = int(input()) # 테스트 케이스
for i in range(t):
    k = int(input()) # 공책에 적혀있는 단어의 수
    words = []
    for j in range(k):
        word = input()
        words.append(word)
        
    # 2개만 조합하면 되므로 permutation 라이브러리로 조합 만들어줌
    combine_word_tuple = list(permutations(words, 2))
    combine_word = [''.join(word_tuple) for word_tuple in combine_word_tuple]
    
    Palidrome = []
    for n in range(len(combine_word)):
        result = check_Palindrome(combine_word[n]) #여부 확인해서 가져온다.
        
        
        if result: #있으면 리스트 담아준다.
            Palidrome.append(combine_word[n])
   
    if Palidrome:
        print(Palidrome[0]) #값이 있으면 첫번째 값 출력해주고
    else:
        print(0) #아니면 0을 출력하도록 한다.
'''