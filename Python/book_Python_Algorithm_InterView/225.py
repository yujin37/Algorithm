import collections 
class MyStack:

    def __init__(self):
        self.q = collections.deque() #큐를 만들기 위해 초기 설정
        

    def push(self, x: int) -> None:
        self.q.append(x) #위 큐에 값을 추가해준다.



    def pop(self) -> int:
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()