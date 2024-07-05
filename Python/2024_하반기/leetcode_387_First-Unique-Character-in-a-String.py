class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = dict()
        for char in s:
            if char in result and (result[char] != -1 or result[char] == -1):
                result[char] = -1
            else:
                result[char] = s.index(char)
        num = -1
        for _, value in result.items():
            if num < 0 and value >= 0:
                num = value
            elif num < 0 and value < 0:
                pass
            elif num >= 0 and value >= 0 and value < num:
                num = value
            else:
                pass
        return num
#두번째 솔루션
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = dict()
        previous = list()
        for char in s:
            if char in previous: #여러번 나오는 경우
                pass
            elif char in queue: #만약 한번 나온적있으면
                del queue[char]
                previous.append(char)
            else: #처음 나오면
                queue[char] = s.index(char)
                #previous.append(char)
        #print(queue, previous )
        result = -1
        if queue:
            result = queue.get(next(iter(queue)))
            
        #print(result)
        return result
'''
solution = Solution()
print(solution.firstUniqChar("loveleetcode"))