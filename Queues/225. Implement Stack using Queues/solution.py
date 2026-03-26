class MyStack:

    def __init__(self):
        #Empty queue so it will be equal to None
        self.q = None
        

    def push(self, x: int) -> None:
        #Use the double ended queue datatype from collections
        self.q = deque([x, self.q])
        #This instatiates the queue with x at the end and the rest of the queue at the front

    def pop(self) -> int:
        #Grab the popped element at the beginning
        popped = self.q.popleft()
        #Ensure that the q is set equal to the q after that element is removed
        self.q = self.q.popleft()
        #Return that element
        return popped

    def top(self) -> int:
        #Return the first element in the stack
        return self.q[0]

    def empty(self) -> bool:
        #Return if self.q is empty
        return not self.q