class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    def size(self):
        return self.rear - self.front

    def getFront(self):
        return self.arr[self.front] if not self.isEmpty else None
    
    def getBack(self):
        return self.arr[self.rear-1] if not self.isEmpty else None
    
    def deQueue(self):
        return self.front += 1 if self.rear > self.front else None
    
    def enQueue(self,val):
        self.arr.append(val) 
        self.rear += 1