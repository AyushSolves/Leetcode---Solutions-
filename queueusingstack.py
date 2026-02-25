class MyQueue:

    def __init__(self):
        self.stack1 = []  
        self.stack2 = [] 

    def push(self, x: int) -> None:
        self.stack1.append(x)

    # Removes and returns front element
    def pop(self) -> int:
        self._move()
        return self.stack2.pop()

    # Returns front element
    def peek(self) -> int:
        self._move()
        return self.stack2[-1]

    # Returns True if empty
    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    # Helper function to move elements
    def _move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

if __name__ == "__main__":
    q = MyQueue()

    q.push(1)
    q.push(2)

    print("Peek:", q.peek())   
    print("Pop:", q.pop())     
    print("Empty:", q.empty()) 