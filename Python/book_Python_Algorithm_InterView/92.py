# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(None)

        if head is None or left == right: #값 바꾸는 위치가 같거나 none이면 그대로 리턴
            return head

        root.next = head #시작점 연결시키기

        for _ in range(left-1): #입력받은 left전까지 이동시키고
            start = start.next
        end = start.next #일단 안 겹치게 두고

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next #다음 연결지점을 계속 갱신
            start.next.next = tmp #앞에서 새로 연결된 시작점 다음에 기존 시작점을 그다음으로 연결
        return root.next