from collections import deque 

class User:
    def __init__(self,id,name):
        self.id = id 
        self.name = name
        self.seq= ()

    def GetName(self):
        return self.name
    def GetId(self):
        return self.id 

    def SetName(self,name): 
        self.name = name

    def GetSeq(self):
        return self.GetSeq
    def setSeq(self,seq):
        self.seq = seq
    def toString(self):
        return 'id:' +  str(self.id) + "name" + str(self.name) +  "seq:" + str(self.seq)

class MyQueue: 
    def  __init__ (self):
        self.q = deque()
    
    def enQueue(self,u):
        u.setSeq(len(self.q)+1) 
        self.q.append(u) 
    def deQueue(self): 
        self.q.popleft()
        self.updateQueue() 
    
    def deQueueRemove(self,u):
        self.q.remove(u)
        self.updateQueue() 
    
    def updateQueue(self):
        i = 1
        for u in self.q: 
            u.setSeq(i) 
            i+=1
    def printQueue(self):
        for u in self.q:
            print(u.toString())

if __name__ == "__main__":
    u1 = User(1,'USER1')
    u2 = User(2,'USER2')
    u3 = User(3,'USER3')
    u4 = User(4,'USER4')
    u5 = User(5,'USER5') 

    queue = MyQueue() 
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.enQueue(u5)
    
    queue.deQueue()
    queue.deQueueRemove(u2) 
    queue.printQueue()

