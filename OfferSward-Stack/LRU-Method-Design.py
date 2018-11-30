from collections import deque

class LRU:
    def __init__(self,cacheSize):
        self.cacheSize = cacheSize
        self.q = deque()
        self.set = set() 
    def isFull(self):
        return len(self.q) == self.cacheSize
    def enQueue(self,val):
        if self.isFull():
            self.set.remove(self.q[-1])
            self.q.pop()
        self.q.appendleft(val)
        self.set.add(val) 

    def accessPage(self,val): 
        if val not in self.set: 
            self.enQueue(val) 
        elif val != self.q[0]:
            self.q.remove(val)
            self.q.appendleft(val) 
    def printQueue(self):
        while len(self.q)> 0:
            print(self.q.popleft())
if __name__ == "__main__":
    lru = LRU(3)
    
    lru.accessPage(1)
    lru.accessPage(3)
    lru.accessPage(5)
    lru.accessPage(7)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)

    lru.printQueue()