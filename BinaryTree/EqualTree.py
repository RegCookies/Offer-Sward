class BitNode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None
    
def isEqual(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None and root2 is not None:
        return False
    if roo1 is not None and root2 is None:
        return False 
    
    if root1.val == root2.val:
        return isEqual(root1.lchild,root2.lchild) and isEqual(root1.rchild, root2.rchild)
    else:
        return False



def constructT():
    root = BitNode(6)
    node1 = BitNode(3) 
    node2 = BitNode(-1)
    node3= BitNode(7)
    node4 = BitNode(9)
    node5 = BitNode(11)
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node5
        
    node2.rchild = None
    node3.lchild = node3.rchild =None
    node4.lchild = node4.rchild =None
    node5.lchild = node5.rchild =None

if __name__ == "__main__":
    root1 = constructT()
    root2 = constructT() 
    
    equal = isEqual(root1,root2)
    
    if equal:
        print("Yes") 
    else:
        print("No")