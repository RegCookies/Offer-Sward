class MyQueue:
    def __init__(self):
        self.item = []
        self.front = 0 
        self.back = 0 
    def isEmpty(self):
        return self.front == self.back
    
    def length(self):
        return self.back - self.front
    
    def getFront(self):
        if self.isEmpty():
            return None
        else:
            return self.item[self.front]
        
    def getBack(self): 
        if self.isEmpty():
            return None
        else:
            return self.item[self.back]

    def deQueue(self):
        if self.back > self.front:
            self.front +=1
        else: 
            return None

    def enQueue(self,element):
        self.item.append(element)
        self.back +=1



    def printEle(self):
        return self.item[self.front:self.back]

if __name__ == "__main__":
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    a = queue.printEle()
    print(a)
    queue.deQueue()
    a = queue.printEle()
    print(a)