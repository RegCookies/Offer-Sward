class BitNode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None

def FindRoad(root,num,sums,v):
    #记录当前的节点
    
    sums += root.val
    v.append(root.val)
    if root.lchild == None and root.rchild == None and sums == num:
        i = 0
        while i< len(v):
            print(v[i])
            i += 1
        
    if root.lchild != None :
        FindRoad(root.lchild,num,sums,v) 
    if root.rchild != None : 
        FindRoad(root.rchild,num,sums,v) 
    sums -= v[-1]
    v.remove(v[-1]) 
