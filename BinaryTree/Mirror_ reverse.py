class BitNode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None


def reverseTree(root):
    if root is None:
        return 
    
    reverseTree(root.lchild)
    reverseTree(root.rchild)
    root.lchild,root.rchild = root.rchild,root.lchild
    
def printT(root):
    if root is None:
        return None 
    queue = [root]
    result = []
    while queue :
        result.append(queue[0].val) 
        if queue[0].lchild != None:
            queue.append(queue[0].lchild)
        if queue[0].rchild != None: 
            queue.append(queue[0].rchild)
        queue.pop(0)
    return result
if __name__ == "__main__":
    root = BitNode(1) 
    node1 = BitNode(2)
    node2 = BitNode(3)
    node3 = BitNode(4)
    node4 = BitNode(5)
    node5 = BitNode(6)
    node6 = BitNode(7)

    root.lchild = node1 
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node5
    node2.rchild = node6
     
    reverseTree(root)
    
    a = printT(root) 
    
    print(a)