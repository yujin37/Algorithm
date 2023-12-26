from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list = []
        alpha_list = []
        for log in logs:
            message = log.split(' ')
            if message[1].isdigit():
                digit_list.append(log)
            else:
                alpha_list.append(log)
        alpha_list.sort(key=lambda x:(x.split()[1:], x.split()[0]))

        return alpha_list + digit_list