#연결 리스트 구조로 짜기

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
def combine_array(arr1, arr2):
    result = []
    while arr1 and arr2:
        if arr1.val <= arr2.val:
            result.append(arr1.val)
            arr1 = arr1.next 
        else:
            result.append(arr2.val)
            arr2 = arr2.next 
    while arr1 is not None:
        result.append(arr1.val)
        arr1 = arr1.next 
    while arr2 is not None:
        result.append(arr2.val)
        arr2 = arr2.next 
    return result
n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_new = create_linked_list(a)
b_new = create_linked_list(b)

result_array = combine_array(a_new, b_new)
for val in result_array:
    print(val, end = ' ')
