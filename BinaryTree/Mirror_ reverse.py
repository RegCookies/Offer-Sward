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
