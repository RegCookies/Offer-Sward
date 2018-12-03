class BitNode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None



def SharedParent(root,node1,node2):
    if root == None or root == node1 or root == node2:
        return root

    lchild = SharedParent(root.lchild,node1,node2)
    rchild = SharedParent(root.rchild,node1,node2) 
    
    if lchild == None: 
        return rchild
    elif rchild == None:
        return lchild
    else:
        return root 

def distance(root,node,length):
    if root is None: 
        return -1 
    if root == node:
        return length
    lev = distance(root.lchild,node,length+1)
    if lev == -1:
        distance(root.rchild,node,length+1)
    else:
        return lev
if __name__ == "__main__":
    node1 = BitNode(6) 
    node2 = BitNode(3)
    node3 = BitNode(1)
    node4 = BitNode(7)
    node5 = BitNode(4)
    node6 = BitNode(5)
    node7 = BitNode(8)

    node1.lchild = node2
    node1.rchild = node3
    node2.lchild = node4
    node2.rchild = node5
    node3.lchild = node6
    node3.rchild = node7

    
    parent = SharedParent(node1,node4,node5) 
    print(parent.val)
    length = 0
    depth = distance(node1,node4,length)
    print(depth)