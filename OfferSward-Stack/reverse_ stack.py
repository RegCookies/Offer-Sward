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


# 翻转栈的元素：
####### move stack bottom to the top ######################## 

def moveBottomToTop(s):
    if s.empty():
        return None
    
    top1 = s.peek()
    s.pop() 
    
    if not s.empty():
        moveBottomToTop(s)

        top2 = s.peek()
        s.pop()
        
        s.push(top1)
        s.push(top2) 
    else:
        s.push(top1)
    
    
def reverse_stack(s):
    if s.empty():
        return None
    moveBottomToTop(s)
    top = s.peek()
    s.pop()

    reverse_stack(s) 
    s.push(top)
    

if __name__ == "__main__":
    s = Mystack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    reverse_stack(s)
    
    while not s.empty():
        print(s.peek())
        s.pop()