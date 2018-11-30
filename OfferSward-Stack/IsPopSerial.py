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


def IsPopSerial(push,pop): 
    if pop == None or push == None:
        return False

    pushLen = len(push)
    popLen = len(pop)
    
    if pushLen != popLen:
        return False

    stack = Mystack()
    pushIndex = 0
    popIndex = 0
    while pushIndex < pushLen:
        stack.push(push[pushIndex]) 
        pushIndex += 1
        
        while not stack.empty() and stack.peek() == pop[popIndex]:
            stack.pop()
            popIndex +=1 

    return stack.empty() and pushIndex == popIndex


if __name__ == "__main__":
    push = [1,2,3,4,5]
    pop = [5,4,3,2,1] 
    
    if IsPopSerial(push,pop):
        print('yes')
    else:
        print("Noe")