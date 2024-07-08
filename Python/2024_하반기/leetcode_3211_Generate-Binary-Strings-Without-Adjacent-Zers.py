class Solution:
    def make_substring(self, now): #각 숫자에 대한 업데이트
        substring = list()
        if now[-1] == '0': #만약 0이 마지막이면
            number = now + '1' #1만 추가
            substring.append(number)
        else: #그외의 경우에는 두가지 다 추가
            number = now + '1'
            substring.append(number)
            number = now + '0'
            substring.append(number)
        return substring
    def validStrings(self, n: int) -> list[str]:
        result = list()
        result.append('0')
        result.append('1')
        if n == 1: #1인 경우는 바로 리턴을 해줘야 한다.
            return result
        for i in range(2, n+1): #그외의 경우에는 돌려주기
            length = len(result)
            for j in range(length):
                check = self.make_substring(result[j]) #호출해서 새로 업데이트 된 값을
              
                result.extend(check) #추가해준다.
            result = [string for string in result if len(string) == i] #그리고 지금 길이가 아닌 이전 값은 삭제한다.
        return result
