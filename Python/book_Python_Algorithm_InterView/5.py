class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 투포인터 방식으로 체크한다.
        def expand(left, right) :
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1
            return s[left+1: right]
        
        # 길이가 짧거나 거꾸로 뒤집어도 같으면 바로 반환
        if len(s) < 2 or s == s[::-1]:
            return s
        
        #아니면 체크 들어간다.
        result = ''
        for i in range(0, len(s)-1):
            #기존 값, 홀짝 경우의 체크 중 가장 긴 것을 찾아 저장해준다.
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)
        return result
        