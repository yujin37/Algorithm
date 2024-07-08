class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result = '' # 결과 값을 저장한다.
        for c in range(len(s)):
            now = (c + k) % len(s) #일단 이동 값 더해주고 다시 길이만큼 나누어서 나머지 구한다.
            result += s[now] #해당 값을 더해준다.
        return result