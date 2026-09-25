class MyQueue:

    def __init__(self):
        self.arr1=[]

    def push(self, x: int) -> None:
        self.arr1.append(x)


    def pop(self) -> int:
        first_ele=self.arr1[0]
        self.arr1 = self.arr1[1:]
        return first_ele


    def peek(self) -> int:
        return self.arr1[0]

    def empty(self) -> bool:
        if self.arr1:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()