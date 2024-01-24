from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        seen = set()
        for char in s:
            counter[char] -=1 #일단 존재 횟수를 빼주고 
            if char in seen:  #한번 나온적 있으면 넣지 않는다.
                continue
            #만약 스택이 유효하고 문자가 맨 뒤 값보다 작으면서 횟수는 1번 이상 남으면
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop()) #스택에서 뽑고 본 것도 무효화한다.
            stack.append(char) #그리고 현재 것을 넣어준다.
            seen.add(char) #본 것에도 일단 추가해주고
        result = ''
        for i in range(len(stack)):
            result += stack[i]
        return result

