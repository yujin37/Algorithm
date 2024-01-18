class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif s[i] == ')':
                if stack.pop() != '(':
                    return False
            elif s[i] == '}':
                if stack.pop() != '{':
                    return False
            elif s[i] == ']':
                if stack.pop() != '[':
                    return False
        if len(stack) != 0:
            return False
        return True