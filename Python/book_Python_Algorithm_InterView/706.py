import collections
class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None: #만약 없으면 
            self.table[index] = ListNode(key, value) #생성해주고
            return #리턴
        p = self.table[index] #아니라면 기준을 잡고
        while p: #반복문을 돌린다. 
            if p.key == key: #현재 키라면
                p.value = value #값을 넣어주고
                return #리턴해준다.
            if p.next is None: #만약 다음게 없으면
                break #멈추고
            p = p.next #다음으로 이동하게 한다.
        p.next = ListNode(key, value) #그리고 다음것을 생성한다. 

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None: #만약 없으면
            return -1 #리턴 -1하고
        p = self.table[index] #있으면
        while p: #찾아본다.
            if p.key == key: #같은 키를 찾으면
                return p.value #값을 리턴해준다.
            p = p.next #아니면 탐색 들어간다. 
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None: #만약 삭제하려는데 비워져있으면
            return #아무일도 없다.
        
        #인덱스의 첫번째 노드이면
        p = self.table[index] #현재 값을 잡고
        if p.key == key: #같은지만 확인해서
            self.table[index] = ListNode() if p.next is None else p.next
            return #마지막이면 다시 생성해주면서 삭제하고 아니면 다음으로 넘긴다.
        
        #연결리스트 노드 삭제
        prev = p #이전 노드와 현재 노드를 일단 위치시키고
        while p:
            if p.key == key:  
                prev.next = p.next #이전 노드를 다음으로 넘기고
                return #리턴한다.
            prev, p = p, p.next #하나씩 탐색해준다. 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)