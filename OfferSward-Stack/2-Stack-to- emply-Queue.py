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



class Myqueue:
    def __init__(self):
        self.A = Stack() 
        self.B = Stack() 

    def push(self,val): 
        self.A.push(val)

    def pop(self):
        if self.B.empty():
            while not self.A.empty():
                self.B.push(self.A.peek()) 
                self.A.pop()
        first =self.B.peek() 
        self.B.pop()
        
        return first

if __name__ == "__main__":
    s = Myqueue() 

    s.push(1) 
    s.push(5)
    s.push(7) 
    print(s.pop())  
