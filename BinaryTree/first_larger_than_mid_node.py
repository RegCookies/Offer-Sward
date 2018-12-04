class BitNode: 
    def __init__(self,val):
        self.val =val
        self.lchild = None
        self.rchild = None


def getMin(root):
    if root is None:
        return root
    while root.lchild != None:
        root = root.lchild
    return root

def getMax(root):
    if root is None:
        return root
    while root.rchild != None:
        root =  root.rchild
    return root

def getNode(root):
    maxN =getMax(root)
    minN = getMin(root)
    
    mid_val = (maxN.val + minN.val )/2
    print(mid_val)
    result = None
    while root != None:
        if root.val <= mid_val:
            root = root.rchild
        else:
            result = root
            root = root.lchild
    return result

if __name__ == "__main__":
    root = BitNode(4) 
    node1 = BitNode(2)
    node2 = BitNode(6)
    node3 = BitNode(1)
    node4 = BitNode(3)
    node5 = BitNode(5)
    node6 = BitNode(7)

    root.lchild = node1 
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node5
    node2.rchild = node6
    
    result = getNode(root)
    print(result.val)