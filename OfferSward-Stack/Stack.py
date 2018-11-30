class Mystack:
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