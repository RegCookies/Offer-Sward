class Stack:
    def __init__(self):
        self.item = []
    

    def empty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.size)
        
    def peek(self):
        if not self.empty():
            return self.item[len(self.item)-1]
            
        else:
            return None

    def pop(self):
        if not self.empty():
            return self.item.pop()
        else:
            return None

    def push(self,val):
        return self.item.append(val) 



class MyStack:
    def __init__(self):
        self.eleStack = Stack()
        self.minStack = Stack()

    def push(self,val):
        self.eleStack.push(val)

        if self.minStack.empty():
            self.minStack.push(val)
        
        else:
            if val < self.minStack.peek():
                self.minStack.push(val) 

        
    def pop(self):
        topVal = self.eleStack.peek()
        self.eleStack.pop()
        
        if topVal == self.mins():
            self.minStack.pop() 
        
        return topVal

    def mins(self):
        if self.minStack.empty():
            return 2*32
        else: 
            return self.minStack.peek() 
    

if __name__ == "__main__":
    stack = MyStack() 
    stack.push(5) 
    print(stack.mins())
    stack.push(1)
    print(stack.mins())