# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #처음에 none 처리 해야 함. 아니면 런타임 에러 걸림
        if head is None:
            return None 
        
        #왼쪽 오른쪽 시작점 설정
        left = head
        right = head.next
        right_head = head.next

        #홀짝 연결 리스트 만들어주기
        while right and right.next:
            left.next = left.next.next
            left = left.next

            right.next = right.next.next
            right = right.next
        
        #홀수 끝에 짝수를 붙여준다.
        left.next = right_head

        return head

