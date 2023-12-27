from typing import List
import re
class Solution:
    def find_word(self,words,banned):
        word_list=[]
        
        
        for word in words:
            if word.lower() not in banned: #빈칸이면서 단어가 금지 단어가 아닐때
                word= word.lower()
                word_list.append(word)
                
            else: pass
        if word != '':
            word_list.append(word.lower())
        return word_list
    def cnt_word(self, word_list):
        cnt = {}
        for word in word_list:
            if word in cnt:
                cnt[word] += 1
            else:
                cnt[word] = 1
        if cnt:
            return max(cnt, key=cnt.get)
        else:
            return None
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).split()]
        word_list=self.find_word(words, banned)
        return self.cnt_word(word_list)
        
